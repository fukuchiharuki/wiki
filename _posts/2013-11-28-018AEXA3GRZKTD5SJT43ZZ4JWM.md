---
title: "JavaScript/テキストの選択を抑止する"
date: 2013-11-28T17:30:55+09:00
last_modified_at: 2013-11-28T17:30:55+09:00
---

# キーワード
- JavaScript
- jQuery

# 概要
右クリックやテキストの選択を抑止したいというユーザーからの要望を抑えられなかったときのメモです。

# 方法
## 右クリック禁止

{% raw %}
```
$(document).bind("contextmenu", function(e) {
	return false;
});
```
{% endraw %}

## テキストの選択禁止
### IE向け

{% raw %}
```
$('html').on('selectstart dragstart', function(e) { 
	e.preventDefault(); 
});
```
{% endraw %}

### IE以外向け

{% raw %}
```
$('html').css({
	'user-select': 'none',
	'-moz-user-select': 'none',
	'-khtml-user-select': 'none',
	'-webkit-user-select': 'none'
});
```
{% endraw %}

# 解説
右クリックはイベント contextmenu を拾って false を返却すれば抑止できるようです。

テキストの選択は IE とそれ以外で別の方法を採ります。IE ではイベント selectstart と dragstart を拾ってそのイベントをキャンセルすることで抑止できるようです。また IE 以外のブラウザではスタイルの指定で抑止できるようです。

# 参考
- [jQueryを使って右クリックメニューを禁止する方法 \| IDEA*IDEA](http://www.ideaxidea.com/archives/2009/03/how_to_disable_right_click_menu.html)
- [ドラッグによるテキストの選択をキャンセルする【CSS, HTML, JavaScript】 - Programming Magic](http://www.programming-magic.com/20071217225449/)
