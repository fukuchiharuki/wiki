---
title: "JavaScriptとCSSで言語切り替えする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- HTML
- JavaScript/jQuery
- CSS

# 概要
JavaScriptとCSSで言語切り替えをする方法のメモです(後日きれいにまとめるかも)。

Webアプリケーションのフレームワークが多言語対応しているケースが多いと思いますが、ここではあえてJavaScriptとCSSだけで実現する方法を考えてみます。多言語対応した静的なページをWebサーバで、なんてときに。

# 方法
- index.html

{% raw %}
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<title>多言語対応テスト</title>
		<link rel="stylesheet" type="text/css" href="css/lang.css">
		<noscript>
			<link rel="stylesheet" href="css/noscript.css">
		</noscript>
		<script type="text/javascript" src="js/jquery.js"></script>
		<script type="text/javascript" src="js/multilingual.js"></script>
		<script type="text/javascript">
<!--
jQuery(function() {
	jQuery('#multilingual').multilingual();
});
// -->
		</script>
	</head>
	<body class="ja">
			<div id="multilingual"></div>
			<div id="header">
				<span id="m001-001"></span>
			</div>
			<div id="content">
				<span id="m001-002"></span>
			</div>
			<div id="footer">
				<span id="m001-003"></span>
			</div>
	</body>
</html>
```
{% endraw %}

- css/lang.css

{% raw %}
```
@charset "UTF-8";

body {
	display: none;
}

.ja #m001-001:after {
	content: "日本語ヘッダ";
}

.en #m001-001:after {
	content: "English Header";
}

.ja #m001-002:after {
	content: "日本語コンテント";
}

.en #m001-002:after {
	content: "English Content";
}

.ja #m001-003:after {
	content: "日本語フッタ";
}

.en #m001-003:after {
	content: "English Footer";
}
```
{% endraw %}

- css/noscript.css

{% raw %}
```
@charset "UTF-8";

body {
 	display: block;
}
```
{% endraw %}

- js/multilingual.js

{% raw %}
```
(function() {

	var langs = [
		{lang: 'ja', name: '日本語'},
		{lang: 'en', name: 'English'}
	];

	var setLang = function(lang) {
		if (! lang) {
			lang = langs[0].lang;
		}
		jQuery.each(langs, function() {
			jQuery('body').removeClass(this.lang);
		});
		jQuery('body').addClass(lang);
	};

	jQuery.fn.extend({
		multilingual: function(callback) {
			var target = jQuery('<ul />').appendTo(this);
			jQuery.each(langs, function() {
				jQuery(target).append(
					jQuery('<li />').append(
						jQuery('<a />')
						.attr('rel', this.lang)
						.text(this.name)
						.click(function() {
							var lang = jQuery(this).attr('rel');
							setLang(lang);
							if (callback) {
								callback(lang);
							}
						})
					)
				);
			});
		}
	});

	jQuery(function() {
		setLang(langs[1].lang);
		jQuery('body').css('display', 'block');
	});

})();
```
{% endraw %}

# 解説
- 例では日本語をデフォルトにして全体を非表示(css/lang.css)
  - JavaScript有効の場合言語を設定して全体を表示(js/multilingual.js)
  - JavaScript無効の場合そのまま全体を表示(css/noscript.css)
    - linkをnoscriptでheadの中に書くためhtml5
- ラベルのIDをつけたspanを置く(index.html)
  - :afterで言語ごとのテキストを定義する(css/style.css)
- JavaScriptでbodyに設定する言語のクラスを切り替える(js/multilingual.js)

## IE7以前で:afterが使えない
使えるようにするJavaScriptライブラリがあるようです。

- http://code.google.com/p/ie7-js/
- http://ash.jp/web/css/ie8_js.htm

## meta(X-UA-COmpatible)でエラー
IEを最新のモードで表示させるためのmetaが次の文法エラーになりますが、.htaccessとかでなんとかできるようです。

{% raw %}
```
Bad value X-UA-Compatible for attribute http-equiv on element meta
```
{% endraw %}

- http://www.joshuawinn.com/fix-html5-validator-error-bad-value-x-ua-compatible-for-attribute-http-equiv-on-element-meta/

## 本文がからっぽで検索の対象にできない
あ。(→[その2]({{ site.baseurl }}{% post_url 2013-08-17-01825REKDRPV9V18A0NT8X8DRM %})もどうぞ。)

# 参考
- http://terkel.jp/archives/2012/07/styles-for-noscript/
