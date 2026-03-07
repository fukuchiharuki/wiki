---
title: "障害メモ/Spring Bootがあがらない"
date: 2016-09-04T16:52:39+09:00
last_modified_at: 2016-09-04T16:52:39+09:00
---

# キーワード
- Spring Boot

# 現象

Spring Bootを立ち上げようとしても次の例外が発生して立ち上がらない。

```
Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No bean named 'entityManagerFactory' is defined
```

# 原因

STSから実行すると確認できないが端末でmavenから実行すると次のログを確認できる。

```
mvn clean spring-boot:run
```

```
[WARNING] /Users/haruki/.m2/repository/org/hibernate/hibernate-entitymanager/5.0.9.Final/hibernate-entitymanager-5.0.9.Final.jarの読込みエラーです。invalid LOC header (bad signature)
```

ローカルリポジトリのjarが壊れているということのよう。

# 対策

ここではhibernate一式を削除して再度mavenから実行した。

```
cd /Users/haruki/.m2/repository/org/
mv hibernate hibernate.org
```

```
mvn clean spring-boot:run
```

# 備考

EntityManagerFactoryに関わる設定が足りてないのか？と疑ったのだが全然違ってて、環境の問題だった。なんと[@marking](https://twitter.com/making)さんが見てくれた。ログに原因が出ているという、初歩的なつまずきをしていてとても恥ずかしい。

# 参考
- [Toshiaki Makiさんのツイート: &quot;@fukuchiharuki ソースコードどこかに上げてくれたら見ますよ？&quot;](https://twitter.com/making/status/771651420613337088)
-
