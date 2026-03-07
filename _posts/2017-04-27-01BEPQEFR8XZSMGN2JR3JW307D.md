---
title: "Spring Boot/実行環境ごとにログファイルの出力先を変える"
date: 2017-04-27T12:32:05+09:00
last_modified_at: 2017-04-27T12:32:05+09:00
---

# キーワード
- Spring Boot
- logback

# したいこと

実行環境ごと(本番、ステージング、開発)にログファイルの出力先を変えたい。

|環境|ログファイル|h
|本番|/home/hoge/log/application.log|
|ステージング|/home/hogestg/log/stg.application.log|
|開発|/home/hogedev/log/dev.application.log|
など。

せっかく同じ構成の環境を用意するのにディレクトリ名を変えなくてもよくないかな。と思ったりもするけど、なぜかそう求められたりすることは多い。

# どうやって

logback-spring.xmlで次のように設定する。

```
<springProfile name="prod">
	<property name="WEB_FILE_NAME" value="/home/hoge/log/application.log" />	
</springProfile>
<springProfile name="stg">
	<property name="WEB_FILE_NAME" value="/home/hogestg/log/stg.application.log" />	
</springProfile>
<springProfile name="dev">
	<property name="WEB_FILE_NAME" value="/home/hogedev/log/dev.application.log" />	
</springProfile>
```

ファイル名の指定で次のように書く。

```
<file>${WEB_FILE_NAME}</file>
```

# ノート

logback-spring.xmlにするとSpringのプロフィールが使えるのですね。

# 参考
- [Spring Boot解説第10回(開発環境編：ログの設定について～logback) - Qiita](http://qiita.com/TEBASAKI/items/bdbecdb22249913d6b67)
