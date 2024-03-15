from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

app = QApplication([])
oyna = QWidget()

oyna.setWindowTitle("Calculator")
oyna.setGeometry(1400, 500, 240, 310)
oyna.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        color: black;
    }
""")


input = QLineEdit(oyna)
input.setGeometry(0, 0, 240, 60)
input.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: black;
    }
""")
input.setAlignment(Qt.AlignRight)

def birBosildi():
    txt = input.text() + "1"
    input.setText(txt)

def ikkiBosildi():
    txt = input.text() + "2"
    input.setText(txt)

def uchBosildi():
    txt = input.text() + "3"
    input.setText(txt)

def tortBosildi():
    txt = input.text() + "4"
    input.setText(txt)

def beshBosildi():
    txt = input.text() + "5"
    input.setText(txt)

def oltiBosildi():
    txt = input.text() + "6"
    input.setText(txt)

def yettiBosildi():
    txt = input.text() + "7"
    input.setText(txt)

def sakkizBosildi():
    txt = input.text() + "8"
    input.setText(txt)

def toqqizBosildi():
    txt = input.text() + "9"
    input.setText(txt)

def nolBosildi():
    txt = input.text() + "0"
    input.setText(txt)

def plusBosildi():
    txt = input.text()
    if txt[-1] == "+":
        return
    if txt[-1] in ["-", "*", "/"]:
        txt = txt[:-1]
    input.setText(txt + "+")

def minusBosildi():
    txt = input.text()
    if txt[-1] == "-":
        return
    if txt[-1] in ["+", "*", "/"]:
        txt = txt[:-1]
    input.setText(txt + "-")

def bolishBosildi():
    txt = input.text()
    if txt[-1] == "/":
        return
    if txt[-1] in ["-", "*", "+"]:
        txt = txt[:-1]
    input.setText(txt + "/")

def kopaytirishBosildi():
    txt = input.text()
    if txt[-1] == "*":
        return
    if txt[-1] in ["-", "+", "/"]:
        txt = txt[:-1]
    input.setText(txt + "*")

def nuqtaBosildi():
    txt = input.text()
    if txt[-1] == ".":
        return
    if txt[-1] in ["-", "+", "/", "*"]:
        txt = txt[:-1]
    input.setText(txt + ".")


def hisobla():
    txt = input.text()
    natija = str(eval(txt))
    input.setText(natija)

def cBosildi():
    txt = input.text()
    if txt[-1] == "C":
        txt = ""



button1 = QPushButton("1", oyna)
button1.setGeometry(0, 110, 60, 50)
button1.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button2 = QPushButton("2", oyna)
button2.setGeometry(60, 110, 60, 50)
button2.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button3 = QPushButton("3", oyna)
button3.setGeometry(120, 110, 60, 50)
button3.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button4 = QPushButton("4", oyna)
button4.setGeometry(0, 160, 60, 50)
button4.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button5 = QPushButton("5", oyna)
button5.setGeometry(60, 160, 60, 50)
button5.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button6 = QPushButton("6", oyna)
button6.setGeometry(120, 160, 60, 50)
button6.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button7 = QPushButton("7", oyna)
button7.setGeometry(0, 210, 60, 50)
button7.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button8 = QPushButton("8", oyna)
button8.setGeometry(60, 210, 60, 50)
button8.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
button9 = QPushButton("9", oyna)
button9.setGeometry(120, 210, 60, 50)
button9.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")

button0 = QPushButton("0", oyna)
button0.setGeometry(0, 260, 120, 50)
button0.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")
buttonNuqta = QPushButton(".", oyna)
buttonNuqta.setGeometry(120, 260, 60, 50)
buttonNuqta.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: red;
    }
""")

buttonBolish = QPushButton("/", oyna)
buttonBolish.setGeometry(60, 60, 60, 50)
buttonBolish.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: yellow;
    }
""")


buttonKopaytirish = QPushButton("*", oyna)
buttonKopaytirish.setGeometry(120, 60, 60, 50)
buttonKopaytirish.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: yellow;
    }
""")

buttonMinus = QPushButton("-", oyna)
buttonMinus.setGeometry(180, 60, 60, 50)
buttonMinus.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: yellow;
    }
""")


buttonPlus = QPushButton("+", oyna)
buttonPlus.setGeometry(180, 110, 60, 100)
buttonPlus.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: yellow;
    }
""")

buttonSolve = QPushButton("=", oyna)
buttonSolve.setGeometry(180, 210, 60, 100)
buttonSolve.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: yellow;
    }
""")

buttonClear = QPushButton("C", oyna)
buttonClear.setGeometry(0, 60, 60, 50)
buttonClear.setStyleSheet("""
    QPushButton {
        border-radius: 5px;
        border: 1px solid black;
        background-color: yellow;
    }
""")

button1.clicked.connect(birBosildi)
button2.clicked.connect(ikkiBosildi)
button3.clicked.connect(uchBosildi)
button4.clicked.connect(tortBosildi)
button5.clicked.connect(beshBosildi)
button6.clicked.connect(oltiBosildi)
button7.clicked.connect(yettiBosildi)
button8.clicked.connect(sakkizBosildi)
button9.clicked.connect(toqqizBosildi)

button0.clicked.connect(nolBosildi)
buttonMinus.clicked.connect(minusBosildi)
buttonPlus.clicked.connect(plusBosildi)
buttonBolish.clicked.connect(bolishBosildi)
buttonKopaytirish.clicked.connect(kopaytirishBosildi)
buttonNuqta.clicked.connect(nuqtaBosildi)
buttonSolve.clicked.connect(hisobla)
buttonClear.clicked.connect(cBosildi)

oyna.show()
app.exec()
print(app.aboutQt())

