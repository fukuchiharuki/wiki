---
title: "設計パターン/ファクトリ"
date: 2014-05-26T13:10:35+09:00
last_modified_at: 2014-05-26T13:10:35+09:00
---

# キーワード
- エンティティ
- 生成
  - インスタンス

# 何か

```
専門工場
```

インスタンスの生成をするための専用クラスを設けます。

# なぜか

インスタンスを生成する(完全なインスタンスの状態を用意する)のに必要な属性情報を組み立てる手順を要する場合があります。この組み立ての手順はドメインモデルにおいてどのクラスの責務にもなりません。

生成される側が組み立てようとすると、たとえばエンティティとして設計したクラスがアプリケーション上の制約(たとえばリクエスト情報を使用するなど)と密な関係になってしまいます。生成する側が組み立てようとすると、コントロールとして設計したクラスが処理の流れ(: 本来メッセージのやりとりだけで表現したいもの)以上の仕事を過剰に負ってしまいます。

- どのモデルの仕事としても不適合
- アプリケーション上の制約と密になる
- 組み立ての手順によって仕事が過剰になる

そこで、インスタンスの生成を専門の責務にするファクトリを設けます。

# どのように

ファクトリによってインスタンスを生成するようにします。

```
UserEntityFactory factory = new UserEntityFactory();
UserEntity user = factory.createUser("haruki", "fukuchi", "B");
```

ファクトリは完全なインスタンスとしての整合性や妥当性を保証します。

```
UserEntityFactory {

  createUser(firstName, lastName, bloodType) {
    UserEntity user = new UserEntity();
    /*
     * 組み立てるための手続き
     */
    return user;
  }

}
```

# 関連
- [設計パターン/リポジトリ]({% post_url 2014-05-23-018RMN9MBRG85AC3D582B83F4M %})
- [設計パターン/ビルダー]({% post_url 2014-05-27-018RXJBHQGBM4SCF0RJPXYEH1D %})
- [設計パターン/完全コンストラクタ]({% post_url 2014-05-22-018RHZ3Z800B1S536GC6CJ199N %})

# 参考
- [ドメイン駆動設計・アプリケーション構築編・ファクトリ - Strategic Choice](http://d.hatena.ne.jp/asakichy/20110531/1306794692)
- [オブジェクト思考: Factory (ファクトリ) パターン](http://think-on-object.blogspot.jp/2011/11/factoryfactory-methodabstract-factory.html)
