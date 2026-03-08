---
title: "障害メモ/MySQLがあがらない「The server quit without updating PID file」"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- MySQL
- InnoDB
- buffer pool

# 関連
- [障害メモ/MySQL関連]({{ site.baseurl }}{% post_url 2013-08-17-01825REKDRNWW3CSW9J45BYEPF %})

# 現象
mysqldが立ちあがらない。

{% raw %}
```
Starting MySQL..The server quit without updating PID file(***.pid).
```
{% endraw %}

# 原因
コマンド実行時のメッセージは罠。pidが作れないとかそんなことではない。

ログを見ます。
- mysql-error.log (設定にもよるが /etc/log/ あたりかと)

{% raw %}
```
130703  0:16:23 InnoDB: The InnoDB memory heap is disabled
130703  0:16:23 InnoDB: Mutexes and rw_locks use GCC atomic builtins
130703  0:16:23 InnoDB: Compressed tables use zlib 1.2.3
130703  0:16:23 InnoDB: Initializing buffer pool, size = 4.0G
InnoDB: mmap(4395630592 bytes) failed; errno 12
130703  0:16:23 InnoDB: Completed initialization of buffer pool
130703  0:16:23 InnoDB: Fatal error: cannot allocate memory for the buffer pool
130703  0:16:23 [ERROR] Plugin 'InnoDB' init function returned error.
130703  0:16:23 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
130703  0:16:23 [ERROR] Unknown/unsupported storage engine: InnoDB
130703  0:16:23 [ERROR] Aborting
```
{% endraw %}

メモリサイズ指定が大きすぎて buffer pool の初期化ができなかったということらしい。

&color(red){*※今回はこうだった、というだけで別の ERROR もあり得ますよ！*};

# 対策
メモリサイズ指定を小さくします。

- /etc/my.cnf

{% raw %}
```
#innodb_buffer_pool_size = 4096M
innodb_buffer_pool_size = 1024M
```
{% endraw %}

# 参考
- [MySQLのメモリ関係](http://m97087yh.seesaa.net/archives/20090107-1.html)
