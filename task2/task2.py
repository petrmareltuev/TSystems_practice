import keyboard
import os
import time

os.startfile("notepad.exe")

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
keyboard.send("ctrl+s")
keyboard.write("barmaglot_file.txt")
keyboard.send("f4")

for i in range(40): 
	keyboard.send("backspace")

keyboard.write("Рабочий стол")
keyboard.send("enter")
keyboard.send("enter")
keyboard.send("enter")
keyboard.send("enter")

keyboard.write(s2)
keyboard.send("ctrl+shift+s")
keyboard.write("barmaglot_new_file.txt")
keyboard.send("enter")
keyboard.send("alt+f4")
