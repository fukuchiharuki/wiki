---
title: "SVN/WindowsにSVNサーバをインストールする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 目標
- WindowsにてSVNサーバを起動する

# 手順

## パッケージをダウンロードする
1. 以下のサイトの Getting Subversion->Binary Packages を選択する
  - http://subversion.apache.org/
1. Windows から Win32Svn を選択する
1. Download をクリックしてmsiファイルをダウンロードする
  - Setup-Subversion-1.6.16.msi（2011-04-27時点）

## パッケージをインストールする
1. ダウンロードしたmsiファイルを実行する
1. Next、Install、Finishをクリックしていく

![svnインストール00.JPG]({{ '/images/wiki/53564E2F57696E646F7773E381AB53564EE382B5E383BCE38390E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_73766EE382A4E383B3E382B9E38388E383BCE383AB30302E4A5047' | relative_url }})

![svnインストール01.JPG]({{ '/images/wiki/53564E2F57696E646F7773E381AB53564EE382B5E383BCE38390E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_73766EE382A4E383B3E382B9E38388E383BCE383AB30312E4A5047' | relative_url }})

![svnインストール02.JPG]({{ '/images/wiki/53564E2F57696E646F7773E381AB53564EE382B5E383BCE38390E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_73766EE382A4E383B3E382B9E38388E383BCE383AB30322E4A5047' | relative_url }})

![svnインストール03.JPG]({{ '/images/wiki/53564E2F57696E646F7773E381AB53564EE382B5E383BCE38390E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_73766EE382A4E383B3E382B9E38388E383BCE383AB30332E4A5047' | relative_url }})

![svnインストール04.JPG]({{ '/images/wiki/53564E2F57696E646F7773E381AB53564EE382B5E383BCE38390E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_73766EE382A4E383B3E382B9E38388E383BCE383AB30342E4A5047' | relative_url }})

![svnインストール05.JPG]({{ '/images/wiki/53564E2F57696E646F7773E381AB53564EE382B5E383BCE38390E38292E382A4E383B3E382B9E38388E383BCE383ABE38199E3828B_73766EE382A4E383B3E382B9E38388E383BCE383AB30352E4A5047' | relative_url }})

## リポジトリを作成する

### リポジトリ用のディレクトリを作成する
svnがリポジトリ管理するためのディレクトリを作成します。

```
>mkdir c:\var
>mkdir c:\var\svn
>mkdir c:\var\svn\documents
```

ここでは次のようなディレクトリの役割を考えています。

<dl>
<dt>var</dt>
<dd>Unix系OSの慣習として</dd>
<dt>svn</dt>
<dd>snvが管理する場所として（一箇所にしたい）</dd>
<dt>documents</dt>
<dd>ドキュメントのリポジトリ用として（カテゴリで分けたい）</dd>
</dl>

### リポジトリを作成する

```
>svnadmin create c:\var\svn\documents
```

### リポジトリを設定する

- c:\var\svn\documents\conf\svnserve.conf

```
anon-access = none
auth-access = write
password-db = passwd
```

上記はそれぞれ次のアクセスを設定します。

<dl>
<dt>anon-access</dt>
<dd>匿名アクセス→none（なし）</dd>
<dt>auth-access</dt>
<dd>認証アクセス→wirte（読み書き）</dd>
<dt>password-db</dt>
<dd>パスワードファイル→passwd（ファイル名）</dd>
</dl>

- c:\var\svn\documents\conf\passwd

```
ユーザ名=パスワード
```

## サーバを起動する
### デーモンモードで実行する

```
>start svnserve -d -r c:\var\svn
```

ここでオプションは次の意味があります。

<dl>
<dt>-d</dt>
<dd>デーモンモードで実行する（デフォルト 3690 番ポートで受け付ける）</dd>
<dt>-r</dt>
<dd>仮想ルートを設定する（上位ディレクトリにアクセスさせない）</dd>
</dl>

さすがにプロンプトから毎度実行するのはしんどいので、サービスと立ち上げるように別途設定するのがよろしいかと思います。

### 基本ディレクトリ構成を作成する

```
>svn mkdir svn://localhost/documents/trunk -m "create"
>svn mkdir svn://localhost/documents/branches -m "create"
>svn mkdir svn://localhost/documents/tags -m "create"
```

SVNでは慣習として次のようなディレクトリ構成をとります。

<dl>
<dt>trunk</dt>
<dd>開発中の最新バージョン</dd>
<dt>branches</dt>
<dd>版（保守対象）</dd>
<dt>tags</dt>
<dd>リリース（保存用）</dd>
</dl>

このとき、一度ログインユーザのアカウント名でパスワードを聞かれますがEnterを押してスルーします。次にユーザ名とパスワードをそれぞれ聞いてきますで先に設定したユーザ名とパスワードを入力します。

# 参考
- http://www.hyuki.com/techinfo/svninit.html
- http://www.caldron.jp/~nabetaro/svn/svnbook-1.4-final/svn.ref.svnserve.html
- http://www.atmarkit.co.jp/fjava/rensai4/devtool02/devtool02_3.html
