---
title: "Angular2/Google Chartsを使う"
date: 2016-10-26T16:31:52+09:00
last_modified_at: 2016-10-26T16:31:52+09:00
---

# キーワード

- Angular2
- Google Charts
- declare

# したいこと

Angular2で作るページにGoogle Chartsを載せたい。

# どうやって

## 用意するもの

- index.html
- チャート用のテンプレート
- チャート用のComponent
- 使う側のテンプレート

## index.html

{% raw %}
```
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
   google.charts.load('current', {'packages':['corechart', 'geochart', 'annotationchart']});
</script>
```
{% endraw %}

index.htmlから普通にGoogle Chartsを使うように書く。パッケージは使うものを任意で。

## チャート用のテンプレート

{% raw %}
```
<div [id]="elementId"></div>
```
{% endraw %}

idはchart描画でgetElementByIdするときに使う。

## チャート用のComponent

{% raw %}
```
import {
  Component,
  OnInit,
  Input,
  HostListener
} from '@angular/core';

declare var google: any;

@Component({
  selector: 'app-my-pie-chart',
  templateUrl: './my-pie-chart.component.html',
  styleUrls: ['./my-pie-chart.component.css']
})
export class MyPieChartComponent implements OnInit {

  elementId: string;

  constructor() { }

  ngOnInit() {
    this.elementId = ’my-pie-chart’;
  }

  ngAfterViewInit() {
    google.charts.setOnLoadCallback(() => this.drawChart());
  }

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.drawChart();
  }

  drawChart() {

    // data
    let data = new google.visualization.DataTable();
    data.addColumn('string', 'Topping');
    data.addColumn('number', 'Slices');
    data.addRows([
      ['Mushrooms', 3],
      ['Onions', 1],
      ['Olives', 1],
      ['Zucchini', 1],
      ['Pepperoni', 2]
    ]);

    // options
    let options = {
      title: 'How Much Pizza I Ate Last Night'
    };

    // draw
    let chart = new google.visualization.PieChart(document.getElementById(this.elementId));
    chart.draw(data, options);

  }

}
```
{% endraw %}

大事なところは次。

### 外部ライブラリの利用

{% raw %}
```
declare var google: any;
```
{% endraw %}

なんとこれだけでgoogle.*が普通に使える。（jQueryも同じようにいける）

### 描画関数の登録

{% raw %}
```
  ngAfterViewInit() {
    google.charts.setOnLoadCallback(() => this.drawChart());
  }
```
{% endraw %}

ngOnIinitではidを与える前に動いてしまうのかエラーになった。ので、描画後イベントにした。

### リサイズに対応

{% raw %}
```
  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.drawChart();
  }
```
{% endraw %}

リサイズイベントはデコレータでとるのがいいと思う。

## 使う側のテンプレート

{% raw %}
```
<app-my-pie-chart></app-my-pie-chart>
```
{% endraw %}

使うだけ。

# ノート

declareで外部のJavaScriptコードがなんでも呼べる。jQueryだって使える。

# 参考

- [Angular2 + Google Charts. How to integrate Google Charts in Angular2? - Stack Overflow](http://stackoverflow.com/questions/37542408/angular2-google-charts-how-to-integrate-google-charts-in-angular2)
- [Quick Start  \|  Charts  \|  Google Developers](https://developers.google.com/chart/interactive/docs/quick_start)
