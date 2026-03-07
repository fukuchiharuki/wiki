---
title: "障害メモ/IE10でjQuery.ajax()するとパラメータがない"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- IE10
- jQuery
- ajax
- 非同期
- postデータ

# 現象
IE10でjQuery.ajax()するとパラメータ(postデータ)が消失している。リクエストは届く。

# 原因
IE10のバグかな？とかっていう噂。

# 対策
IE9モードで動かすという強引な手で解決するらしい(試してない)。

```
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9" >
```

# 参考
- [Why is IE 10 Refusing to send POST data via jQuery $.ajax - Stack Overflow](http://stackoverflow.com/questions/13188500/why-is-ie-10-refusing-to-send-post-data-via-jquery-ajax)
- [Solution to IE10 Ajax Problem  &#8211;   Gishan Code](http://code.gishan.net/code/solution-to-ie10-ajax-problem/)
