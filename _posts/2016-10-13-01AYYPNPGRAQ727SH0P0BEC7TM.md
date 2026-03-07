---
title: "Angular2/覚書"
date: 2016-10-13T18:41:19+09:00
last_modified_at: 2016-10-13T18:41:19+09:00
---

# バインディング

## 単方向

```
{{hero.name}}
```

表示させたいところに書くだけ。

## 双方向

```
[(ngModel)]="hero.name"
```

inputのvalue属性の代わりにする。

# 制御

## 条件

```
<div *ngIf="selectedHero"></div>
```

selectedHeroが定義されると現れる。

## 繰り返し

```
<li *ngFor="let hero of heroes"></li>
```

「let 変数 of コレクション」は決まり文句。

# イベント

## クリック

```
<li .. (click)="onSelect(hero)">
```

「onSelect()」は任意のメソッド。「hero」は引数（*ngForしている変数など）。

# コンポーネント

## プロパティ・インプット

渡す側。

```
<my-hero-detail [hero]="selectedHero"></my-hero-detail>
```

受ける側。

```
@Input()
hero: Hero;
```

「=」を書いているが代入ではない。<br>
ので、my-hero-detail側で書き換えればmy-appでも書き換わる。
