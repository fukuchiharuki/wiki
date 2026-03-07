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

```
TypeError: Cannot read property 'func' of undefined
```

# 原因

React.PropTypesは非推奨になった。

# 対策

> Please use the prop-types library instead.

prop-typesを使え、ということのようです。

```
import React, { PropTypes } from 'react'
```

などとしていたところを次のようにする。

```
import PropTypes from 'prop-types'
```

# 備考

インストールも忘れずに。

```
$ npm install --save prop-types
```

# 参考
- [Typechecking With PropTypes - React](https://reactjs.org/docs/typechecking-with-proptypes.html)
- [電卓アプリで学ぶReact/Redux入門(実装編) - Qiita](https://qiita.com/nishina555/items/9ff744a897af8ed1679b)
