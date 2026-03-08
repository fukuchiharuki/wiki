---
title: "Spring Boot/Data JPA/エンティティを実装する"
date: 2023-02-07T19:31:34+09:00
last_modified_at: 2023-02-07T19:31:34+09:00
---

# キーワード

- JPA
- Spring Boot
- Kotlin

# 目次

<!-- TODO: #contents -->

# したいこと

ひとまず最小でありがちな関連と永続化処理を実装したい。

# エンティティ（単体）

まずはただIDで識別できる単独の実体。

## モデル

{% raw %}
```
@Entity
class User(
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  var name: String = "",

  @Version
  var version: Long = -1
)
```
{% endraw %}

### エンティティにはIDが必要

JPAのエンティティはID（プライマリキー）を持つ、のが基本。

### @Versionを設定

エンティティを楽観ロックするならバージョンを設ける。

## 永続化処理

{% raw %}
```
User(name = "山田太郎")
  .also { entityManager.persist(it) }
```
{% endraw %}

### Kotlinで実装する場合デフォルト値の定義が必要

Kotlinでエンティティを実装する場合、デフォルト値を定義しておく必要がある。デフォルト値を定義しておかないと、エンティティ永続化時にエラーが発生する。永続化時に値があるかどうかではないことに注意。エラーメッセージからだと原因がなんとも想像つかない。

{% raw %}
```
detached entity passed to persist spring jpa
```
{% endraw %}

# 伝票・明細、集約等（１対多）の関係

伝票・明細の関係。伝票単位で明細も含めて一式保存するものとして。

## モデル

Slipを伝票、Detailを明細として。

{% raw %}
```
@Entity
class Slip(
  @OneToMany(mappedBy = "slip", cascade = [CascadeType.ALL], orphanRemoval = true)
  var details: MutableList<Detail> = emptyList<Detail>().toMutableList()

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  var name: String = "",

  @Version
  var version: Long = -1
)
```
{% endraw %}

{% raw %}
```
@Entity
class Detail(
  @ManyToOne
  @JoinColumn(name = "slip_id", referencedColumnName = "id")
  var slip: Slip? = null,

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  var name: String = ""
)
```
{% endraw %}

### @OneToManyの設定

<dl>
<dt>mappedBy</dt>
<dd>伝票側エンティティが明細側エンティティから何として関連しているか</dd>
<dt>cascade</dt>
<dd>明細側エンティティにカスケードする永続化オペレーション</dd>
<dt>orphanRemoval</dt>
<dd>リレーションから削除した明細側エンティティに削除操作を適用する</dd>
</dl>

### @ManyToOne (@JoinColumn)の設定

<dl>
<dt>name</dt>
<dd>伝票側エンティティを指定する明細側エンティティ上の外部キー</dd>
<dt>referencedColumnName</dt>
<dd>その外部キーに該当する伝票側エンティティの主キー</dd>
</dl>

### 伝票側に@Versionを設定

伝票側エンティティに楽観ロック用のバージョンを設ける。

## 永続化処理

{% raw %}
```
Slip(name = "伝票")
  .apply { detils.add(Detail(slip = this, name = "明細")) }
  .also { entityManager.persist(it) }
```
{% endraw %}

### 明細側エンティティの永続化処理は不要

永続化オペレーションをカスケードするのでpersistするのは伝票側エンティティだけでいい。

# イベントやログ、ジョブ等（多対１）の関係

ある実体に紐づくイベントやログ、ジョブ等の関係。親側エンティティの単位で子側エンティティ（イベントやログ、ジョブ等）を保存しないものとして。

## モデル

Dealを取引、DealEventを取引イベントとして。

{% raw %}
```
@Entity
class Deal(
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  @Version
  var version: Long = -1
)
```
{% endraw %}

{% raw %}
```
@Entity
class DealEvent(
  @ManyToOne
  @JoinColumn(name = "foo_id", referencedColumnName = "id")
  var deal: Deal? = null,

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  var name: String = "",

  var raisedAt: LocalDateTime = LocalDateTime.now()
)
```
{% endraw %}

### @ManyToOne (@JoinColumn)の設定

伝票・明細、集約等（１対多）の関係、明細側のエンティティと同じ。

<dl>
<dt>name</dt>
<dd>親側エンティティを指定する子側エンティティ上の外部キー</dd>
<dt>referencedColumnName</dt>
<dd>その外部キーに該当する伝票側エンティティの主キー</dd>
</dl>

## 永続化処理

{% raw %}
```
entityManager.find(Deal::class.java, dealId)
  ?.let { DealEvent(deal = it, name = "取引イベント") }
  ?.also { entityManager.persist(it) }
```
{% endraw %}

### managedな親側エンティティが必要

子側エンティティにセットする親側エンティティはmanagedである必要がある（はず）。

# カーソルとスナップショット等（１対１）の関係

ある実体を指すカーソルとしての関係。カーソルはすでに存在するスナップショット等を指すものとして。

## モデル

{% raw %}
```
@Entity
class Cursor(
  @OneToOne
  @JoinColumn(name = "details_id", referencedColumnName = "id")
  var details: Details? = null,

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  @Version
  var version: Long = -1
)
```
{% endraw %}

{% raw %}
```
@Entity
class Details(
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  var name: String = "",
 
  @Version
  var version: Long = -1   
)
```
{% endraw %}

### @OneToOne (@JoinColumn)の設定

イベントやログ、ジョブ等（多対１）の関係、子側のエンティティと同じ。

<dl>
<dt>name</dt>
<dd>ターゲット側エンティティを指定するカーソル側エンティティ上の外部キー</dd>
<dt>referencedColumnName</dt>
<dd>その外部キーに該当するターゲット側エンティティの主キー</dd>
</dl>

## 永続化処理

{% raw %}
```
Details(name = "スナップショット等")
  .also { entityManager.persist(it) }
  .let { Cursor(details = it) }
  .also { entityManager.persist(it) }
```
{% endraw %}

### カーソル側エンティティは子として処理する

ターゲット側のエンティティはmanagedである必要があり、カーソル側のエンティティは子として処理する。

# 任意の関連をもつ（１対０，１）関係

ユーザーについて固定の記事など、任意の関連をもつ関係。関連は関連テーブルにして、存在しない場合も許すものとして。

## モデル

{% raw %}
```
@Entity
class User(
  @OneToOne
  @JoinTable(
    name = "user_fixed_post",
    joinColumns = [JoinColumn(name = "user_id", referencedColumnName = "id")],
    inverseJoinColumns = [JoinColumn(name = "post_id", referencedColumnName = "id")]
  )
  var fixedPost: Post? = null,

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  var name: String = "",

  @Version
  var version: Long = -1
)
```
{% endraw %}

{% raw %}
```
@Entity
class Post(
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  var id: Long = -1,

  var name: String = "",

  @Version
  var version: Long = -1
)
```
{% endraw %}

### @OneToOne (@JoinTable, JoinColumn)の設定

<dl>
<dt>joinColumns</dt>
<dd>ユーザー側エンティティを指定する関連テーブルの外部キー（name）と、ユーザー側エンティティの主キー（referencedColumnName）</dd>
<dt>inverseJoinColumns</dt>
<dd>記事側エンティティを指定する関連テーブルの外部キー（name）と、記事側エンティティの主キー（referencedColumnName）</dd>
</dl>

## 永続化処理

{% raw %}
```
User(name = "ユーザー")
  .apply { fixedPost = entityManager.find(Post::class.java, postId) }
  .also { entityManager.persist(it) }
```
{% endraw %}

### 記事側エンティティは子のようであるがmanaged

伝票・明細、集約等（１対多）の関係のように、記事側エンティティをフィールドにセットしてユーザー側エンティティを保存する。このとき、記事側エンティティはmanagedである必要がある（はず）。

# 参考

- [java - How to use spring Repository without @Id? - Stack Overflow](https://stackoverflow.com/a/29561919)
- [エンティティの状態遷移](http://itdoc.hitachi.co.jp/manuals/link/cosmi_v0870/APKC/EU070301.HTM)
- [@OneToMany](http://itdoc.hitachi.co.jp/manuals/link/cosmi_v0870/APR4/EU260088.HTM)
- [OneToMany (Jakarta EE 仕様 API) - Javadoc](https://spring.pleiades.io/specifications/platform/8/apidocs/javax/persistence/onetomany)
- [OneToManyのリストフィールドの削除・更新の仕方 - Qiita](https://qiita.com/yukihigasi/items/14eac33cc2043fcdbddb)
