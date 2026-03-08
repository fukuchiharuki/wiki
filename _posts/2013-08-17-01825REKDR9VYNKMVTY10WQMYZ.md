---
title: "MySQL/ユーザーを作成する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード

- MySQL
- grant

# 関連

- [MySQL/データベースを作成する]({{ site.baseurl }}{% post_url 2013-08-17-01825REKDRZKVFR2RWTH543RHB %})

# 概要
ユーザを作成する。

# 方法

{% raw %}
```
mysql> GRANT ALL PRIVILEGES ON データベース名.* TO 'ユーザー名'@'ホスト名' IDENTIFIED BY 'パスワード';
mysql> flush privileges;
```
{% endraw %}

# 解説

- 「ALL PRIVILEGES」はfull権限を与える場合の設定
- どのホストからでも接続できるようにするには「'ユーザー名'@'%'」にする
  - 「'ユーザー名'@'localhost'」も忘れずに ← めんどくさいね

# 参考

- http://dev.mysql.com/doc/refman/5.1/ja/grant.html
