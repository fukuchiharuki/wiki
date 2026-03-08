---
title: "Tomcat/WindowsにTomcatをインストールする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 目標
- Tomcatをインストールする
- Tomcatを起動する

# 手順

## Tomcatをダウンロードする
1. 次のサイト左の Download->Tomcat7.0（2011-04-27時点）を選択する
  - http://tomcat.apache.org/
1. 画面中央の Binary Distributions->Core->zip を選択してアーカイブをダウンロードする
1. 適当なディレクトリにアーカイブを展開する
  - ここでは c:\opt\tomcat\apache-tomcat-7.0.12 に展開した

![Tomcatインストール00.JPG]({{ '/images/wiki/546F6D6361742F57696E646F7773E381AB546F6D636174E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_546F6D636174E382A4E383B3E382B9E38388E383BCE383AB30302E4A5047' | relative_url }})

## 環境変数を追加する
1. マイコンピュータの右クリックメニューからプロパティを選択する
1. 詳細設定タブの環境変数を選択する
1. 誰某のユーザー環境変数で新規を選択する
1. 変数名と変数値を次のように設定する
  - 変数名：JAVA_HOME
  - 変数値：C:\Program Files\Java\jdk1.6.0_24

![環境変数00.JPG]({{ '/images/wiki/546F6D6361742F57696E646F7773E381AB546F6D636174E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_E792B0E5A283E5A489E695B030302E4A5047' | relative_url }})

![環境変数01.JPG]({{ '/images/wiki/546F6D6361742F57696E646F7773E381AB546F6D636174E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_E792B0E5A283E5A489E695B030312E4A5047' | relative_url }})

## Tomcatを起動する
1. プロンプトで次のように叩く

```
>cd c:\opt\tomcat\apache-tomcat-7.0.12\
>bin\startup.bat
```

### 動作確認する
別のプロンプトが立ち上がって次のように表示されたらOKです。

```
情報: Server startup in 0000 ms
```

ブラウザからも確認してみましょう。次のURLにアクセスします。

```
http://localhost:8080/
```

猫さんが表示されたらOKです。

# 参考
- http://coffeecupman.blog28.fc2.com/blog-entry-10.html
