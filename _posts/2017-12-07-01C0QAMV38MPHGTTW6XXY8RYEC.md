---
title: "React/条件分岐と繰り返しをする"
date: 2017-12-07T10:50:09+09:00
last_modified_at: 2017-12-07T10:50:09+09:00
---

# キーワード
- React
- 条件分岐 (if)
- 繰り返し (for)

# したいこと

Reactで条件分岐や繰り返しをして描画したい。

# どうやって

普通に条件分岐と繰り返しをする（！？）。

## 条件分岐

```
const ResultLabel = ({state}) => (
    <div>
        Result:
        <span>
            {
                state.showingResult
                    ? state.resultValue
                    : state.inputValue
            }
        </span>
    </div>
)
```

## 繰り返し

```
const HistoryList = ({state}) => (
    <div>
        <ul>
            {
                state.resultHistory.map(result => (
                    <li key={result.id}>{result.value}</li>
                ))
            }
        </ul>
    </div>
)
```

# ちなみに

「{}」の中で変数や配列を置いてやれば、その変数の値や配列の要素の値を書いてくれます。if文やfor文を使おうとすると即時関数でreturnする必要があるのでちょっと手間です。ので、三項演算子やArray.prototype.map()を使う方がシュッとします。

「()」でJSX要素が返却できるのはなんでかっていうと、ラムダ式になっているからなだけですね。

なお、繰り返し中に「key」を指定しないと「ユニークなkeyをもつべし」と[怒られます]({% post_url 2017-12-07-01C0QAHXB836Q53AN27R729XMC %})ので注意。

# 参考
- [React.jsのJSXで条件分岐・繰り返しを記述する - Qiita](https://qiita.com/r7kamura/items/b16cb11b30a54d3c607d)
- [ReactのJSXでifやforを使いたい場合 - Qiita](https://qiita.com/yuch_i/items/ec24579024c221979317)
- [JSX | XML-like syntax extension to ECMAScript](https://facebook.github.io/jsx/)
