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

{% raw %}
```
$('#hoge').attr('checked', 'checked');
```
{% endraw %}

# 原因
HTMLのチェックボックスタグに名前がないから。

# 対策
HTMLのチェックボックスタグに名前をつけてあげる。

{% raw %}
```
<input type="checkbox" name="hoge" id="hoge"></input>
```
{% endraw %}

# 参考

- (なし)
