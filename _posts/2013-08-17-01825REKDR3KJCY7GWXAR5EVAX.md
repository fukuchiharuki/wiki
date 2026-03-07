---
title: "障害メモ/jQueryでチェックボックスをオンにできない"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JavaScript/jQuery
- HTML

# 現象
jQueryにて次のコードでチェックボックスをオンにできない。
```
$('#hoge').attr('checked', 'checked');
```

# 原因
HTMLのチェックボックスタグに名前がないから。

# 対策
HTMLのチェックボックスタグに名前をつけてあげる。
```
<input type="checkbox" name="hoge" id="hoge"></input>
```

# 参考
- (なし)
