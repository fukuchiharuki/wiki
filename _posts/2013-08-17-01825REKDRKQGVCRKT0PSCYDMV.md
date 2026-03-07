---
title: "JavaScript/正規表現で特定箇所をいくつか抜き出す"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JavaScript
- 正規表現

# 概要
正規表現で特定箇所をいくつか抜き出したい。

# 方法

```
var text = "1984-03-12";
var regexp = new RegExp("^([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])$");
var matcher = text.match(regexp);
if (matcher) {
  year = RegExp.$1; // "1984"
  month = RegExp.$2; // "03"
  day = RegExp.$3; // "12"
}
```

# 解説
RegExpクラスを使用すると特定箇所を抜き出すことができます。

# 参考
- http://www.tohoho-web.com/js/regexp.htm
