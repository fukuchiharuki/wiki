---
title: "障害メモ/React Navigationで作成するヘッダがステータスバーに被る"
date: 2017-12-30T13:01:28+09:00
last_modified_at: 2017-12-30T13:01:28+09:00
---

# キーワード

- React Native
- React Navigation

# 現象

React Nativeにて、React Navigationで作るヘッダがステータスバーに被ってしまう。

- expo経由・Android実機で被る
- iOSのシミュレータでは問題ない
- ビルドしてデプロイしたときにどうかは見てない

# 原因

分からない。

# 対策

StackNavigator()の第2引数に次を追加する。

{% raw %}
```
{
  cardStyle: {
    paddingTop: (Platform.OS === 'ios')? 0: StatusBar.currentHeight
  }
}
```
{% endraw %}

なお、次のimportが必要。

{% raw %}
```
import { Platform, StatusBar } from 'react-native'
```
{% endraw %}

# 備考

なし。

# 参考

- [Android header is overlapped · Issue #1478 · react-navigation/react-navigation](https://github.com/react-navigation/react-navigation/issues/1478)
