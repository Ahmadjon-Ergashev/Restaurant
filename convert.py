from PyQt5 import uic

with open("login.py", "w", encoding="utf-8") as fout:
    uic.compileUi("./design/login.ui", fout)
