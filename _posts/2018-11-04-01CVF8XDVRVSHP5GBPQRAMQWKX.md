---
title: "React/絶対パスでimportを書く"
date: 2018-11-04T20:49:47+09:00
last_modified_at: 2018-11-04T20:49:47+09:00
---

# キーワード

- React
- JavaScript
- import
- VisualStudio Code, VS Code

# したいこと

絶対パスでimportを書きたい。

相対パスでimportが並ぶと単純に見通しが悪いだけでなく、リファクタリングしづらい。

# どうやって

## webpackの設定

{% raw %}
```
resolve: {
    modules: ['node_modules', 'src'],
    extensions: ['.js', '.jsx']
},
```
{% endraw %}

## VisualStudio Codeの設定

プロジェクトのルートディレクトリに jsconfig.json を作成して次を書く。 

{% raw %}
```
{
    "compilerOptions": {
        "target": "es2015",
        "baseUrl": "./src/"
    }
}
```
{% endraw %}

//* ちなみに [#n87e0748]

# 参考

- [大規模でスケールするReactアプリケーション開発のための実践的アドバイス - WPJ](https://www.webprofessional.jp/organize-large-react-application/)
- [[React]絶対パスでimportできるようにする with vscode and eslint - Qiita](https://qiita.com/ozaki25/items/03e1a229123293241ab8)
- [Resolve](https://webpack.js.org/configuration/resolve/#resolve-modules)
- [jsconfig.json Reference](https://code.visualstudio.com/docs/languages/jsconfig)
