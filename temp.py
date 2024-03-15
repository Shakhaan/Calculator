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
