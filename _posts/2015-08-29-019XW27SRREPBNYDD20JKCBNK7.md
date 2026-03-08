---
title: "Alloy/イベントハンドラを取りつける"
date: 2015-08-29T15:27:43+09:00
last_modified_at: 2015-08-29T15:27:43+09:00
---

# キーワード
- Titanium Mobile
- Alloy

# 目標
コントロールにイベントハンドラを取りつけます。

![event01.png]({{ '/images/wiki/416C6C6F792FE382A4E38399E383B3E38388E3838FE383B3E38389E383A9E38292E58F96E3828AE381A4E38191E3828B_6576656E7430312E706E67' | relative_url }})

![event02.png]({{ '/images/wiki/416C6C6F792FE382A4E38399E383B3E38388E3838FE383B3E38389E383A9E38292E58F96E3828AE381A4E38191E3828B_6576656E7430322E706E67' | relative_url }})

# 方法
- index.xml

```
<Label id="label1">I am Window 1</Label>
```

- index.js

```
$.label1.addEventListener('click', function() {
	Ti.UI.createAlertDialog({title:'Click', message:'You clicked it.'}).show();
});
```

# 解説
index.xml のタグ中に onclick 属性を書くこともできるようですが、分離の観点から index.js に書くのがよいでしょう。

index.js 中では id 属性に書いた名前でコントロールを取得できます。(例では $.label1)

# 参考
- [Titanium 3.X - Appcelerator Docs](http://docs.appcelerator.com/titanium/latest/#!/api/Titanium.Proxy-method-addEventListener)
