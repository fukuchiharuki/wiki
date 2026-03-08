---
title: "Vim/ファイルタイプを指定してインデントする"
date: 2014-05-03T13:13:06+09:00
last_modified_at: 2014-05-03T13:13:06+09:00
---

# キーワード

- Vim

# やりたいこと
ファイルタイプを自動認識してくれないときに自動インデントを有効にしたい。

# 設定に書いとけって話ではある

# 方法

- インデントを有効にする

{% raw %}
```
:filetype indent on
```
{% endraw %}

- ファイルタイプをhtmlにする

{% raw %}
```
:set filetype=html
```
{% endraw %}

# 詳細
同じ filetype なのに別の書き方をしたりして混乱するね。

# 参考

- [Vim documentation: filetype](http://vim-jp.org/vimdoc-ja/filetype.html)
