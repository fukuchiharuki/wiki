---
title: "Tomcat/WARファイルを配置する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- Tomcat
- WAR
- デプロイ

# 関連
- [WindowsでWebアプリケーションを作ってみる]({% post_url 2013-08-17-01825REKDRF59BCD8KYSM0CVBA %})

# 概要
TomcatにWARファイル(webアプリケーション)をデプロイします。

## 前提
- Tomcatはインストール済み
- Tomcatは動作確認済み

# WARファイルを配置する
## ディレクトリ構成を確認する
Tomcatをインストールしたディレクトリを /usr/local/tomcat/ とする。

この /usr/local/tomcat/ 下は次の構成になっている。
- /usr/local/tomcat/
  - LICENSE
  - NOTICE
  - RELEASE-NOTES
  - RUNNING.txt
  - bin/
  - conf/
  - lib/
  - logs/
  - temp/
  - webapps/
  - work/

## WARファイルをコピーする
このうち、webapps/ 下に作成したWARファイルをコピーする（WARファイルを作成する方法はここでは述べないが、Eclipseを使っているのであればプロジェクトからエクスポートするのがおそらくは最も簡単。）
- /usr/local/tomcat/
  - webapps/
    - Hoge.war

# 動作確認
## Tomcatを起動する

```
$ /usr/local/tomcat/bin/startup.sh
```

先にコピーしたWARファイルの名前が Hoge.war であれば webapps/ 下に Hoge/ が作成されているはずである。
- /usr/local/tomcat/
  - webapps/
    - Hoge.war
    - Hoge/

## ブラウザで次のURIにアクセスする

```
http://localhost:8080/Hoge/
```

# 参考
- [eclipseでwarファイルを作成。tomcatにdeploy](http://d.hatena.ne.jp/uyaji/20110604/1307140687)
- [Eclipseで.warファイルを作成する](http://www.atmarkit.co.jp/fjava/javatips/043eclipse016.html)
