from PyQt5 import uic

with open("Ui_main_admin.py", "w", encoding="utf-8") as fout:
    uic.compileUi("main_admin.ui", fout)
