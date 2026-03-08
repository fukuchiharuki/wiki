---
title: "Docker/Dockerで立ち上げたMySQLサーバーに接続する"
date: 2017-04-13T12:41:22+09:00
last_modified_at: 2017-04-13T12:41:22+09:00
---

# キーワード
- Docker
- MySQL

# 関連
- [Docker/MySQLサーバーを立てる]({{ site.baseurl }}{% post_url 2017-04-13-01BDJPCT5GX86CSVDSWVM0SRAV %})
- [障害メモ/Docker for Windowsでボリュームマウントできない]({{ site.baseurl }}{% post_url 2017-04-13-01BDJPB1H0Q89Z9F8Y5MRVMK66 %})

# したいこと

Dockerで立ち上げたMySQLに別のコンテナから接続したい。

背景としては、データ移行するためのスクリプトの実行を試したいため。Dockerで立ち上げたMySQLコンテナに直接という手もあるけど、これはこれで触らずにおいておきたい。

# どうやって

リンクして接続する。

Dockerで立ち上げたMySQLコンテナの名前が『mysqld』であるとして。

{% raw %}
```
$ docker run -it --rm --link mysqld:dbserver mysql bash
```
{% endraw %}

MySQLのイメージにはmysqlクライアントもbashもある。

{% raw %}
```
# env | grep DBSERVER
DBSERVER_PORT_3306_TCP_ADDR=172.17.0.2
DBSERVER_ENV_MYSQL_USER=mydb
DBSERVER_ENV_MYSQL_PASSWORD=mydb
DBSERVER_PORT=tcp://172.17.0.2:3306
DBSERVER_ENV_MYSQL_VERSION=5.7.17-1debian8
DBSERVER_PORT_3306_TCP_PROTO=tcp
DBSERVER_PORT_3306_TCP_PORT=3306
DBSERVER_ENV_MYSQL_ROOT_PASSWORD=rootpw
DBSERVER_NAME=/heuristic_wozniak/dbserver
DBSERVER_ENV_TZ=Asia/Tokyo
DBSERVER_ENV_MYSQL_DATABASE=MYDB
DBSERVER_PORT_3306_TCP=tcp://172.17.0.2:3306
DBSERVER_ENV_MYSQL_MAJOR=5.7
DBSERVER_ENV_GOSU_VERSION=1.7
#
```
{% endraw %}

{% raw %}
```
# mysql -h$DBSERVER_PORT_3306_TCP_ADDR -u$DBSERVER_ENV_MYSQL_USER -p$DBSERVER_ENV_MYSQL_PASSWORD $DBSERVER_ENV_MYSQL_DATABASE
```
{% endraw %}

# ノート

後で立ち上げるコンテナでボリュームのマウントをすればスクリプトを試験できそう。

# 参考
- [Docker の基本学習 ~ コンテナ間のリンク - Qiita](http://qiita.com/Arturias/items/75828479c1f9eb8d43fa)
