---
title: "シェル/スペース区切りを分割する"
date: 2018-09-22T14:22:10+09:00
last_modified_at: 2018-09-22T14:22:10+09:00
---

# キーワード

- set
- shift

# 概要
スペース区切りの文字列を分割します。

# 方法
sample.sh: 

{% raw %}
```
set -- `echo i1 i2 i3`
while [ $# -ne 0 ]
do
    echo $1
    shift
done
```
{% endraw %}

次の実行結果を得ます。

{% raw %}
```
$ ./sample.sh
i1
i2
i3
$
```
{% endraw %}

# 解説
$1 や shift は引数を扱うためのものですが set を使うことで引数の代わりにすることができます。

# 参考

- [bourne shellのTips - web-cahier.com](http://www.web-cahier.com/log/2012/01/bourne-shelltips.html)
