---
title: "Angular2/ブラウザがrequiredをチェックしてしまって困る"
date: 2016-11-14T16:13:42+09:00
last_modified_at: 2016-11-14T16:13:42+09:00
---

# キーワード

- Angular2
- required
- ngForm
- ngModel

# したいこと

inputにrequiredをつけたvalidationをAngular2で実装したいが、ブラウザがhtml5の枠組みでrequiredをチェックしてしまい、ブラウザのメッセージが邪魔。Angular2だけでvalidationしたい。

# どうやって

{% raw %}
```
<form novalidate>
```
{% endraw %}

novalidateはAngular2ではなくて、html5の記述。

# ノート

NgFormに関する公式のドキュメントでもnovalidateを書いている。validateしてるはずなのにnovalidateとはどういうことかと思ったが、html5でやってくれなくていいよ、ということのようだ。

# 参考

- [NgForm - ts - API](https://angular.io/docs/ts/latest/api/forms/index/NgForm-directive.html)
