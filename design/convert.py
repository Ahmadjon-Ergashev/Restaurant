from PyQt5 import uic

with open("Ui_main_user.py", "w", encoding="utf-8") as fout:
    uic.compileUi("main_user.ui", fout)
