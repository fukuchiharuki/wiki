---
title: "シェル/ファイルの中身をgrepしてファイル名をリストする"
date: 2015-04-03T18:00:11+09:00
last_modified_at: 2015-04-03T18:00:11+09:00
---

&color(red){次と重複};
- [シェル/特定の文字列を含むファイルを探す]({{ site.baseurl }}{% post_url 2014-12-23-0199TQ9NJRR6ST366FG7VSTVB1 %})

# キーワード
- find
- grep

# やりたいこと

特定の文字列を含むファイルのファイル名をリストしたい。

# どうやって

たとえば「HOGE」を探す場合

```
$ find . -name "*.txt" -exec grep -q HOGE {} \; -print
```

または

```
$ find . -name "*.txt" -print | xargs grep HOGE
```

# 備考
オプションでgrepするか、パイプしてxargs越しにgrepする。

# 参考
- [find -execの使い方 - にたまごほうれん草](http://d.hatena.ne.jp/emergent/20071127/1196091725)
