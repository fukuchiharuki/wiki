---
title: "はじめてのAngular2/EclipseでTypeScript"
date: 2016-07-02T17:25:53+09:00
last_modified_at: 2016-07-02T17:25:53+09:00
---

vimでもいいのですが、やっぱりIDEがほしい。使い慣れたEclipseでTypeScriptな環境を作ることにしました。

&color(red){-- 嘘です！[Atomを使うことにしました](../AtomでTypeScript.md)};

# TypEcs - TypeScript IDE for Eclipse

- [TypEcs - TypeScript IDE for Eclipse](http://typecsdev.com)

Quick Startのとおりでインストールできる。普通にプラグインをインストールするやり方。

## NodeJSがインストールされていません

![an_error.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_616E5F6572726F722E706E67' | relative_url }})

```
An error occured during TypeScript engine initialization.
TypeScript runtime requires NodeJS that should be installed separately.
It seems NodeJS is not installed or is not available in system path.
```

NodeJSが見つからないからTypeScriptエンジンが初期化できないそうです。いやいや、まてまて、そんなはずはない。Hello Worldやったもん。nodeもnpmも動いてるはずだよ？

- Macを使っています
- nodebrewでnodeをインストールしました

### /usr/local/bin/nodeなら見つかった

シンボリックリンクで /usr/local/bin/node を作ってあげるとエラーはでなくなった。PATH変数をみているのではどうやらなさそう。でもこのシンボリックリンクは気持ちが悪い。共有の場所からホームディレクトリへのシンボリックリンクはさすがにイヤ。

### /usr/local/bin/nodeを作る

ホームディレクトリを直に書いてシンボリックリンクを張るのは気持ちが悪いので、環境変数を使ってホームディレクトリ下のnodeに橋渡しするスクリプトを書いて置いておくことにしました。なければ呼べないだけ。

- /usr/local/bin/node 

```
$HOME/.nodebrew/current/bin/node $@
```

### %%システムパスにnodebrewを追加する%%

&color(red){-- この方法では解決できていませんでした};

Macのシステムパスを追加するには/etc/paths.d/にパスを書いたファイルを作成してあげればよいみたいです。

- /etc/paths.d/node

```
~/.nodebrew/current/bin
```

次のようにたどれます。

- /etc/profile から /usr/libexec/path_helper を実行している
- path_helperは /etc/paths.d/* を読み上げている
- /etc/paths.d/node を追加する

この記事が教えてくれました。

- [PATH設定がどこにあるか分からないときに見るべきファイル - Qiita](http://qiita.com/gm_kou/items/24dec9f0e51b9343651b)

# Validationを省く

ううん、エラーがいっぱい出るよう。動くからいいんだけど、さすがに気になるのでエラーがでないようにします。

## node_modulesは見ない

node_modulesはnpmでインストールされるものなのでここはみてくれなくてもいい。くれなくてもいいというか、ここでエラー出ちゃうのって＞＜

### Include Path

1. プロジェクトを右クリックして Properties を開く
1. JavaScript > Include Path を選択
1. Excluded: (None) を選択して Edit... をクリック

![include_path_1.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_696E636C7564655F706174685F312E706E67' | relative_url }})

1. Exclusion patterns: の方の　Add... をクリック

![include_path_2.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_696E636C7564655F706174685F322E706E67' | relative_url }})

1. Browse... をクリック

![include_path_3.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_696E636C7564655F706174685F332E706E67' | relative_url }})

1. ファイル一覧から node_modules を選択して OK、OK、Finish をクリック

![include_path_4.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_696E636C7564655F706174685F342E706E67' | relative_url }})

1. Excluded: node_modules/ の表示を確認

![include_path_5.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_696E636C7564655F706174685F352E706E67' | relative_url }})

### HTMLとJSON

1. メニューの Eclipse > 環境設定... をクリック
1. Validation を選択
1. HTML Syntax Validator のチェックを外す（Angular2の書き方だと必ず警告が出てダルいので）
1. JSON Validator 行の ... をクリック

![json_1.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_6A736F6E5F312E706E67' | relative_url }})

1. Add Exclude Group... をクリック
1. Exclude Group を選択して Add Rule... をクリック

![json_2.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_6A736F6E5F322E706E67' | relative_url }})

1. Folder or file name を選択して Next > をクリック

![json_3.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_6A736F6E5F332E706E67' | relative_url }})

1. Browse Folder... をクリック
1. 何も選択せずそのまま 開く をクリック（ここが謎のコツ）

![json_4.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_6A736F6E5F342E706E67' | relative_url }})

1. node_modules を入力して Finish をクリック

![json_5.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_6A736F6E5F352E706E67' | relative_url }})

1. Exclude Group に Folder: node_modules の表示を確認

![json_6.png]({{ '/images/wiki/E381AFE38198E38281E381A6E381AE416E67756C6172322F45636C69707365E381A754797065536372697074_6A736F6E5F362E706E67' | relative_url }})
