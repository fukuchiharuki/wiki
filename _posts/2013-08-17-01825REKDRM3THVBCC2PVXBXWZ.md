---
title: "障害メモ/画像のpreload(先読み)がうまくいかない"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- HTML/JavaScript
- img
- Image

# 現象
次の状況でうまくいかない。
1. XXX_off.png を初期表示
1. XXX_on.png をpreload(先読み)
1. 画像を読み込めない状況にする
1. mouseover で XXX_off.png を XXX_on.png に切り替えて表示
1. mouseout で XXX_on.png を XXX_off.png に切り替えて表示

うまくいかないのは 5. のところ。つまり元の画像に戻すところ。

少なくともIE8ではだめ。

# 原因
JavaScriptで切り替える画像はJavaScriptでpreload(先読み)する必要があるくさい。

参考サイト([画像のプリロード（先読み）](http://lion.zero.ad.jp/inn/js/image/image-preload.html))で「ここでプリロードした画像はJavaScriptで表示させる必要があります。」とあるが、どうやら逆もそうらしい(と思える動作をする、IE8が)。

従って、初期表示している画像をpreload(先読み)しないと mouseout のタイミングで画像が消えていく。

# 対策

初期表示している画像をpreload(先読み)する。
1. XXX_off.png を初期表示
1. XXX_off.png をpreload(先読み) ← ここ
1. XXX_on.png をpreload(先読み)
1. 画像を読み込めない状況にする
1. mouseover で XXX_off.png を XXX_on.png に切り替えて表示
1. mouseout で XXX_on.png を XXX_off.png に切り替えて表示

# 参考
- http://lion.zero.ad.jp/inn/js/image/image-preload.html
