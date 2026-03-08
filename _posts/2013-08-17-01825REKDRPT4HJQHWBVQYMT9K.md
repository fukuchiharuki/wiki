---
title: "MySQL/接続数を確認する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 手順
MySQLにログイン済みなら

{% raw %}
```
mysql> SHOW STATUS LIKE 'Threads%';
+-------------------+--------+
| Variable_name     | Value  |
+-------------------+--------+
| Threads_cached    | 0      |
| Threads_connected | *      | < ここ
| Threads_created   | *      |
| Threads_running   | *      |
+-------------------+--------+
```
{% endraw %}

MySQLにログインしていないなら

{% raw %}
```
$ mysqladmin -uroot -p extended-status | grep Threads
| Threads_cached                    | 0         |
| Threads_connected                 | *         | < ここ
| Threads_created                   | *         |
| Threads_running                   | *         |
```
{% endraw %}

# 参考

- http://dev.mysql.com/doc/refman/5.1/en/show-status.html
- http://dev.mysql.com/doc/refman/4.1/ja/show-status.html
- http://d.hatena.ne.jp/foosin/20081217/1229515671
