---
title: "Wicket/ローカルの画像ファイルを表示する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 実装

## コンテキスト内
公開ディレクトリに配置しているコンテキスト内の静的ファイルならば、src属性に画像の相対パス（またはURL）を指定したほうが無駄な処理がない。

{% raw %}
```
item.add(
  new WebMarkupContainer("hoge")
  .add(new SimpleAttributeModifier("src", "moge.jpg"))
);
```
{% endraw %}

URLでアクセスできる画像ならば、そのURLを指定することで表示させることができる（src属性値を書くのと同じだから。）

## コンテキスト外
非公開ディレクトに配置した画像をアプリケーションを介して表示させるたいとき、Imageコンポーネントにバイナリを読み込んで渡してあげる。

{% raw %}
```
final String imagePath = <ファイルパス>;
Resource image = new DynamicImageResource() {
  @Override
  protected byte[] getImageData() {
    // imagePathから画像のバイト列を取得する
    return <画像のバイト列>;
  }
};
item.add(new Image("hoge", image));
```
{% endraw %}

注意しなければならないのは、アプリケーションがgetImageData()をコールするのはブラウザが画像を取得するときだということ。つまり、ページをレンダリングした後、になる。リソースのファイルパスをLoadableDetachableModelに保持していると、アプリケーションはファイルパスを取得できなくなる。

# 参照
- http://wicket.apache.org/apidocs/1.3/org/apache/wicket/markup/html/image/resource/DynamicImageResource.html
- http://java.sun.com/j2se/1.5.0/ja/docs/ja/api/java/io/FileOutputStream.html
- http://java.sun.com/javase/ja/6/docs/ja/api/java/io/FileInputStream.html
