from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QLabel, QVBoxLayout, QHBoxLayout

class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.setGeometry(200,300,400,500)
        self.setStyleSheet("font-size: 30px; color: blue")

        self.label_name = QLabel("Name")
        self.label_name.setStyleSheet("font-size: 20px; color: red")

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Enter name")

        self.btn = QPushButton("Send")
        self.btn.clicked.connect(self.on_click)

        self.vbox = QHBoxLayout()
        self.vbox.addWidget(self.label_name)
        self.vbox.addWidget(self.edit)
        self.vbox.addWidget(self.btn)

        self.setLayout(self.vbox)        
        self.show()

    def on_click(self):
        print(self.edit.text())
        self.edit.clear()


app = QApplication([])
win = Win()
app.exec_()