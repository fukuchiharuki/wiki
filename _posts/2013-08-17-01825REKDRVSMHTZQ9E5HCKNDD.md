---
title: "fstab/tmpディレクトリにメモリ空間をあてる"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 目的
EeePCを使うにあたってはSSD（Solid State Drive）に優しくすると嬉しいらしいです。
# tmpディレクトリにメモリ空間をあてる
/etc/fstabを次のように編集します。

{% raw %}
```
tmpfs   /tmp    tmpfs   defaults,noatime        0       0
```
{% endraw %}

# 参考

- http://unixlife.jp/unixlife/linux/sys-fstab.jsp
