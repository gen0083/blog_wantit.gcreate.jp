[![CircleCI](https://circleci.com/gh/gen0083/blog_wantit.gcreate.jp/tree/master.svg?style=svg)](https://circleci.com/gh/gen0083/blog_wantit.gcreate.jp/tree/master) [![Netlify Status](https://api.netlify.com/api/v1/badges/b9975b41-720e-4d51-b850-ec5d153ebef1/deploy-status)](https://app.netlify.com/sites/laughing-einstein-5f6ad9/deploys)

## 新しい記事の作成

`hugo new --kind has-image post/{sub-category}/{post-name}`

例: `hugo new --kind has-image post/bicycle/my-new-bike`

デフォルトで`{post-name}`がslugに設定される。
slugが重複している場合、ビルド時にエラーが出るようになるのでその際はslugをユニークなものに変更すること。
記事内で使う画像リソースは`{post-name}`のディレクトリ内に配置すればよい。

画像の配置は`![alt属性で表示される説明文](画像ファイル名)`。

## タグについて

frontmatterで設定する。

```
tags:
    - タグ1
    - タグ2
```

タグを設定しない場合は`tags`はあってもいいが、その配下のリストは削除しておくこと。
`-`だけあるとpermalinkの重複によってビルドが失敗する。

## サマリについて

サマリを登録する方法は2つ

1. `<!--more-->`までの部分に書いたもの
2. frontmatterの`description`に書いたもの

優先度は`description`が高く、値が設定されていないdescriptionが存在すると`<!--more-->`は無視される。

参照の仕方:

1. `.Summary`
1. `.Params.description`

## ショートコード

Markdown内で使えるショートコード: [公式ドキュメント](https://gohugo.io/content-management/shortcodes/)

`{{< ショートコード >}}`のような形で使う

- gist `{{< gist username gistID >}}`
- tweet `{{< tweet tweetID >}}`
- YouTube: `{{< youtube ビデオID >}}`
- リンク `{{< ref "コンテンツのslug" >}}`

リンクに関してはURLに変換されるだけのため、`[hoge]({{< ref "hoge" >}})`のように使う必要がある。

## textlintの一時的な無効化

どうしてもtextlintのルールを無視したい場合はつぎのコメントを挿入することで、部分的にtextlintを無効化できる。

```
<!-- textlint-disable -->
ここはtextlintのルールを無視してもエラーにならない
<!-- textlint-enable -->
以降はtextlintのルールが有効になってチェックされる。
```

記事中で話し言葉っぽい書き方をどうしてもしたいときなどに使える。

## デプロイ

現状では記事を書いたらプルリクを送り、その後`master`にマージしたら公開されるようになっている。

`git push`したあと`hub pull-request`でプルリクを送る。マージはGitHub上でやる。

`./script/delete-merged-branch.sh`を実行すれば作成したマージ済みのブランチを消すことができる。

## ライセンス

利用しているhugoテーマ: [aether](https://github.com/josephhutch/aether)
> MIT © Joe Hutchinson

改変している部分に関してはMIT © gen0083

記事自体のライセンス
Copyright © gen0083

というスタンスですが、細かくはまたあとで整備する
