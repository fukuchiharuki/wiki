---
title: "障害メモ/Titanium SDK 2.0.1にしてからiPhone用にビルドできない"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連

- Titanium Mobile
- Xcode

# 現象
Titanium SDKのバージョンを2.0.1にしてからiPhone用のビルドができない。

現象は[ここ](http://developer.appcelerator.com/question/135521/build-error-with-titanium-sdk-201--ios-sdk-42)。

# 原因
Xcodeのバージョンによる？

# 対策

- OSをLionにする
- AppStoreからXcodeの最新をインストールする
- 次のコマンドを叩く（[Titaniumのドキュメントに解説あり](http://docs.appcelerator.com/titanium/release-notes/?version=2.0.1.GA#xcode43)）

{% raw %}
```
sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
```
{% endraw %}

# 参考

- http://developer.appcelerator.com/question/135521/build-error-with-titanium-sdk-201--ios-sdk-42
- http://docs.appcelerator.com/titanium/release-notes/?version=2.0.1.GA#xcode43
