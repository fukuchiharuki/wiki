---
title: "設計パターン/ビルダー"
date: 2014-05-27T09:47:50+09:00
last_modified_at: 2014-05-27T09:47:50+09:00
---

# キーワード
- インスタンス
  - 生成
    - パラメータ

# 何か

```
組み立て屋さん
```

インスタンスを生成するために必要なパラメータをもつビルダークラスを別途設けます。このビルダークラスのオブジェクトはパラメータ(ビルダーの属性)を使用することで対象のインスタンスを生成して完全な状態にします。

Effective JavaでいうところのビルダーパターンとGoFが提唱するビルダーパータンは別のものです。ここでは前者を挙げています。

後者の特徴はDirectorがインスタンス生成のための手順をもっていることです。単に複数のパラメータが必要であるということだけではない手順です。調理法が定まっていて食材を変えることができるイメージです。

# なぜか

引数が多すぎるとコードの見通しが悪くなります。コンストラクタについても同じことが言えます。ビルダーにインスタンスの生成責務を預けることでコンストラクタの引数が多くなり過ぎる問題を解決できます。また、インスタンスを生成するためのインタフェースを特定しませんから、ビルダーがパラメータに応じて柔軟にインスタンスの生成パターンを変更することができます。

- コンストラクタの過剰なパラメータ数を回避
- クライアント側から生成パターンを特定しない

デフォルトコンストラクタでインスタンスを生成して属性を後からセットする手段もあります。JavaBeansパターンです。この方法ではクライアントが注意深くインスタンスを生成しなければなりません。対象のオブジェクトがメソッド実行の際に完全な状態であることを自身でチェックすることはできます。しかし対象のクラスの責務が大きくなり過ぎて見通しが悪くなります。本来のドメインモデルにおける債務に集中できなくなってしまいます。

- 責務(: 完全な状態であることのチェック)を分離

# どのように

たとえば、Userクラスのインスタンスを生成するためのUser.Builderクラスを設けます。

```
User {

  Builder {

    // required
    private name;

    // optional
    private gender;

    public Builder(name) {
      this.name = name;
    }

    public setGender(gender) {
      this.gender = gender;
      return this;
    }

    public build() {
      /*
       * ここでパラメータの整合性チェックをする
       * (チェックエラーの場合IllegalArgumentExceptionを投げるなど)
       */
      User user = new User();
      user.name = this.name;
      user.gender = this.gender;
      return user;
    }

  }

  private name, gender;
  private User(){}

}
```

クライアントはUser.Builderを使ってUserクラスのインスタンスを得ます。

```
Client {
  do() {

    User user = new User.Builder("fukuchi").setGender("male").build();

  }
}
```

# 関連
- [設計パターン/スタティックファクトリメソッド]({{ site.baseurl }}{% post_url 2014-05-26-018RVBGNP839YZFXNFXCAFWDQM %})
- [設計パターン/ファクトリ]({{ site.baseurl }}{% post_url 2014-05-26-018RVBJ2KRC9HNNNFH3HT0RZZT %})

# 参考
- Effective Javaのビルダーパターン
  - [Item 2: Consider a builder when faced with many constructor parameters \| Creating and Destroying Java Objects \| InformIT](http://www.informit.com/articles/article.aspx?p=1216151&seqNum=2)
  - [Builderパターンについて考えてみる。 - 感謝のプログラミング 10000時間](http://programming-10000.hatenadiary.jp/entry/20130814/1376497461)
- GoFが提唱するビルダーパターン
  - [7. Builder パターン \| TECHSCORE(テックスコア)](http://www.techscore.com/tech/DesignPattern/Builder.html/)
  - [Builder - Strategic Choice](http://d.hatena.ne.jp/asakichy/20090306/1236344710)
