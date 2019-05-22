## 新しい記事の作成

`hugo new --kind has-image post/{sub-category}/{post-name}`

例: `hugo new --kind has-image post/bicycle/my-new-bike`

デフォルトで`{post-name}`がslugに設定される。
slugが重複している場合、ビルド時にエラーが出るようになるのでその際はslugをユニークなものに変更すること。
記事内で使う画像リソースは`{post-name}`のディレクトリ内に配置すれば良い。

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

## ライセンス

利用しているhugoテーマ: [aether](https://github.com/josephhutch/aether)
> MIT © Joe Hutchinson

改変している部分に関してはMIT © gen0083

記事自体のライセンス
Copyright © gen0083

というスタンスですが、細かくはまたあとで整備する
