# ----
# PDFファイルを2つ読み込んで、１つのPDFファイルにマージします。
# ----

from fileinput import filename
import PyPDF2

merger = None
try:
    #① 結合したいファイル名を２つ入力
    filename1 = input("PDFを結合するファイルを入力してください")
    filename2 = input("PDFを結合するファイルを入力してください")
    
    #② PDF結合用のインスタンスを作成
    merger = PyPDF2.PdfFileMerger(strict=False)

    #③ インスタンスにappendメソッドを使ってPDFデータを追加
    merger.append(filename1)
    merger.append(filename2)

    #④ 結合したPDFの保存
    merger.write('sample_merge.pdf')
finally:
    merger.close()