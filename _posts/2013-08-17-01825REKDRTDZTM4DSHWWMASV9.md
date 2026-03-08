---
title: "障害メモ/sshからログアウトするとmysqldが停止する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- nohup
- ssh
- MySQL

# 現象
mysqld をコンソールから立ち上げて ssh からログアウトすると、mysqld が停止する。

# 原因
ユーザがシェルからログアウトすると、シェルが端末から起動したプロセスに向けて SIGHUP シグナルを発信するため。プロセス（mysqld）は SIGHUP シグナルを受けて終了する。

# 対策
次のようにしてプロセスを実行すると、プロセスはSIGHUPシグナルを無視する。

```
$ nohup mysqld [options] &
```

## バックグラウンド処理は nohup の機能ではない
なにかの都合で fg(フォアグラウンド) したときは bg(バックグラウンド) することを忘れずに。

```
$ fg
(Ctrl + z)
$ bg
```

# 参考
- http://dev.mysql.com/doc/refman/4.1/ja/alpha-dec-unix.html
- http://www.atmarkit.co.jp/flinux/rensai/linuxtips/352nostopprog.html
- http://www.glamenv-septzen.net/view/854
