import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(100, 100, 300, 300)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        buttons = [
            ("7", self.on_button_clicked),
            ("8", self.on_button_clicked),
            ("9", self.on_button_clicked),
            ("/", self.on_button_clicked),
            ("4", self.on_button_clicked),
            ("5", self.on_button_clicked),
            ("6", self.on_button_clicked),
            ("*", self.on_button_clicked),
            ("1", self.on_button_clicked),
            ("2", self.on_button_clicked),
            ("3", self.on_button_clicked),
            ("-", self.on_button_clicked),
            ("0", self.on_button_clicked),
            (".", self.on_button_clicked),
            ("=", self.on_equals_clicked),
            ("+", self.on_button_clicked),
            ("C", self.clear_display)
        ]

        for text, slot in buttons:
            button = QPushButton(text)
            button.clicked.connect(slot)
            self.layout.addWidget(button)

        self.setLayout(self.layout)

    def on_button_clicked(self):
        button = self.sender()
        self.result_display.setText(self.result_display.text() + button.text())

    def on_equals_clicked(self):
        try:
            result = eval(self.result_display.text())
            self.result_display.setText(str(result))
        except Exception as e:
            self.result_display.setText("Hata")

    def clear_display(self):
        self.result_display.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30)
        self.display.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create and place buttons
        r = 1
        c = 0
        for btn in self.buttons:
            tk.Button(master, text=btn, width=5, command=lambda char=btn: self.button_click(char)).grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def button_click(self, char):
        if char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
