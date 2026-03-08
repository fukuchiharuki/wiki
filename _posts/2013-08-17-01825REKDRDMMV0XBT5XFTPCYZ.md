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

{% raw %}
```
$ vi ~/.bash_logout
```
{% endraw %}

次の行を追加します。

{% raw %}
```
history -c
```
{% endraw %}

# 解説

<dl>
<dt>.bach_logout</dt>
<dd>ログアウト時に実行するスクリプト</dd>
<dt>history -c</dt>
<dd>コマンドの実行履歴をクリアする</dd>
</dl>

# 参考
- http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230795/
