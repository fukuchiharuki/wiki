---
title: "シェル/リアルタイムにgrepする"
date: 2024-08-27T14:56:26+09:00
last_modified_at: 2024-08-27T14:56:26+09:00
---

# キーワード

- grep
- tail

# したいこと

標準出力に出力されつづけるテキストをパイプしてリアルタイムにgrepして表示したい。

# どうやって

{% raw %}
```
(標準出力に出力しつづけるコマンド) | grep --line-buffered 'something'
```
{% endraw %}

たとえばtail -fなどが標準出力に出力しつづけるコマンド。

# ちなみに

{% raw %}
```
$ man grep 
     --line-buffered
             Force output to be line buffered.  By default, output is line buffered when standard output is a terminal and block buffered otherwise.
```
{% endraw %}

# 参考

- [リアルタイムに「tail -f」をgrepする方法 #Linux - Qiita](https://qiita.com/naotarou/items/ee2afc15804e37129c2d)
