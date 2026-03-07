---
title: "はじめてのAngular2/Hello Worldと環境構築"
date: 2016-07-04T17:43:48+09:00
last_modified_at: 2016-07-04T17:43:48+09:00
---

今どきのJavaScriptはコンパイルして実行したり、パッケージ管理があったり、ブラックボックスがどんどん増えていって怖いですね！と逃げてばっかりもいられないのでまずは "Hello World" からです。

# npmをインストールする

node.js？？サーバーサイドじゃなくてクライアントサイドがやりたいのですが。。知ってます！ライブラリ・パッケージ管理のためにnpmが要ります。何かをするために手前の環境にnpmが入っていたのですが、途中でうまくいかないことが起きたのでnodebrewで入れなおしました。

そこで参考にした記事はこちら。

- [Macにnodebrew（node.js, npm）をインストールする手順 - Qiita](http://qiita.com/oreo3@github/items/622fd6a09d5c1593fee4)

# Hello Worldする

&color(red){-- オフィシャルのQickstartを[やり直すことに](../再びHello World.md)しました。};

次の記事のとおりに従えばまずはAngular2が動くのを確認できます。

- [Angular2 for TypeScript - 5 MIN QUICKSTARTの日本語訳だよ。 | Yuhiisk](http://blog.yuhiisk.com/archive/2015/12/05/angular2-quickstart-typescript-japanese.html)

最終的に次のようにファイルができあがります。

```
アプリケーションルート
├── node_modules
├── package.json
└── src
    ├── app
    │   └── app.ts
    ├── index.html
    └── tsconfig.json
```

## 初期設定する

アプリケーションをコンパイルしたり実行したりできるように、npmの設定をします。手動で書くこともあるようなので注意（参考記事のとおりでいけます）。

```
cd アプリケーションルート
npm init -y
npm i angular2@2.0.0-alpha.44 systemjs@0.19.2 --save --save-exact
npm i typescript live-server --save-dev
```

## コンパイルする

コンパイル？JavaScriptはコンパイルなしで動くのでは？そう、だけどTypeScriptで書いたからJavaScriptにコンパイルする必要があります。TypeScriptからJavaScriptへのコンパイルはすごい。TypeScriptのコードを更新した瞬間JavaScriptにコンパイルします。

```
cd アプリケーションルート
npm run tsc
```

## 実行する

live-serverでローカルのhttpdを立ち上げてブラウザで動作確認します。このlive-serverもすごい。TypeScriptからJavaScriptにコンパイルした瞬間何かをしてブラウザをリロードさせます。つまり、TypeScriptのコードを更新すればブラウザで動作確認できていることになります。

```
cd アプリケーションルート
npm start
```

# ソースコード

- https://github.com/fukuchiharuki/til/tree/master/javascript/angular2/angular2-quickstart
