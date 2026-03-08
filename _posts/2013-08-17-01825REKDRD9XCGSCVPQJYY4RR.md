---
title: "MySQL/ファイルをインポート・エクスポートする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連

- MySQL

# 概要
タブ区切りのデータをインポートしたりエクスポートしたりします。
## 制限事項
各カラム値に改行はないものとして

# 方法
## インポート

{% raw %}
```
$ mysql --local-infile=1 -u ${user} -p${passwd} ${database} -e "LOAD DATA LOCAL INFILE '${file}' REPLACE INTO TABLE ${table} FIELDS TERMINATED BY '\t'
```
{% endraw %}

## エクスポート

{% raw %}
```
$ mysql -u ${user} -p${passwd} ${database} -e "SELECT * FROM ${table} INTO OUTFILE '${file}' FIELDS TERMINATED BY '\t'
```
{% endraw %}

# 解説
LOAD DATA LOCALする場合、環境によってはオプション「--local-infile=1」が必要です。

SELECT INTO OUTFILEするユーザーはmysqldを動かしているユーザーです。/tmp/下にファイル指定する必要があるかもしれません。

# 参考

- http://oshiete.goo.ne.jp/qa/1030943.html
- http://q.hatena.ne.jp/1159437279
