# ----
# PDFファイルを読み込んで、ファイルの情報をコンソールに表示します。
# ----

# ① PyPDFをインポート
import PyPDF2

try:
    # ② ファイル名をコンソールから入力
    filename = input('ファイル名を入力してください。')

    # ③ 指定されたファイルを開いて、先頭ページの情報を表示
    with open(filename, mode='rb') as fp:
        reader = PyPDF2.PdfFileReader(fp)
        print("filename={}を読み込みました。".format(filename))

        #④ ページ数を取得してコンソールに表示
        page_num = reader.getNumPages()
        print("このファイルは{}ページあります。".format(page_num))

        #⑤ テキストを取得してコンソールに表示
        page = reader.getPage(page_num - 1)
        text = page.extractText()
        print("1ページ目のテキストは次のとおりです")
        print(text)

except OSError as e:
    print(e)

