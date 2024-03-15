from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.collection = ""

        self.display = QLineEdit("0")

        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn0 = QPushButton("0")
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_divide = QPushButton("/")
        self.btn_multiply = QPushButton("*")
        self.btn_equal = QPushButton("=")
        self.btn_clear = QPushButton("C")

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.hbox1.addWidget(self.btn1)
        self.hbox1.addWidget(self.btn2)
        self.hbox1.addWidget(self.btn3)
        self.hbox1.addWidget(self.btn_plus)

        self.hbox2.addWidget(self.btn4)
        self.hbox2.addWidget(self.btn5)
        self.hbox2.addWidget(self.btn6)
        self.hbox2.addWidget(self.btn_minus)

        self.hbox3.addWidget(self.btn7)
        self.hbox3.addWidget(self.btn8)
        self.hbox3.addWidget(self.btn9)
        self.hbox3.addWidget(self.btn_multiply)

        self.hbox4.addWidget(self.btn0)
        self.hbox4.addWidget(self.btn_equal)
        self.hbox4.addWidget(self.btn_clear)
        self.hbox4.addWidget(self.btn_divide)

        self.vbox.addWidget(self.display)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        self.setLayout(self.vbox)
        self.show()

        self.btn1.clicked.connect(self.on_click)
        self.btn2.clicked.connect(self.on_click)
        self.btn3.clicked.connect(self.on_click)
        self.btn4.clicked.connect(self.on_click)
        self.btn5.clicked.connect(self.on_click)
        self.btn6.clicked.connect(self.on_click)
        self.btn7.clicked.connect(self.on_click)
        self.btn8.clicked.connect(self.on_click)
        self.btn9.clicked.connect(self.on_click)
        self.btn0.clicked.connect(self.on_click)
        self.btn_plus.clicked.connect(self.on_click)
        self.btn_minus.clicked.connect(self.on_click)
        self.btn_divide.clicked.connect(self.on_click)
        self.btn_multiply.clicked.connect(self.on_click)
        self.btn_equal.clicked.connect(self.evaluate)
        self.btn_clear.clicked.connect(self.clear_display)

    def on_click(self):
        text = self.sender().text()
        self.collection += text
        self.display.setText(self.collection)

    def clear_display(self):
        self.collection = ""
        self.display.setText("0")

    def evaluate(self):
        try:
            result = eval(self.collection)
            self.display.setText(str(result))
            self.collection = str(result)
        except Exception as e:
            self.display.setText("Error")

app = QApplication([])
win = Win()
app.exec_()
