---
title: "Angular2/覚書"
date: 2016-10-13T18:41:19+09:00
last_modified_at: 2016-10-13T18:41:19+09:00
---

# バインディング

## 単方向

{% raw %}
```
{{hero.name}}
```
{% endraw %}

表示させたいところに書くだけ。

## 双方向

{% raw %}
```
[(ngModel)]="hero.name"
```
{% endraw %}

inputのvalue属性の代わりにする。

# 制御

## 条件

{% raw %}
```
<div *ngIf="selectedHero"></div>
```
{% endraw %}

selectedHeroが定義されると現れる。

## 繰り返し

{% raw %}
```
<li *ngFor="let hero of heroes"></li>
```
{% endraw %}

「let 変数 of コレクション」は決まり文句。

# イベント

## クリック

{% raw %}
```
<li .. (click)="onSelect(hero)">
```
{% endraw %}

「onSelect()」は任意のメソッド。「hero」は引数（*ngForしている変数など）。

# コンポーネント

## プロパティ・インプット

渡す側。

{% raw %}
```
<my-hero-detail [hero]="selectedHero"></my-hero-detail>
```
{% endraw %}

受ける側。

{% raw %}
```
@Input()
hero: Hero;
```
{% endraw %}

「=」を書いているが代入ではない。<br>
ので、my-hero-detail側で書き換えればmy-appでも書き換わる。
