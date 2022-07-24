# ----
# PDFファイルを読み込んで、ファイルのメタ情報をコンソールに表示します。
# ----

# ① PyPDFをインポート
import PyPDF2

try:
    # ② ファイル名をコンソールから入力
    filename = input('ファイル名を入力してください。')

    # ③ 指定されたファイルを開いて、先頭ページのメタデータを表示
    with open(filename,mode='rb') as fp:
        reader = PyPDF2.PdfFileReader(fp)
        info = reader.getDocumentInfo()
        print(info)

except OSError as e:
    print(e)