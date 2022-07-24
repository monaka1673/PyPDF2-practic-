# ----
# PDFファイルを読み込んで、ページずつファイルを分割します。
# ----

from csv import reader
import PyPDF2
from os import path

try:
    #① 分割したいファイル名を入力
    input = input('PDFを分割するファイルを入力してください')

    #② 分割したいファイルを読み込みで開く
    with open(input,mode='rb')as fp:
        #③ 分割したいファイルを読み込む
        reader = PyPDF2.PdfFileReader(fp)
        #④ ページ数を取得
        page_num = reader.getNumPages()
        # print(page_num)

        #⑤ １ページずつページ数分読み込む
        for i in range(page_num):
            page = reader.getPage(i)

            #⑥ 分割後のファイル名を作成
            basename = path.basename(input)
            filename,extname = path.splitext(basename)
            newname = "p{}_{}{}".format(i,filename,extname)

            #⑦ 読み込んだページを別のファイルに書き込む
            with open(newname,mode="w+b")as output:
                writer = PyPDF2.PdfFileWriter()
                writer.add_page(page)
                writer.write(output)


finally:
    pass