---
title: "Spring Boot/作り始めにやること"
date: 2017-03-23T12:49:51+09:00
last_modified_at: 2017-03-23T12:49:51+09:00
---

Spring Bootに限った話ではないけど、作り始めに整えておいた方がいいこと。

### ビルド
- [プロジェクト分割]({{ site.baseurl }}{% post_url 2017-03-23-01BBWMX9ZGCN5SAZ878974BECX %})
  - Gradle
  - 依存関係
- DB接続
  - データソース設定
  - 自動化ツール(MyBatis Generator)
- DI
  - Mapper(MyBatis)

### 動作確認
- STSで(for development)
- jarをキックして(for production)

### 開発環境
- ソースコードリポジトリ
- インポート手順

### IDE
- STSプラグイン
  - Buildship
  - EGit
  - Properteis Editor
  - Vrapper
- 設定
  - 文字コード

### 実装方式
- 配置
  - テンプレート
  - リソース
  - Mapper(MyBatis)
- 定数
  - domainの定数(Springに頼らない実装)
  - application.yml(Springに頼る実装)
  - staticな定数(リクエストマッピング名やテンプレート名)

### 例外処理
- システムエラー
  - すべてのエラーの受け皿として
- 画面遷移
  - どこが入力チェックの役割をもつか
- フィードバック
  - 検査例外 or NOT
  - メッセージ

ぜんぜん途中
