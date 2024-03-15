from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout

class Tasbix(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.count = 0
        self.index = 0
        self.zikrlar = ("SubhanAlloh", "Alhamdulillah", "Allohu Akbar")

        self.setWindowTitle("Elektron Tasbix")
        self.setStyleSheet("font-size:25px")
        self.setFixedSize(200,250)
        self.vbox = QVBoxLayout()

        self.zikr_label = QLabel(self.zikrlar[self.index])

        self.edit_count = QLineEdit(str(self.count))

        self.btn_count = QPushButton("📿")

        self.vbox.addWidget(self.zikr_label)
        self.vbox.addWidget(self.edit_count)
        self.vbox.addWidget(self.btn_count)

        self.setLayout(self.vbox)
        self.show()

        self.btn_count.clicked.connect(self.on_press)

    def on_press(self):
        self.count+=1
        self.edit_count.setText(str(self.count)) 
        if self.count == 33:
            self.count = 0
            self.index+=1
            self.zikr_label.setText(self.zikrlar[self.index%3])

app = QApplication([])
win = Tasbix()
app.exec_()