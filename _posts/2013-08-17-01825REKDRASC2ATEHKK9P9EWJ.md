---
title: "JSTL/一文字ずつsplitする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JSP
- JSTL

# 概要
JSPで一文字ずつsplitする方法です。
ついでに&amp;shy;を挟みます。

# 方法

```
<c:set var="text" value="${longtext}" />
<c:forEach var="str" items="<%=((String)pageContext.getAttribute(\"text\")).toCharArray() %>" ><c:out value="${str}" />&shy;</c:forEach>
```

# 解説
各ブラウザで折り返しがどうのとかいう、見栄えが優先されるときに。
逆にそうでなければ一文字ずつ処理するとその文字列が情報でなくなる恐れもあります。
ので、お勧めはしないです。
