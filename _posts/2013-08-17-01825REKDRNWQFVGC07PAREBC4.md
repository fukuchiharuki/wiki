---
title: "シェル/標準入力から一行ずつ処理する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連

- sh
- awk

# 概要
次のように実行するときにファイルを一行ずつ処理したい。

{% raw %}
```
./test.sh < file.txt
```
{% endraw %}

# 方法
こう書きます。

{% raw %}
```
#!/bin/sh

while read LINE
do
    # ここに $LINE を使った処理
done
```
{% endraw %}

# 解説
一行ずつ処理をするなら

{% raw %}
```
awk '{print $1+1}' < /dev/stdin
```
{% endraw %}

した方がいいよ、という見方もあるようです。詳しくは参考サイトをご覧になってください。

# 参考

- http://shellscript.sunone.me/input_output.html
- http://www.usptomonokai.jp/TOMONOKAI_CMS/CGI/TOMONOKAI_CMS.CGI?PAGE=20120212
