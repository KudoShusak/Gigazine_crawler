import re
import requests
import time
import os
from datetime import datetime
import json
from bs4 import BeautifulSoup

# クローリングを開始するURL
start_url = "https://gigazine.net/"

prefix = '{:%Y%m%d_%H%M%S}_'.format(datetime.now())

# クローリング結果保存ファイル
result_file = f"{prefix}gigazine_cwlLog.jsonl"

# テキストデータ保存ファイル
text_file = f"{prefix}gigazine.jsonl"

# 取得したhtmlのリストを保存するファイル
logfile = f"{prefix}gigazine_html_list.jsonl"

# htmlファイルの名前
sub_filename = "_gigazine_article.html"

# htmlファイルを保存するディレクトリ（フォルダ）
directory = f'{prefix}html'
os.mkdir(directory)

#### テキスト抽出 ####
def gettext(soup):

    txthtmllist = []
    txtlist = []

    article = soup.find('div', class_='cntimage')

    # 記事名
    title = article.find('h1', class_='title')
    txthtmllist.append(title)
    txtlist.append(title.text)

    # 本文
    bodytxtlist = []
    # <p>タグのclassが'preface'のテキストを抽出
    for paragraph in article.find_all('p', class_='preface'):
        if paragraph.text != "" :
            txthtmllist.append(paragraph)
            bodytxtlist.append(paragraph.text)

    # 各paragraphを改行で連結
    bodytxt = '\n'.join(bodytxtlist)
    # 段落の切れ目に入る空行が1行になるように調整
    bodytxt = re.sub('\n[\n]+','\n\n', bodytxt)
    # 本文の先頭と最後にある無駄な改行は1つにまとめる
    bodytxt = re.sub('^[\n]+|[\n]+$','\n', bodytxt)

    txtlist.append(bodytxt)

    return [txthtmllist,txtlist]

#### JSONL形式で保存 ####

# save_dataをJSON形式でresult_fileに追記する。
def save_result(cont_txt, url="None", filename=result_file):

    save_data = {"url":url, "contents": [str(cont_txt[0]), cont_txt[1]]}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

# テキストデータのlistを指定の形式でtext_fileに追記する
def save_text(textlist, url="None", filename=text_file):

    jointxt = '\n'.join(textlist)
    save_data = {"url" : url, "text" : jointxt}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

#### クローリング ####

# アクセスするURL(初期値はクローリングを開始するURL)
url = start_url
urllist = [url]

# クロール済みリスト
crawledlist = []

count = 0
for i in range(8):
    print(f'{i + 1}階層目クローリング開始')

    linklist = []
    # 対象ページのhtml取得
    for url in urllist:
        #　同じURLを何度もクロールしない
        if url in crawledlist:
            continue

        time.sleep(3) # データ取得前に少し待つ

        try:
            html = requests.get(url)
            soup = BeautifulSoup(html.content, "html.parser")
            # 次のループで使うURLの候補として<a>タグのリストをため込む

            linklist.extend(soup.find_all("a"))

            ## テキスト抽出

            if 'gigazine.net/news/2' in url :
                count += 1

                cont_txt = gettext(soup)
                save_result(cont_txt, url=url, filename = result_file)
                save_text(cont_txt[1], url=url, filename = text_file)
                print(count, cont_txt[1])

                # 取得したhtmlをファイルに保存
                filename = str(count).zfill(5) + sub_filename
                filepath = os.path.join(directory,filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(html.text))
                f.close()

                # ファイル名とurlのセットを記録しておく
                logdata = {'filename': filename, 'url': url}
                with open(logfile, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(logdata)+'\n')
                f.close()

        except:
            # 何かエラーが出てもとりあえず続ける
            print(f'Error: {url}')
            continue

    # 使い終わったurllistをクロール済みリストに追加
    crawledlist.extend(urllist)
    crawledlist = list(set(crawledlist)) # 重複削除

    # 次のループのためのurllistを作る
    urllist = []
    for link in linklist:
        # 取得した<a>タグのリストから、記事であることを期待して"/news/"が含まれているURLを取得
        for url in re.findall('<a.+?href="(.+?/news/.+?)".*?>', str(link)):
            # 同じ記事を何度もクロールしないように'?'と'#'の後の文字列を削除
            url = re.sub('[?#].+','',url)
            # 先頭が'/'の場合は、'https://gigazine.net'を追加
            if url[0] == '/' :
                url = f'https://gigazine.net{url}'
            if 'gigazine.net' in url :
                urllist.append(url)

    urllist = list(set(urllist)) # 重複削除
