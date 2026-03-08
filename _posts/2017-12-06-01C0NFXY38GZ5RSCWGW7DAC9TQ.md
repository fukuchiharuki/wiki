---
title: "障害メモ/PropTypes.funcが見つからない"
date: 2017-12-06T17:44:01+09:00
last_modified_at: 2017-12-06T17:44:01+09:00
---

# キーワード

- React
- PropTypes
- func

# 現象

プロパティを定義するところでエラーになる。 

{% raw %}
```
TypeError: Cannot read property 'func' of undefined
```
{% endraw %}

# 原因

React.PropTypesは非推奨になった。

# 対策

> Please use the prop-types library instead.

prop-typesを使え、ということのようです。

{% raw %}
```
import React, { PropTypes } from 'react'
```
{% endraw %}

などとしていたところを次のようにする。

{% raw %}
```
import PropTypes from 'prop-types'
```
{% endraw %}

# 備考

インストールも忘れずに。

{% raw %}
```
$ npm install --save prop-types
```
{% endraw %}

# 参考

- [Typechecking With PropTypes - React](https://reactjs.org/docs/typechecking-with-proptypes.html)
- [電卓アプリで学ぶReact/Redux入門(実装編) - Qiita](https://qiita.com/nishina555/items/9ff744a897af8ed1679b)
