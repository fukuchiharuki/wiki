---
title: "JavaScript/ページ内リンクをアニメーションでスクロールする"
date: 2018-04-12T19:16:35+09:00
last_modified_at: 2018-04-12T19:16:35+09:00
---

# キーワード
- JavaScript
- hash
- ページ内リンク
- アニメーション

# したいこと

ページ内リンクをアニメーションしてスクロールさせたい。簡単に。

# どうやって

htmlにスクロール先をマーキングして、

```
<a name="pageTop"></a>
```

クリックでリンクするなら普通にアンカーリンク。

```
<a href="#pageTop">page top</a>
```

JavaScriptでリンクするならhashの値を変更。

```
window.location.hash = ""
window.location.hash = "pageTop"
```

cssでscroll-behaviorをsmoothにセットしておくとアニメーションできる。

```
#scroll-container {
  scroll-behavior: smooth;
}
```

# ちなみに

JavaScriptでリンクするときに

```
window.location.hash = ""
```

としているのは、JavaScriptで二度続けて同じページ内リンクをできるようにするため。hash値のリセットがないと二度目にスクロールしてくれない。ただしこれだと履歴が汚れる。が、気にしないならこれで済む。

# 参考
- [window.location - Web API インターフェイス | MDN](https://developer.mozilla.org/ja/docs/Web/API/Window/location)
- [scroll-behavior - CSS: カスケーディングスタイルシート | MDN](https://developer.mozilla.org/ja/docs/Web/CSS/scroll-behavior)
