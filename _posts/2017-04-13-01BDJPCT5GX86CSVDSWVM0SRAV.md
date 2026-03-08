---
title: "Docker/MySQLサーバーを立てる"
date: 2017-04-13T12:41:02+09:00
last_modified_at: 2017-04-13T12:41:02+09:00
---

# 関連

- [Docker/Dockerで立ち上げたMySQLサーバーに接続する]({{ site.baseurl }}{% post_url 2017-04-13-01BDJPDDPG04FJWDFFDMHDKZS9 %})

# イメージをダウンロード

{% raw %}
```
docker pull mysql
```
{% endraw %}

# コンテナを起動

{% raw %}
```
docker run \
--name mysqld \
-e "TZ=Asia/Tokyo" \
-e MYSQL_ROOT_PASSWORD=rootpassword \
-e MYSQL_DATABASE=mydatabase \
-e MYSQL_USER=mydatabase \
-e MYSQL_PASSWORD=mydatabase \
-p 3306:3306 \
-d mysql
```
{% endraw %}

「-e」で指定の箇所は任意で設定のこと。

## 停止と再起動

停止。

{% raw %}
```
docker stop mysqld
```
{% endraw %}

再起動。

{% raw %}
```
docker start mysqld
```
{% endraw %}

「--name」でつけた名前で停止と再起動ができる。
