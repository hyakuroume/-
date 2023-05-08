import webbrowser
import pyperclip
import pyautogui as pag
import time

#webサイトを開いて5秒待機
webbrowser.open("https://www.google.co.jp")
time.sleep(5)

#職員番号、パスワードを定義
num = "339837"
pass_ = "cp339837"

#入力フォームまでマウスカーソルを移動
print(pag.position())
#pag.moveTo()

#職員番号、パスワードを張り付けてEnter
pyperclip.copy(num)
#pag.hotkey("ctrl","v")

print(pag.position())
#pag.moveTo()
pyperclip.copy(pass_)
#pag.hotkey("ctrl","v")

print(pag.position())
#pag.moveTo()
#pag.hotkey("Enter")


