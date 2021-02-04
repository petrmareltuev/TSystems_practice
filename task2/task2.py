import keyboard
import os
import time

os.startfile("notepad.exe")
english = False

path = f"{os.environ['USERPROFILE']}\\Desktop"
if (os.path.exists(path)):
    english = True
else:
    path = f"{os.environ['USERPROFILE']}\\Рабочий стол"

s1 = """Варкалось. Хливкие шорьки
Пырялись по наве,
И хрюкотали зелюки,
Как мюмзики в мове."""

s2 = """\nО, бойся Бармаглота, сын!
Он так свирлеп и дик!
А в глу́ше ры́мит исполин —
Злопастный Брандашмыг!"""

time.sleep(2)
keyboard.write(s1)
keyboard.send("ctrl+shift+s")
time.sleep(2)
keyboard.send("f4")
time.sleep(1)
keyboard.send("ctrl+a")
keyboard.write(path)
keyboard.send("enter")
time.sleep(1)
keyboard.send("tab")
time.sleep(1)
keyboard.send("esc")
time.sleep(1)
if (english == True):
    keyboard.send("alt + n")
else:
    try:
        keyboard.send("alt+и")
    except ValueError:
        keyboard.send("alt+shift")
        keyboard.send("alt+и")

time.sleep(2)
keyboard.write("barmaglot_file.txt")
time.sleep(2)
keyboard.send("enter")
keyboard.send("enter")
keyboard.send("enter")
time.sleep(2)

keyboard.write(s2)
keyboard.send("ctrl+shift+s")
keyboard.write("barmaglot_new_file.txt")
keyboard.send("enter")
keyboard.send("alt+f4")