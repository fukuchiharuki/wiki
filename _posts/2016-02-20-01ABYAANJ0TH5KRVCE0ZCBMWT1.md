---
title: "Git/GitHubと連携する"
date: 2016-02-20T12:07:20+09:00
last_modified_at: 2016-02-20T12:07:20+09:00
---

# 関連
- Git
- GitHub

# 概要
GitHub（リモート）と連携するためのメモ。

# セッティング

## ユーザー情報を設定する

```
$ git config --global user.name "<アカウント名>"
$ git config --global user.email "<メールアドレス>"
```

# スタートアップ

## gitを初期化する

```
$ cd <プロジェクトのディレクトリ>
$ git init
```

## コミットする

```
$ git add *
$ git commit -m "first commit"
```

## プッシュする

```
$ git remote add origin git@github.com:<username>/<Project>.git
$ git push -u origin master
```

次回からは省略することができる。

```
$ git push
```

# タグ
## タグをつける

```
$ git tag -a tagname -m "message"
$ git push --tag
```

tagnameとmessageは適宜。

## タグを削除する

```
$ git tag -d tagname
$ git push origin :tagname
```

# 参考
- http://help.github.com/create-a-repo/
- http://kakakikikeke.blogspot.jp/2012/05/githubeclipsegithub.html
- http://at-aka.blogspot.jp/2010/06/git.html
