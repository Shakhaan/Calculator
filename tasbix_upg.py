import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton,
    QLabel,
    QLineEdit
)

class Button(QPushButton):
    def __init__(self, text) -> None:
        super().__init__(text)
        self.setFixedSize(100,80)
        self.setStyleSheet('background: #176B87; font-size:30px; border-radius: 25px; padding: 10px 0px; border: 2px solid black')

class Edit(QLineEdit):
    def __init__(self, text) -> None:
        super().__init__(text)
        self.setStyleSheet('background: #fff; font-size:30px; border-radius: 10px; border: 2px solid black; padding: 0px 10px;')
        self.setAlignment(QtCore.Qt.AlignCenter) 


class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Tasbix')
        self.setFixedSize(300,300)
        self.setStyleSheet('background: #64CCC5')

        self.count = 0
        self.index = 0
        self.zikrlar = ('SubhanAlloh', 'Alhamdulillah', 'AllohuAkbar')
        self.on = False

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.label_zikr = QLabel()
        self.v_box.addWidget(self.label_zikr)

        self.edit_display = Edit("")
        self.v_box.addWidget(self.edit_display)

        self.btn_mode = Button('power')
        self.h_box.addWidget(self.btn_mode)

        self.h_box.addStretch()

        self.btn_reset = Button('reset')
        self.h_box.addWidget(self.btn_reset)

        self.v_box.addLayout(self.h_box)

        self.btn_count = QPushButton('📿')
        self.btn_count.setEnabled(False)
        self.v_box.addWidget(self.btn_count)

        self.setLayout(self.v_box)

        self.btn_count.clicked.connect(self.on_press)
        self.btn_mode.clicked.connect(self.on_off)
        self.btn_reset.clicked.connect(self.reset_display)

        self.show()

        
    def on_press(self):

        if self.on:
            if self.count == 33:
                self.count = 0
                self.index+=1
                self.label_zikr.setText(self.zikrlar[self.index%3])
            self.count+=1
            self.edit_display.setText(str(self.count))

    def on_off(self):
        self.on = not self.on
        if self.on:
            self.label_zikr.setText(self.zikrlar[self.index])
            self.edit_display.setText(str(self.count))
            self.btn_count.setEnabled(True)

        else:
            self.label_zikr.setText('')
            self.edit_display.setText('')
            self.count = 0
            self.index = 0
            self.btn_count.setEnabled(False)

    def reset_display(self):
        self.count = 0
        self.index = 0
        self.label_zikr.setText(self.zikrlar[self.index])
        self.edit_display.setText(str(self.count))
        




app = QApplication(sys.argv)

win = Win()

sys.exit(app.exec_())