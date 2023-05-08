#! python3
# bulletPointAdder.py - クリップボードのテキストの各行に
# 点を打って、Wikipediaの箇条書きにする

import pyperclip
text = pyperclip.paste()

# TODO:行を分割して、'*'を追加する
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)S

pyperclip.copy(text)
