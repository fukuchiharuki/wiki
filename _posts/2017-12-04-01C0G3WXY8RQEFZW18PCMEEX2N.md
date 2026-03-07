---
title: "AngularJS/イベントリスナを手動で削除する"
date: 2017-12-04T15:37:33+09:00
last_modified_at: 2017-12-04T15:37:33+09:00
---

# キーワード
- AngularJS
- ディレクティブ
- イベントリスナ

# したいこと

$on()を経由せずエレメントに直接追加したイベントリスナは手動で削除する必要があるっぽいです。

# どうやって

「$destroy」イベントを拾って処理する。

```
element.on('click', function () {
  ...
});

scope.$on('$destroy', function () {
  element.off();
});
```

$rootScopeに登録したリスナも片付ける必要があるようです。

```
const deregister = $rootScope.$on('anEvent', function () {
  ...
});

scope.$on('$destroy', deregister);
```

$timeoutでペンディング中のものもキャンセルするべきみたい。

```
const timer = $timeout(function () {
  ...
}, 60000);

scope.$on('$destroy', function () {
  $timeout.cancel(timer);
});
```

# ちなみに

DataTablesにも同じようなことがあるらしい。

# 参考
- [memory leaks - AngularJS - Does $destroy remove event listeners? - Stack Overflow](https://stackoverflow.com/questions/26983696/angularjs-does-destroy-remove-event-listeners)
- [Possible memory leak when refreshing table - DataTables forums](https://datatables.net/forums/discussion/35701/possible-memory-leak-when-refreshing-table)
