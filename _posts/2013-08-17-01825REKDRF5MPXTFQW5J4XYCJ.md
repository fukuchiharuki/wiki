---
title: "JavaScript/とりあえずajaxしてみる"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JavaScript
- jQuery
- ajax

# 概要
ajaxの枠組みがないフレームワーク等の環境でとりあえずajaxさせたいときのTips。

- 前提条件が次のような感じだとして
  - ajaxする仕組みが特別ない
  - ページを出力する枠組みしかない
  - jQueryが使える

# 方法

- ページをふたつ作る
  - ajaxしたいページ
  - 動的に切り替わる要素を書いたページ(別ページ)
- ajaxしたいページから別ページを呼ぶ
  - $.ajax()を使う(jQeury)
- ajaxしたいページの要素を書き換える
  - 別ページの要素を選択して
  - ajaxしたいページに入れ込む

{% raw %}
```
var formData = $(フォームのセレクタ).serializeArray();
$.ajax({
	type: 'POST',
	url: 別ページのURL,
	data: formData,
	dataType: 'html',
	cache: false,
	success: function(html) {
		var div = $(html).filter(抜き出したい要素のセレクタ);
		// 正常時
		if ($(div).size() > 0) {
			$(入れ込みたい要素のセレクタ).html($(div).html());
		}
		// エラー時（抜き出したい要素が拾えないとき）
		else {
			alert('ダメでした。');
		}
	},
	// エラー時（通信的エラーのとき）
	error: function(XMLHttpRequest, textStatus, errorThrown) {
		alert('ダメでした。');
	}
});
```
{% endraw %}

# 解説

{% raw %}
```
$(フォームのセレクタ).serializeArray()
```
{% endraw %}

JSON形式のデータ構造を取得する。

{% raw %}
```
$.ajax({
	・
	・
	・
  success: function(){},
    error: function(){}
});
```
{% endraw %}

ajaxして成功時、失敗時の関数をそれぞれ実行する。

{% raw %}
```
$(html).filter(抜き出したい要素のセレクタ);
```
{% endraw %}

読み込んだページから要素を選択する。

# 参考
- http://semooh.jp/jquery/api/ajax/serializeArray/+/
- http://semooh.jp/jquery/api/ajax/jQuery.ajax/options/
- http://semooh.jp/jquery/api/traversing/filter/expr/
