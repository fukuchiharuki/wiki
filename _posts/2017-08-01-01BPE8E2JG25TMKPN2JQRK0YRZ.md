---
title: "障害メモ/svnクリーンアップがどうしてもできない"
date: 2017-08-01T15:41:22+09:00
last_modified_at: 2017-08-01T15:41:22+09:00
---

# キーワード

- TortoiseSVN
- クリーンアップ
- sqlite

# 現象

システム開発の現場ではまだまだSVNは現役なのです。

TortoiseSVNで何かがどうかなってクリーンアップを求めたれたが、クリーンアップができずにさらにクリーンアップを求められて詰んだ。

{% raw %}
```
Previous operation has not finished; run 'cleanup' if it was interrupted
Please execute the 'Cleanup' command."
```
{% endraw %}

# 原因

言葉どおり受け止めれば、前のオペレーションが済んでないということだが、どうしてこうなったかは分からない。

# 対策

sqliteを使ってsvnのデータベースに残ったゴミを削除してやればよいらしい。

{% raw %}
```
sqlite3 .svn/wc.db "select * from work_queue"
```
{% endraw %}

ここでリストが出てくるようなら次のようにして消す。

{% raw %}
```
sqlite3 .svn/wc.db "delete from work_queue"
```
{% endraw %}

その後、クリーンアップする。このとき、「ロックを強制的に解除する」にチェックを入れた状態でないとだめだったが、もうなにがどうしてということは分からない。

# 備考

sqlite3は別途自分でインストールする必要がある。

# 参考

- [tortoisesvn - Svn error &quot;Previous operation has not finished&quot; - Stack Overflow](https://stackoverflow.com/questions/22715303/svn-error-previous-operation-has-not-finished)
