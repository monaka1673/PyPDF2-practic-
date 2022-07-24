# r 読み込み
# with open('./mode.txt',mode='r') as test:
#     s = test.read()
# print(s)

# w 書き込み（新規作成）
# with open('./mode.txt',mode='w') as test:
#     test.write('ddd')

# a 追加書き込み
# with open('./mode.txt',mode='a') as test:
#     test.write('\nddd')

# t テキストモード
# with open('./mode.txt', mode='rt') as f:
#     s = f.read()
# print(s)

# b バイナリモード
with open('./mode.txt', mode='rb') as f:
    s = f.read()
print(s)