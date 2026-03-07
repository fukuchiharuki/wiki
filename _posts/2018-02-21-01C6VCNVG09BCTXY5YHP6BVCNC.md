---
title: "Spring Boot/authoritiesに応じて処理をガードする"
date: 2018-02-21T14:16:48+09:00
last_modified_at: 2018-02-21T14:16:48+09:00
---

# キーワード
- Spring Boot
- Spring Security
- PreAuthorize

# したいこと

ロール（roles）に紐づける権限（authorities）に応じて、特定の処理をガードしたい。権限があるユーザーだけが処理できるように。

# どうやって

URLを拾ってガードすることもできるようだけど、権限の分だけURLの名前をつけ分けることは難しいので、サービスのメソッドにガードをかけるようにする。

- Some情報を追加するメソッドを
- ADD_SOME_DATA権限をもつユーザーだけ実行できる

ようにする。

```
@PreAuthorize("hasAuthority('ADD_SOME_DATA')")
@Transactional(readOnly = false)
fun add(someData: SomeData) {
  /* ガードがかかる追加処理 */
}
```

文字列で設定するのが少し気持ち悪い。開発初期の段階で、権限の名称を変えるときなんかに注意。

# ちなみに

## 有効化

@PreAuthorizeによる権限チェックをするにはSecurityConfigで次の設定をする必要がある。

```
@EnableGlobalMethodSecurity(prePostEnabled = true) // <-- これ
@Configration
class SecurityConfig: WebSecurityConfigurerAdapter {
  ...
```

## 範囲

@PreAuthorizeをクラスにつければどのメソッドでも権限チェックできる。

# 参考
- [java - Spring security - @PreAuthorize not working - Stack Overflow](https://stackoverflow.com/questions/29643183/spring-security-preauthorize-not-working)
