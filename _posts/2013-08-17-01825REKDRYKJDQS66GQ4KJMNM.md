---
title: "MySQL/サーバーサイドPreparedStatementする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- MySQL
- Java

# 概要
JavaでサーバーサイドPreparedStatementします。

# 方法
接続URLに次のパラメータを足します。

```
useServerPrepStmts=true
```

# 解説
デフォルトの接続だとどうもクライアントPreparedStatementしてるようです（クライアント側でパラメータをバインドしたSQL文を作成して投げる）。
これに伴ってU+00A5問題なんてのがあるようです。

しかしサーバーサイドPreparedStatementの採用はそれほどポジティブでもないようです。
なぜならそもそも実行計画をキャッシュすることがないようだからです。

# 参考
- http://blog.everqueue.com/chiba/2008/12/23/33/
- http://d.hatena.ne.jp/kazuhooku/20081224/1230084621
