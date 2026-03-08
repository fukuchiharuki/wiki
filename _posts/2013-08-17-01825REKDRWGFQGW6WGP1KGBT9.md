---
title: "障害メモ/HTML5でrel属性がシンタックスエラーになる"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- HTML5
- rel属性

# 現象
JavaScriptで外部リンクさせるための規約にrelを使っていたらHTML5でシンタックスエラーになった。

{% raw %}
```
<a href="(どこがし)" rel="(なにがし)">外部リンク</a>
```
{% endraw %}

{% raw %}
```
Bad value (なにがし) for attribute rel on element a: Keyword (なにがし) is not registered. 
```
{% endraw %}

# 原因
rel属性には決まったキーワードしか値になれないようで。
- http://www.playstudy.net/blog/develop/html5-linkrel.html

# 対策
独自のデータ属性を使えばいい。

{% raw %}
```
<a href="(どこがし)" data-external="(なにがし)">外部リンク</a>
```
{% endraw %}

「external」の部分は任意。「data-*」の形ならなんでもよさ気。

jQueryでは次のようにして値をとれる。

{% raw %}
```
jQuery('#hoge').data('external');
```
{% endraw %}

# 参考
- http://css-tricks.com/forums/discussion/14733/bad-value-xxx-for-attribute-rel-on-element-a-keyword-xxx-is-not-registered-html5/p1
- http://www.html5.jp/tag/attributes/data.html
