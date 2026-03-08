---
title: "IntelliJ/変更のあるファイルを含むフォルダに色をつける"
date: 2018-02-20T15:32:03+09:00
last_modified_at: 2018-02-20T15:32:03+09:00
---

# キーワード

- IntelliJ
- Git
- ファイル
- フォルダ

# したいこと

Gitなどのバージョン管理は当然使うものとして、ファイル一覧で変更のあるファイルには色がつく。しかしこれを含むディレクトリには色がつかない。すごく困っている。Eclipseでは色がつくのに。なんとかしてください。

# どうやって

次にチェックを入れる。

- Prefferences.. > Version Control > Show directories with changed descendants

# ちなみに

cogアイコン下にある Flatten Packages を有効にするとEclipseのパッケージ・エクスプローラみたいにできる。

ああ、これでやっと。

# 参考

- [View VCS folder status &ndash; IDEs Support (IntelliJ Platform) \| JetBrains](https://intellij-support.jetbrains.com/hc/en-us/community/posts/207002455-View-VCS-folder-status)
