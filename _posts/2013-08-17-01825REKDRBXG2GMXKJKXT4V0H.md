---
title: "障害メモ/phpでmb_strlen()が使えない"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード

- php
- mb_strlen()
- mbstring

# 現象
php で mb_strlen() が使えない。

{% raw %}
```
Fatal error: Call to undefined function mb_strlen() in どこどこ on line どこどこ
```
{% endraw %}

# 原因
php-mbstring のインストールができていない。

# 対策
yum でサクッとインストールする。

{% raw %}
```
# yum install php-mbstring
```
{% endraw %}

# 参考

- [php - Fatal error: Call to undefined function mb_strlen() - Stack Overflow](http://stackoverflow.com/questions/6419102/fatal-error-call-to-undefined-function-mb-strlen)
- [PHP: Installation - Manual](http://www.php.net/manual/en/mbstring.installation.php)
