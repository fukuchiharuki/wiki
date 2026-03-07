---
title: "障害メモ/Cookieのpathを指定するとIEで食べられない"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JavaScript
- HTML/Cookie

# 現象
pathを指定してCookieを保存するとIEで取得することができない。

- ページのパス

```
/(ContextPath)/Login
```

- 指定したCookieのpath

```
/(ContextPath)/Login
```

# 原因
IEはCookieのpathをディレクトリとしてだけ扱うことによるっぽい。

指定するCookieのpathが

```
/(ContextPath)/Login
```

ならば、次のパスをもつページでそのCookieを取得することができる。

```
/(ContextPath)/Login/Hoge
```

# 対策
pathにページのパスから1階層分上のパスを指定する。

# 参考
- http://hamalog.tumblr.com/post/18542555704/ie-cookie-path-hoge-foo-html
- http://www.synck.com/blogs/technote/technote_1230518860.html
