from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QLabel

class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(200,300,400,500)
        self.setStyleSheet("font-size: 30px; color: blue")

        self.label_name = QLabel("Name", self)
        self.label_name.move(10, 100)
        self.label_name.setStyleSheet("font-size: 20px; color: red")

        self.edit = QLineEdit(self)
        self.edit.move(100,97)
        self.edit.setPlaceholderText("Enter name")

        self.btn = QPushButton(self)
        self.btn.setText("Send")
        self.btn.move(145,150)
        self.btn.clicked.connect(self.on_click)
        
        self.show()

    def on_click(self):
        print(self.edit.text())
        self.edit.clear()





app = QApplication([])
win = Win()
app.exec_()