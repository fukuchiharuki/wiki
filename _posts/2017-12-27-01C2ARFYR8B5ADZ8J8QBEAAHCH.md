---
title: "Git/rebaseする"
date: 2017-12-27T10:13:25+09:00
last_modified_at: 2017-12-27T10:13:25+09:00
---

# キーワード
- Git
- fetch
- rebase
- pull
- merge

# したいこと

git pullしちゃうとマージコミットされてきもちわるいのでrebaseしたい。

けど、コミットしてない変更があると怒られる。

```
$ git rebase
Cannot rebase: You have unstaged changes.
Please commit or stash them.
```

Eclipseで操作するでもいいけど、環境が変わると対処できなくなるのは困るのでコマンドで操作したい。

# どうやって

```
$ git fetch
$ git rebase
```

ここで怒られるので、コミットしてない変更を退避してからrebaseする。

```
$ git stash save
$ git rebase
```

退避した変更を適用する。

```
$ git stash pop
```

# ノート

## メッセージ
退避するときにメッセージをつけられる。

```
$ git stash save "メッセージ"
```

## 一覧
退避した変更を確認することができる。

```
$ git stash list
stash@{0}: WIP on master: 554699c refactor: 分かりづらいメソッド名をrename
```

## 適用
いくつか退避した場合、退避した変更を指定することができる。
```
$ git stash pop stash@{N}
```

退避した変更を適用したときに、これを消さないでおくことができる。
```
$ git stash apply stash@{N}
```

退避した変更を適用せずに、これを消すことができる。
```
$ git stash drop stash@{N}
```

# 参考
- [色々な git stash - Qiita](http://qiita.com/akasakas/items/768c0b563b96f8a9be9d)
- [変更を一時的に退避！キメろgit stash - Qiita](http://qiita.com/fukajun/items/41288806e4733cb9c342)
