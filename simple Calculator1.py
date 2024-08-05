import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("400x600")
        self.configure(bg="lightgray")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self, bg="lightgray")
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=("Arial", 24), justify='right', bd=10, bg="white")
        input_field.pack(expand=True, fill="both")

        buttons_frame = tk.Frame(self, bg="lightgray")
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            '7', '8', '9', 'C',
            '4', '5', '6', '/',
            '1', '2', '3', '*',
            '0', '.', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            button = tk.Button(buttons_frame, text=button, font=("Arial", 18), bd=1, fg="black", bg="white", command=action)
            button.grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            buttons_frame.grid_rowconfigure(i, weight=1)
            buttons_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set(self.expression)
        elif button == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += button
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
