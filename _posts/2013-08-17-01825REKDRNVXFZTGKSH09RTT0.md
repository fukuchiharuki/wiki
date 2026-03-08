---
title: "障害メモ/IEが旧バージョンモードになる"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- Internet Explore
- HTML
- Servlet/JSP

# 現象
IEがIE7モードでページを表示してしまう。

# 原因
よく分からん。

# 対策
最新のモードで表示するように次のmetaタグを仕込んであげる。

{% raw %}
```
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
```
{% endraw %}

JavaのWebアプリケーションならServletやJSPで次のように書ける。

{% raw %}
```
<% response.addHeader("X-UA-Compatible", "IE=edge,chrome=1"); %>
```
{% endraw %}

# 参考
- http://blog.summerwind.jp/archives/1145
