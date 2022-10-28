from PyQt5 import uic

with open("Ui_Update_password.py", "w", encoding="utf-8") as fout:
    uic.compileUi("update_password.ui", fout)
