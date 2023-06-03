# Gigazine crawler
Gigazine `gigazine.net` から記事を収集します。  
Collect articles from the Gigazine `gigazine.net`.

## execution 
```
% python crawling_Gigazine.py
```

カレントディレクトリに３種類のファイル、`xxxxxxxx_xxxxxx_gigazine.jsonl`と、`xxxxxxxx_xxxxxx_gigazine_cwlLog.jsonl`、`xxxxxxxx_xxxxxx_gigazine_html_list.jsonl`が出力されます。  
また、`xxxxxxxx_xxxxxx_html`という名前のフォルダに、収集したhtmlファイルが保存されます。  
（`xxxxxxxx_xxxxxx`には、実行した日付と時刻からユニークな文字列が入ります）  
Three files `xxxxxxxxxxxxxx_gigazine.jsonl`, `xxxxxxxxxxxxxx_gigazine_cwlLog.jsonl` and `xxxxxxxxxxxxxx_gigazine_html _list.jsonl` will be output in the current directory.  
In addition, the collected html files will be saved in a folder named `xxxxxxxxxxxx_xxxxxx_html`.  
(where `xxxxxxxxxxxx_xxxxxxxx` is a unique string from the date and time of execution)

* `xxxxxxxxxxxxxx_gigazine.jsonl`  
記事のURLと記事のテキストデータが保存されます。  
The text data of the article is saved.
* `xxxxxxxxxxxxxx_gigazine_cwlLog.jsonl`  
クロールしたURLと、htmlから抽出した記事のデータ（htmlタグ付きと、テキストデータ）が保存されます。  
The crawled URL and the article data (html tagged and text data) extracted from the html are saved.
* `xxxxxxxxxxxxxx_gigazine_html _list.jsonl`  
`xxxxxxxxxxxx_xxxxxx_html`に保存されているhtmlのファイル名と、収集元のURLが保存されます。  
The file name of the html file stored in `xxxxxxxxxxxxxxxxx_xxxxxxxxx_html` and the URL of the collection source will be saved.
* `xxxxxxxxxxxx_xxxxxx_html`  
収集したhtmlはこのフォルダに保存されます。  
The collected html is stored in this folder.

## Saved data format

### xxxxxxxxxxxxxx_gigazine.jsonl

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows

```
{"url": "https://www....", "text":"Article Data"}
{"url": "https://www....", "text":"Article Data"}
{"url": "https://www....", "text":"Article Data"}
.....
```

Example.
```
{"url": "https://gigazine.net/news/20230531-apple-cloud-my-photo-stream-shuts-down/", "text": "Appleのクラウド写真サービスの「マイフォトストリーム」が今夏終了\n\n2011年にサービスがスタートしたAppleのクラウド写真サービス「マイフォトストリーム」は、2015年に「iCloudフォトライブラリ」が登場するまで、iCloudのクラウド写真サービスとして機能してきました。そんなマイフォトストリームが2023年7月26日にサービス終了することが明らかになっています。\n\nInformation about the My Photo Stream shutdown - Apple Support\nhttps://support.apple.com/en-us/HT210705\n\nApple's 'My Photo Stream' Service Shutting Down in July 2023 - MacRumors\nhttps://www.macrumors.com/2023/05/26/my-photo-stream-july-2023-shutdown/\n\nApple shutting down free ‘My Photo Stream’ feature that originally launched with iCloud - 9to5Mac\nhttps://9to5mac.com/2023/05/26/my-photo-stream-shutdown-icloud/\n\nApple’s original cloud photo sync service shuts down this summer - The Verge\nhttps://www.theverge.com/2023/5/30/23741976/apple-my-photo-stream-discontinued-july-2023\n\nマイフォトストリームは過去30日間分の画像(最大1000枚)を、iCloudにアップロードしてiPhone・iPad・MacといったAppleデバイスから簡単にアクセスできるようにするという無料のクラウド写真サービスです。同機能はiCloudと同時に登場したもので、iCloud写真が登場した際にiCloudフォトライブラリに取って代わられています。\n\nそんなマイフォトストリームのサービスを2023年7月26日に終了すると、Appleがサポートページ上で発表しました。マイフォトストリームのサービス終了に伴い、端末からマイフォトストリームへの写真のアップロードは1カ月前の6月26日で不可能となります。それより以前にアップロードされた写真は、アップロードしてから30日間はiCloudに残ることとなりますが、7月26日以降はiCloud上から完全に削除されてしまうため注意が必要です。\n\nAppleは「マイフォトストリーム内の写真は少なくとも1台のデバイス上にすでに保存されているため、デバイスにオリジナルの写真が保存されている限りは、マイフォトストリームのサービス終了に伴い写真が失われてしまうことはありません。必要な写真が特定のデバイスのライブラリに存在しない場合、必ずそのデバイスのライブラリに保存してください」と説明しています。\n\nただし、Apple関連メディアの9to5Macは「重要なのは、マイフォトストリームは高品質の写真をフル解像度で同期していなかったという点です」と指摘し、マイフォトストリームで共有した写真がアップロードのタイミングで元の解像度から下がっているため、オリジナルの写真をユーザーがダウンロードすることはできないと指摘しました。\n\nなお、iCloudフォトライブラリとマイフォトストリームはどちらもiCloudのクラウド写真サービスですが、マイフォトストリームは「iCloud写真を使用していないiPhone・iPad・Macユーザーが利用できるクラウド写真サービス」であり、iCloud写真を有効にするとマイフォトストリーム機能は完全に非表示になってしまうそうです。\n"}
{"url": "https://gigazine.net/news/20230531-familymart-famichiki-uma-shio/", "text": "ジャンキーさ控えめなあっさり塩味の「ファミチキ 旨塩だれ」を食べてみた\n\nファミリーマートのホットスナック「ファミチキ」に、新たに藻塩を使用した「ファミチキ 旨塩だれ」が2023年5月30日から加わったということなので、買ってきて食べてみました。\n\nファミチキに待望の塩だれ味が新登場 にんにくの旨みとまろやかな塩味 じゅわっと肉汁の「ファミチキ 旨塩だれ」新発売！｜ファミリーマート｜ニュースリリース\nhttps://www.family.co.jp/company/news_releases/2023/20230529_02.html\n\nレジ前のホットスナックコーナーで「ファミチキ(骨なし)」の隣に「ファミチキ 旨塩だれ」が並んでいました。\n\nさっそく買ってきました。\n\n左がノーマルのファミチキ、右がファミチキ 旨塩だれ。衣の色はかなり薄めです。\n\nノーマルのファミチキの断面はこんな感じ。\n\n一方、旨塩だれはこんな感じ。袋から取り出す前からにんにくの香りが漂っていますが、いざ食べてみると、香りほどにはにんにくの風味が効いてる感じはなく、「あっさりとした塩味のファミチキ」という感じ。ノーマルのファミチキにあるジャンキーな感じもほどよくなくなっています。ただ、にんにくが入っていないわけではないので、食べた後にはしっかりとにんにくの匂いがします。\n\n「ファミチキ 旨塩だれ」の価格は税込230円です。\n"}
```


### xxxxxxxxxxxxxx_gigazine_cwlLog.jsonl

１記事につき、１行のJSONフォーマットで保存されます。（JSONLフォーマット）内容は下記の通り。  
One line per article will be saved in JSON format.(JSONL Format) The contents are as follows
```
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
{"url": "https://www......", "contents": ["[Article data with html tags]","[Article data with only text extracted]"]}
.....
```

Example.
```
{"url": "https://gigazine.net/news/20230531-apple-cloud-my-photo-stream-shuts-down/", "contents": ["[<h1 class=\"title\">Appleのクラウド写真サービスの「マイフォトストリーム」が今夏終了</h1>, <p class=\"preface\">\n<br>\n2011年にサービスがスタートしたAppleのクラウド写真サービス「<b><a href=\"https://support.apple.com/ja-jp/HT201317\" target=\"_blank\">マイフォトストリーム</a></b>」は、2015年に「iCloudフォトライブラリ」が登場するまで、iCloudのクラウド写真サービスとして機能してきました。そんなマイフォトストリームが2023年7月26日にサービス終了することが明らかになっています。<br>\n<br/>\n<b>Information about the My Photo Stream shutdown - Apple Support</b><br/>\n<b><a href=\"https://support.apple.com/en-us/HT210705\" target=\"_blank\">https://support.apple.com/en-us/HT210705<br/>\n</a></b></br></br></p>, <p class=\"preface\">\n<br/>\n<b>Apple's 'My Photo Stream' Service Shutting Down in July 2023 - MacRumors</b><br/>\n<b><a href=\"https://www.macrumors.com/2023/05/26/my-photo-stream-july-2023-shutdown/\" target=\"_blank\">https://www.macrumors.com/2023/05/26/my-photo-stream-july-2023-shutdown/</a></b><br/>\n<br/>\n<b>Apple shutting down free ‘My Photo Stream’ feature that originally launched with iCloud - 9to5Mac</b><br/>\n<b><a href=\"https://9to5mac.com/2023/05/26/my-photo-stream-shutdown-icloud/\" target=\"_blank\">https://9to5mac.com/2023/05/26/my-photo-stream-shutdown-icloud/</a></b><br/>\n<br/>\n<b>Apple’s original cloud photo sync service shuts down this summer - The Verge</b><br/>\n<b><a href=\"https://www.theverge.com/2023/5/30/23741976/apple-my-photo-stream-discontinued-july-2023\" target=\"_blank\">https://www.theverge.com/2023/5/30/23741976/apple-my-photo-stream-discontinued-july-2023</a></b><br/>\n<br/>\nマイフォトストリームは過去30日間分の画像(最大1000枚)を、iCloudにアップロードしてiPhone・iPad・MacといったAppleデバイスから簡単にアクセスできるようにするという無料のクラウド写真サービスです。同機能はiCloudと同時に登場したもので、iCloud写真が登場した際にiCloudフォトライブラリに取って代わられています。<br/>\n<br/>\nそんなマイフォトストリームのサービスを2023年7月26日に終了すると、Appleがサポートページ上で発表しました。マイフォトストリームのサービス終了に伴い、端末からマイフォトストリームへの写真のアップロードは1カ月前の6月26日で不可能となります。それより以前にアップロードされた写真は、アップロードしてから30日間はiCloudに残ることとなりますが、7月26日以降はiCloud上から完全に削除されてしまうため注意が必要です。<br/>\n</p>, <p class=\"preface\">\n<br/>\nAppleは「マイフォトストリーム内の写真は少なくとも1台のデバイス上にすでに保存されているため、デバイスにオリジナルの写真が保存されている限りは、マイフォトストリームのサービス終了に伴い写真が失われてしまうことはありません。必要な写真が特定のデバイスのライブラリに存在しない場合、必ずそのデバイスのライブラリに保存してください」と説明しています。<br/>\n<br/>\nただし、Apple関連メディアの9to5Macは「重要なのは、マイフォトストリームは高品質の写真をフル解像度で同期していなかったという点です」と指摘し、マイフォトストリームで共有した写真がアップロードのタイミングで元の解像度から下がっているため、オリジナルの写真をユーザーがダウンロードすることはできないと指摘しました。<br/>\n</p>, <p class=\"preface\">\n<br/>\nなお、iCloudフォトライブラリとマイフォトストリームはどちらもiCloudのクラウド写真サービスですが、マイフォトストリームは「iCloud写真を使用していないiPhone・iPad・Macユーザーが利用できるクラウド写真サービス」であり、iCloud写真を有効にするとマイフォトストリーム機能は完全に非表示になってしまうそうです。<br/>\n</p>]", ["Appleのクラウド写真サービスの「マイフォトストリーム」が今夏終了", "\n2011年にサービスがスタートしたAppleのクラウド写真サービス「マイフォトストリーム」は、2015年に「iCloudフォトライブラリ」が登場するまで、iCloudのクラウド写真サービスとして機能してきました。そんなマイフォトストリームが2023年7月26日にサービス終了することが明らかになっています。\n\nInformation about the My Photo Stream shutdown - Apple Support\nhttps://support.apple.com/en-us/HT210705\n\nApple's 'My Photo Stream' Service Shutting Down in July 2023 - MacRumors\nhttps://www.macrumors.com/2023/05/26/my-photo-stream-july-2023-shutdown/\n\nApple shutting down free ‘My Photo Stream’ feature that originally launched with iCloud - 9to5Mac\nhttps://9to5mac.com/2023/05/26/my-photo-stream-shutdown-icloud/\n\nApple’s original cloud photo sync service shuts down this summer - The Verge\nhttps://www.theverge.com/2023/5/30/23741976/apple-my-photo-stream-discontinued-july-2023\n\nマイフォトストリームは過去30日間分の画像(最大1000枚)を、iCloudにアップロードしてiPhone・iPad・MacといったAppleデバイスから簡単にアクセスできるようにするという無料のクラウド写真サービスです。同機能はiCloudと同時に登場したもので、iCloud写真が登場した際にiCloudフォトライブラリに取って代わられています。\n\nそんなマイフォトストリームのサービスを2023年7月26日に終了すると、Appleがサポートページ上で発表しました。マイフォトストリームのサービス終了に伴い、端末からマイフォトストリームへの写真のアップロードは1カ月前の6月26日で不可能となります。それより以前にアップロードされた写真は、アップロードしてから30日間はiCloudに残ることとなりますが、7月26日以降はiCloud上から完全に削除されてしまうため注意が必要です。\n\nAppleは「マイフォトストリーム内の写真は少なくとも1台のデバイス上にすでに保存されているため、デバイスにオリジナルの写真が保存されている限りは、マイフォトストリームのサービス終了に伴い写真が失われてしまうことはありません。必要な写真が特定のデバイスのライブラリに存在しない場合、必ずそのデバイスのライブラリに保存してください」と説明しています。\n\nただし、Apple関連メディアの9to5Macは「重要なのは、マイフォトストリームは高品質の写真をフル解像度で同期していなかったという点です」と指摘し、マイフォトストリームで共有した写真がアップロードのタイミングで元の解像度から下がっているため、オリジナルの写真をユーザーがダウンロードすることはできないと指摘しました。\n\nなお、iCloudフォトライブラリとマイフォトストリームはどちらもiCloudのクラウド写真サービスですが、マイフォトストリームは「iCloud写真を使用していないiPhone・iPad・Macユーザーが利用できるクラウド写真サービス」であり、iCloud写真を有効にするとマイフォトストリーム機能は完全に非表示になってしまうそうです。\n"]]}
{"url": "https://gigazine.net/news/20230531-familymart-famichiki-uma-shio/", "contents": ["[<h1 class=\"title\">ジャンキーさ控えめなあっさり塩味の「ファミチキ 旨塩だれ」を食べてみた</h1>, <p class=\"preface\">\n<br>\nファミリーマートのホットスナック「<b>ファミチキ</b>」に、新たに藻塩を使用した「<b>ファミチキ 旨塩だれ</b>」が2023年5月30日から加わったということなので、買ってきて食べてみました。<br>\n<br/>\n<b>ファミチキに待望の塩だれ味が新登場 にんにくの旨みとまろやかな塩味 じゅわっと肉汁の「ファミチキ 旨塩だれ」新発売！｜ファミリーマート｜ニュースリリース</b><br/>\n<b><a href=\"https://www.family.co.jp/company/news_releases/2023/20230529_02.html\" target=\"_blank\">https://www.family.co.jp/company/news_releases/2023/20230529_02.html</a></b><br/>\n<br/>\nレジ前のホットスナックコーナーで「ファミチキ(骨なし)」の隣に「ファミチキ 旨塩だれ」が並んでいました。<br/>\n</br></br></p>, <p class=\"preface\">\n<br/>\nさっそく買ってきました。<br/>\n</p>, <p class=\"preface\">\n<br/>\n左がノーマルのファミチキ、右がファミチキ 旨塩だれ。衣の色はかなり薄めです。<br/>\n</p>, <p class=\"preface\">\n<br/>\nノーマルのファミチキの断面はこんな感じ。<br/>\n</p>, <p class=\"preface\">\n<br/>\n一方、旨塩だれはこんな感じ。袋から取り出す前からにんにくの香りが漂っていますが、いざ食べてみると、香りほどにはにんにくの風味が効いてる感じはなく、「あっさりとした塩味のファミチキ」という感じ。ノーマルのファミチキにあるジャンキーな感じもほどよくなくなっています。ただ、にんにくが入っていないわけではないので、食べた後にはしっかりとにんにくの匂いがします。<br/>\n</p>, <p class=\"preface\">\n<br/>\n「ファミチキ 旨塩だれ」の価格は税込230円です。<br/>\n</p>]", ["ジャンキーさ控えめなあっさり塩味の「ファミチキ 旨塩だれ」を食べてみた", "\nファミリーマートのホットスナック「ファミチキ」に、新たに藻塩を使用した「ファミチキ 旨塩だれ」が2023年5月30日から加わったということなので、買ってきて食べてみました。\n\nファミチキに待望の塩だれ味が新登場 にんにくの旨みとまろやかな塩味 じゅわっと肉汁の「ファミチキ 旨塩だれ」新発売！｜ファミリーマート｜ニュースリリース\nhttps://www.family.co.jp/company/news_releases/2023/20230529_02.html\n\nレジ前のホットスナックコーナーで「ファミチキ(骨なし)」の隣に「ファミチキ 旨塩だれ」が並んでいました。\n\nさっそく買ってきました。\n\n左がノーマルのファミチキ、右がファミチキ 旨塩だれ。衣の色はかなり薄めです。\n\nノーマルのファミチキの断面はこんな感じ。\n\n一方、旨塩だれはこんな感じ。袋から取り出す前からにんにくの香りが漂っていますが、いざ食べてみると、香りほどにはにんにくの風味が効いてる感じはなく、「あっさりとした塩味のファミチキ」という感じ。ノーマルのファミチキにあるジャンキーな感じもほどよくなくなっています。ただ、にんにくが入っていないわけではないので、食べた後にはしっかりとにんにくの匂いがします。\n\n「ファミチキ 旨塩だれ」の価格は税込230円です。\n"]]}
```

### xxxxxxxxxxxxxx_gigazine_html _list.jsonl

`xxxxxxxxxxxx_xxxxxx_html`に保存されているhtmlのファイル名と、収集元のURLがJSONL形式で保存されます。  
The html file name stored in `xxxxxxxxxxxxxxxxx_xxxxxxxxx_html` and the URL of the collection source will be saved in JSONL format.

```
{"filename": "xxxxx_gigazine_article.html", "url": "https://www......."}
{"filename": "xxxxx_gigazine_article.html", "url": "https://www......."}
{"filename": "xxxxx_gigazine_article.html", "url": "https://www......."}
.....
```

Example.
```
{"filename": "00001_gigazine_article.html", "url": "https://ameblo.jp/kumikotakeda/entry-12805291014.html"}
{"filename": "00002_gigazine_article.html", "url": "https://ameblo.jp/kawata--hiromi/entry-12805341645.html"}
{"filename": "00003_gigazine_article.html", "url": "https://ameblo.jp/hiranonora/entry-12805304197.html"}
```

### xxxxxxxxxxxx_xxxxxx_html

収集したhtmlはこのフォルダに保存されます。  
The collected html is stored in this folder.

個々のファイルの名前は５桁の数字の後に`_gigazine_article.html`を付けたものになります。  
The name of each individual file will be a five-digit number followed by `_gigazine_article.html`.