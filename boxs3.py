from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout

class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.hbox1.addWidget(self.btn1)
        self.hbox1.addWidget(self.btn2)
        self.hbox2.addWidget(self.btn4)
        self.hbox2.addWidget(self.btn5)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.btn3)        

        self.setLayout(self.vbox)
        self.show()
        

app = QApplication([])
win = Win()
app.exec_()