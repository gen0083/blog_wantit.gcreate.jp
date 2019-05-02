---
title: CSSを効率よく記述したい人はぜひ読むべきな、Web制作者のためのSassの教科書
slug: sass-text
description: <p>ずっと前からCSSでサイトデザインする際、ある不満を持っていました。プログラムのように変数が使えたらいいのにと。しかしそんな人に朗報があります。Sassを使えばCSSでも変数が使えるようになるのです。これでCSSの記述がくそ便利になります。</p>

cover_image: images/cover/book.jpg
date: 2013-12-12
lastmod: 2015-01-26
tags: 
    - Web
product:
    name: 'Web制作者のためのSassの教科書'
    number: '4844334662'
    rate: '4.5'
    link: 'http://book.scss.jp/'
    comment: '非常に分かりやすく読みやすい。'
    kaeyome: '<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/4844334662/illusionspace-22/" rel="nofollow" target="_blank"><img src="http://ecx.images-amazon.com/images/I/51xkjL4k%2BRL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4844334662/illusionspace-22/" rel="nofollow" target="_blank">Web制作者のためのSassの教科書 これからのWebデザインの現場で必須のCSSメタ言語</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">平澤 隆,森田 壮 インプレスジャパン 2013-09-13    </div><div class="booklink-link2"><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/asin/4844334662/illusionspace-22/" rel="nofollow" target="_blank" title="アマゾン" >Amazonで購入</a></div><div class="shoplinkrakuten"><a href="http://hb.afl.rakuten.co.jp/hgc/11acbc01.369b1bf6.11acbc02.cabf9fe9/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F12451132%2F%3Fscid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2Fev%2Fbook%2F" rel="nofollow" target="_blank" title="楽天ブックス" >楽天ブックスで購入</a></div>                  	  <div class="shoplinkkino"><a href="http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=3085416&pid=882196163&vc_url=http%3A%2F%2Fwww.kinokuniya.co.jp%2Ff%2Fdsg-01-9784844334668" target="_blank" title="kino" >紀伊國屋書店で購入<img src="http://ad.jp.ap.valuecommerce.com/servlet/gifbanner?sid=3085416&pid=882196163" height="1" width="1" border="0"></a></div>	  	  	</div></div><div class="booklink-footer"></div></div>'
---

<p>「ああ、ここの色はあの部分と同じ色にしよう・・・で、カラーコードは何だっけ」と思いながら、該当箇所を探しまわる。</p>
<p>「ああ、ここの部分はあそこのスタイルを応用して作るか・・・」とスタイルをコピーしてきて、作業中の部分にまた戻ってくる。</p>
<p>すごく・・・<strong>面倒くさい！</strong></p>
<p>スタイルシートを記述していてそんな面倒臭いことを思ったことはないでしょうか。私は<strong>しょっちゅう</strong>です。</p>
<p>ソース中を行ったり来たりとか非常に面倒くさい。スタイルを記述する時間より、行ったり来たりしている時間の方が多いのではないかとさえ思えます。<strong>そんな悩みを解決するのがこのSass</strong>です。</p>
<p>スタイルシートを効率的に記述するためのもので、スタイルシートが書けさえすれば非常にとっつきやすいはず。本書はそんなSassの紹介から、導入方法、活用方法まで非常に分かりやすく教えてくれる良書です。</p>
<h2>非常に入りやすい</h2>
<p>CSSのファイルの拡張子をSCSSにしただけでSassのファイルになります。<em>Sassだからといって何か特殊な記述方法をしなければならないわけではない</em>のです。拡張子がscssになっただけで、中身はCSSのままでも何ら問題ありません（それだけだとSassにする意味は無いですが）。</p>
<p>Sassの便利な機能を知らなくても、自分で少しずつ勉強しながら<em>、使い方がわかったものだけ徐々に試していく</em>なんてこともできます。</p>
<p>環境を構築することが、若干ハードルが高い人もいるかもしれません。そういう人はこの教科書が詳しく説明してくれているので、購入するといいでしょう。</p>
<p>それにネットにSassの情報はたくさんあるし、調べればお金をかけずとも勉強することは可能でしょう。私もこの教科書を買っておきながら、<a href="http://dotinstall.com/" target="_blank">ドットインストール</a>でSassの動画を見て勉強しました。</p>
<p>とりあえず<em>ネストにして記述するだけ</em>、<em>変数を使うだけ</em>といった簡単なところからSassの便利な機能を使っていくといいのではないでしょうか。</p>
<h2>具体例</h2>
<p>例えば、<em>当サイトで利用させて頂いているカエレバブログパーツのスタイルシートの設定</em>です。</p>
<p>私のサイトでは、CSSだとこのようになるものが・・・</p>
<pre><code>.shoplinkamazon , .shoplinkkindle , .shoplinkrakuten , .shoplinkseven , .shoplinkbk1 , .shoplinkkino , .shoplinkehon , .shoplinkyahoo , .shoplinkyahooAuc{
    float: left;
    margin: 5px;
    border: 1px solid #5484D2;
    background-color: #EDF2FA;
}
.shoplinkamazon:hover , .shoplinkkindle:hover , .shoplinkrakuten:hover , .shoplinkseven:hover , .shoplinkbk1:hover , .shoplinkkino:hover , .shoplinkehon:hover , .shoplinkyahoo:hover , .shoplinkyahooAuc:hover{
    background-color: #FAA; 
}
.shoplinkamazon , .shoplinkkindle {
    background-image: url(images/amazon.png);
    background-repeat: no-repeat;
    background-position: 2px 3px;
}
.shoplinkrakuten{
    background-image: url(images/rakuten.png);
    background-repeat: no-repeat;
    background-position: 2px 3px;
}
.shoplinkseven{
    background-image: url(images/7net.png);
    background-repeat: no-repeat;
    background-position: 2px 3px;
}
.shoplinkyahoo , .shoplinkyahooAuc{
    background-image: url(images/yahoo.png);
    background-repeat: no-repeat;
    background-position: 2px 3px;
}
.shoplinkbk1{
    background-image: url(images/bk1.png);
    background-repeat: no-repeat;
    background-position: 2px 3px;
}
.shoplinkehon{
    background-image: url(images/e-hon.png);
    background-repeat: no-repeat;
    background-position: 2px 3px;
}
.shoplinkkino{
    background-image: url(images/kino.png);
    background-repeat: no-repeat;
    background-position: 2px 3px;
}
</code></pre>
<p>Sassを利用すると、以下のようにコンパクトな記述で済みます。</p>
<pre><code>$shoplink-list:amazon,kindle,rakuten,seven,bk1,kino,ehon,yahoo,yahooAuc;
@each $item in $shoplink-list{
    .shoplink#{$item}{
        float: left;
        margin: 5px;
        border: 1px solid $main-accent-color;
        background:url(images/#{$item}.png) $main-color no-repeat 2px 3px;
        &:hover{
                background-color:#faa;
        }
    }
}</code></pre>
<h2>Chrome Developer Toolとの連携</h2>
<p>Chrome Developer toolは、調べたい対象の要素に適用されているプロパティの値を確認したりすることができます。さらに<em>その記載が、スタイルシートの何行目にあるかを確認することもできます</em>。とても便利な機能です。</p>
<p>しかしSCSSにしてしまうと、CSSの行数を表示されても意味がありません。なぜなら、<em>編集するのはSCSSのファイルだから</em>です。便利なはずのSassを導入した結果、どこの記述を直せばよいのかわからなくなり、逆に不便になってしまうではないか。</p>
<p>私も最初そうでしたが、ちゃんと対応策があります。Sourcemapを出力することにより、SCSSファイルでの記述箇所を表示させることができるようになるのです。</p>
<h3>Sassのバージョン3.3以降をインストール</h3>
<p>これはSourcemapの出力をするためには、<em>Sassのバージョン3.3以降でないと対応していない</em>ためです。今のところプレバージョンなので、GUI環境とかで使う場合は使えないかもしれません。</p>
<p>Macの場合は以下のコマンドでインストールしているSassのバージョンをアップデートしましょう。</p>
<pre><code>sudo gem update —system
sudo gem update sass —pre</code></pre>
<p>まだSassをインストールしていない場合は、sudo gem install sass -preでインストールしましょう。（Sassの教科書を見ながらプレバージョンのインストールをすればOK）</p>
<h3>Google Chrome Canaryのインストール</h3>
<p>普通のChromeだと対応していないので、<a href="https://www.google.co.jp/intl/ja/chrome/browser/canary.html" target="_blank">Google Chrome Canary</a>をインストール。</p>
<p>Cmd + Option + iでDeveloper Toolを起動し、歯車のアイコンを押して設定画面を表示。[General] → [Sources] → [Enable CSS Source Maps]にチェックを入れれば準備は完了。</p>
<h3>&#8211;sourcemapオプションを付けてコンパイル</h3>
<p>後はデバッグをしたいScssファイルを、<em>&#8211;sourcemapオプションを付けてコンパイル</em>すればOKです。出力されたCSSファイルをChrome Canaryで表示させれば、<em>Scssファイルでの行数が表示されます</em>。</p>
<p>この環境があればSassでのデザイン作業が捗ります。</p>
<p>ただ、Chromeのインスペクタを使って適用されているスタイルを書き換えてしまうと、表示される行数がCSSのものに変わってしまうのが難点です。再読み込みしたらまたScssの行数を表示してくれるが、もう少し融通効かないかなぁ・・・と思わなくもない。</p>
<h2>取っ付き易く非常に捗る</h2>
<p>Sassを使うことで何が楽になるかといえば、<em>メンテナンスが非常に楽になる</em>ことでしょう。記述する行数が減るということは、その分見やすくなるということです。また、一部のスタイルを変更しようと思った時に、<em>修正する箇所が減る</em>ということでもあります。</p>
<p><em>基本的にCSSと記述方法が変わらない</em>ため、プログラミングを新たに勉強することに比べれば、とても取っ付き易いです。</p>
<p>私も今現在、このサイトで使っているスタイルシートをSassに切り替えている最中なのですが、ちょっとずつ見やすくなっていくのがうれしいです。CSSのままでは記述がごちゃごちゃしていて、とてもではないがデザインの変更などする気が起きませんでした。</p>

  