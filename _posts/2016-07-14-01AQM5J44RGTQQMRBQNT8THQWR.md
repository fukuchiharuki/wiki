---
title: "はじめてのAngular2/Componentを作る・利用する"
date: 2016-07-14T16:39:59+09:00
last_modified_at: 2016-07-14T16:39:59+09:00
---

# Componentってなに

Componentはビューとロジックをもった要素。

# Componentを作る

- @Component（メタデータ）をつけて
```
@Component({
  selector: 'alert-button',
  template: `
    <button (click)="onClick()">Click me!</button>
  `
})
```

- classをexportする
```
export class AlertButtonComponent{
  onClick(): void {
    window.alert('Hello!!');
  }
}
```

メタデータに名前（セレクタ）やテンプレート、スタイルを書きます。Javaでいうところのアノテーションみたいな感じですかね。書き方も似ていますし。classはそのまま、Java同様のクラスですね。そのコンポーネントの属性と振る舞いを書きます。

Componentを用意して組み合わせていくのが最近の向きらしいですね。プログラミングとして新しい概念ではありませんが、jQueryでDOM操作をガリガリするのがもう辛すぎたということでしょう。確かに辛かった。

# Componentを利用する

- exportしたクラスをimportして
```
import {AlertButtonComponent} from './alert-button.component';
```

- メタデータのdirectivesに追加して
- メタデータのtemplateで使う
```
@Component({
  selector: 'my-app',
  template: `
    <h1>My First Angular 2 App R2</h1>
    <alert-button></alert-button>
  `,
  directives: [AlertButtonComponent]
})
```

Componentはselectorで名前がついているので、使う側はその名前にてtemplateで使う。

# ソースコード

- [til/javascript/angular2/angular2-practical-ABC-r2 at master · fukuchiharuki/til](https://github.com/fukuchiharuki/til/tree/master/javascript/angular2/angular2-practical-ABC-r2)

# 参考

- [Angular2のコンポーネント、bootstrap関数の概要 | VPSサーバーでWebサイト公開　備忘録　~Linux、MySQLからAJAXまで](http://wordpress.honobono-life.info/code/angular2のコンポーネント、bootstrap関数の概要/)
