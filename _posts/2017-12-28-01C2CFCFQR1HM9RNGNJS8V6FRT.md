---
title: "JavaScript/文字列からオブジェクトのプロパティを参照・更新する"
date: 2017-12-28T02:12:43+09:00
last_modified_at: 2017-12-28T02:12:43+09:00
---

# キーワード
- JavaScript
- オブジェクト
  - プロパティ
- 配列
  - インデックス

# したいこと

```
name = "a.b"
```

で

```
data.a.b
```

を参照したい。また更新したい。

# どうやって

## 参照

```
console.log(
  name.split('.').reduce((data, prop) => data[prop], data)
)
```

## 更新

```
;(a => { a.pop(); return a })(name.split('.')).reduce((data, prop) => data[prop], data)[(a => a.pop())(name.split('.'))] = value
```

# 例

```
const data = {
	numbers: [ "one", "two", "three" ],
	greeting: {
		hi: "Hi!"
	},
}

name = "numbers.3"
value = "four"

;(a => { a.pop(); return a })(name.split('.')).reduce((data, prop) => data[prop], data)[(a => a.pop())(name.split('.'))] = value
console.log(name.split('.').reduce((data, prop) => data[prop], data))

name = "greeting.hello"
value = "Hello!"

;(a => { a.pop(); return a })(name.split('.')).reduce((data, prop) => data[prop], data)[(a => a.pop())(name.split('.'))] = value
console.log(name.split('.').reduce((data, prop) => data[prop], data))

console.log(data)
```

の結果は、

```
four
Hello!
{numbers:["one","two","three","four"],greeting:{hi:"Hi!",hello:"Hello!"}}
```

になる。

オブジェクトならオブジェクトとしてプロパティが、配列なら配列としてインデックスが追加できてしまうのがJavaScriptの融通が効くすばらしいところ。

# ちなみに

## 前提知識

### オブジェクトのプロパティは連想配列のようにできる

```
data.a.b
```

は

```
data[a][b]
```

と同じ。

### 配列のインデックスは文字列でもよい

```
data.c
```

が配列なら

```
data.c[0]
```

と

```
data.c['0']
```

は同じに振る舞う。ので、名前は "c.0" とできる。

## 解説

### name.split('.')

プロパティの階層を掘るのに「.」を使うことを決めて、プロパティ名の配列を作る。

### %%[data, ...names]%%

%%dataが先頭にあって、プロパティ名が後に続く配列を作る。%%

### .reduce((data, prop) => data[prop], data)

dataから順番にプロパティを掘っていく。%%先にdataを先頭に乗せたのはそのため。%%reduce()でinitialValueを与えることができる。

### (a => { a.pop(); return a })(names)

更新の場合、末端のプロパティのプリミティブ型の値（の、ばっかり）を得てしまっても意味がない。ので、ひとつ手前まで取得するように、プロパティ名の配列（末端を除く）を作成する。

### (a => a.pop())(name.split('.'))

ひとつ手前までのオブジェクトまたは配列まで取得したら最後に末端のプロパティ名またはインデックスを指定する。そこに値を代入する。

### ;

文末に「;」を書かない派だと、前の文によっては誤解が生じるので文を切っておく。

# 参考
- [String.prototype.split() - JavaScript \| MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/String/split) 
- [スプレッド演算子 - JavaScript \| MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Spread_operator)
- [Array.prototype.reduce() - JavaScript \| MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
- [Array.prototype.pop() - JavaScript \| MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
- [アロー関数 - JavaScript \| MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/arrow_functions)
