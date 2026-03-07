---
title: "jQuery/jQueryオブジェクトの条件を調べる"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JavaScript
- jQuery

# 概要
class属性やid属性からjQueryオブジェクトを引いたとき、そのオブジェクトが何者であるか調べたい。

# 方法

```
if ($(this).is('input')) {
  $(this).val('ほげ');
} else {
  $(this).html('ほげ');
}
```

# 解説
jQueryオブジェクトのis()メソッドにセレクタを渡すことでそのセレクタにマッチするかどうかを調べることができます。

# 参考
- 
-
