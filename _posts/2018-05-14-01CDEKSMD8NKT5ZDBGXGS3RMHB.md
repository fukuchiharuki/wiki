---
title: "React/子コンポーネントのフィールドから値を取得する"
date: 2018-05-14T15:00:57+09:00
last_modified_at: 2018-05-14T15:00:57+09:00
---

# キーワード

- React
- コンポーネント
- react-new-window

# したいこと

react-new-window で開いた別ウィンドウを印刷させたい、のがきっかけ。

{% raw %}
```
window.print();
```
{% endraw %}

すると、親ウィンドウが印刷されてしまう。

ので、react-new-window がそのコンポーネントで保持する this.window の値を取得したい。react-new-window は window.open() したときの戻り値を this.window に保持している。

# どうやって

ref を使う。

{% raw %}
```
<NewWindow {...newWindowProps} ref={element => this.newWindow = element} />
```
{% endraw %}

目的の window オブジェクトでプリントするには、

{% raw %}
```
this.newWindow.window.print();
```
{% endraw %}

# なお書き

%%element がないよ、みたいなタイミングがあったので三項演算子した。%%

%%なお、%% this.newWindow とするには関数ではくて React.Component のサブクラスにする必要がある。

## 標準的なやり方ではフィールドを使わない

「[Thinking in React - React](https://reactjs.org/docs/thinking-in-react.html)」によると、

- 変更のある値はstateにする
- またがってstateを利用するコンポーネントのルートがstateをもつ
- 子コンポーネントからの伝達はハンドラにてする

ということのはずなので、通常はフィールドに変更のある値を持たない。従ってrefを使うこともない。

今回のは NewWindow がもってしまっているので、通常のケースではない。

# 参考

- [Refs and the DOM - React](https://reactjs.org/docs/refs-and-the-dom.html)
- [rmariuzzo/react-new-window: 🔲 Pop new windows in React, using `window.open`.](https://github.com/rmariuzzo/react-new-window)
- [Reactのrefを理解する@Typescript - Qiita](https://qiita.com/knknkn1162/items/29d675c8cd26592a95b5)
