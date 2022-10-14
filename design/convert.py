from PyQt5 import uic

with open("Ui_Registration.py", "w", encoding="utf-8") as fout:
    uic.compileUi("registration.ui", fout)
