import keyboard
import os
import time
import locale
import ctypes

def main():
    rus = is_russian_locale()
    path = get_desktop_path()
    os.startfile("notepad.exe")

    s1 = """    Варкалось. Хливкие шорьки
    Пырялись по наве,
    И хрюкотали зелюки,
    Как мюмзики в мове."""

    s2 = """\n    О, бойся Бармаглота, сын!
    Он так свирлеп и дик!
    А в глу́ше ры́мит исполин —
    Злопастный Брандашмыг!"""

    create_barmaglot_file(s1, path, rus)
    create_new(s2)

def is_russian_locale():
    windll = ctypes.windll.kernel32
    lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

    if (lang == 'ru_RU'):
        return True

    else: 
        return False

def get_desktop_path():
    path = f"{os.environ['USERPROFILE']}\\Desktop"
    if not (os.path.exists(path)):
        path = f"{os.environ['USERPROFILE']}\\Рабочий стол"
    return path

def create_barmaglot_file(s1, path, rus):
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

    if (rus == False):
        keyboard.send("alt+n")
        keyboard.send("alt+shift")
        keyboard.send("alt+n")
    else:
        try:
            keyboard.send("alt+и")
        except ValueError:
            keyboard.send("alt+shift")
            time.sleep(1)
            keyboard.send("alt+b")

    time.sleep(1)
    keyboard.write("barmaglot_file.txt")
    time.sleep(2)
    keyboard.send("enter")
    keyboard.send("enter")
    keyboard.send("enter")
    time.sleep(2)

def create_new(s2):
    keyboard.write(s2)
    keyboard.send("ctrl+shift+s")
    keyboard.write("barmaglot_new_file.txt")
    keyboard.send("enter")
    keyboard.send("alt+f4")

if __name__ == "__main__":
    main()
