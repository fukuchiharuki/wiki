---
title: "Linux/ログアウト時にコマンドの実行履歴をクリアする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- Linux
- .bash_logout
- コマンド
- 実行履歴

# 概要
ログアウト時にコマンドの実行履歴をクリアします。

# 方法
.bash_logout に

```
$ vi ~/.bash_logout
```

次の行を追加します。

```
history -c
```

# 解説
:.bach_logout|ログアウト時に実行するスクリプト
:history -c|コマンドの実行履歴をクリアする

# 参考
- http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230795/
