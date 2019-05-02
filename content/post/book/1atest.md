---
title: テストですよこれは
date: 2019-04-08
product:
    name: ほげ
---

Markdownで書いたらこうなるっていうテスト

一行開けるとこうなる

一行開けない改行はどうレンダリングされるでしょうか。
それはここを見ればわかります。
ちなみにデフォルトでは改行されません。
改行を反映させるには、hugoが利用しているblackfridayというMarkdownパーサの設定に付け加えてやる必要があります。
その方法は、各Markdownファイルのfront matterで設定するか、もしくはconfigファイルで全体に適用させるかのどちらかです。

ちなみに`config.toml`に設定をする場合はこう。[^1]

```
[blackfriday]
    extensions = ["hardLineBreak"]
```

```
// this is a code block in markdown
function hoge() {
    console.log("hoge");
}
```

> 引用文はこれね

`var hoge = "fuga";`というのはインラインコードブロックであります。

スラッグが重複した場合、エラーにはならないけれど後からレンダリングされたものが優先されるっぽい？

[^1]: これがフットノート、注釈ですわ。