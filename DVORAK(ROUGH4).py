import tkinter as tk

# Define the Dvorak mapping
dvorak_mapping = {
    "q": "'", "w": ",", "e": ".", "r": "p", "t": "y", "y": "f", "u": "g", "i": "c", "o": "r", "p": "l",
    "a": "a", "s": "o", "d": "e", "f": "u", "g": "i", "h": "d", "j": "h", "k": "t", "l": "n", ";": "s",
    "z": ";", "x": "q", "c": "j", "v": "k", "b": "x", "n": "b", "m": "m", ",": "w", ".": "v", "/": "z",
    "backspace": "", "space": " "
}

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.expr = tk.StringVar()
        self.page3 = tk.Frame(self)
        self.page3.pack()

        # Create a custom Entry widget that converts key inputs into Dvorak
        self.e30 = DvorakEntry(self.page3, textvariable=self.expr, width=30, bg="grey", fg="black", border=1, borderwidth=5, cursor="hand1", font=("times new roman", 20, "bold"))
        self.e30.grid(row=5, column=5, sticky=tk.N + tk.W + tk.E + tk.S)

class DvorakEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Bind key press events to the dvorak_conversion function
        self.bind("<Key>", self.dvorak_conversion)

    # Function to convert QWERTY input to Dvorak layout
    def dvorak_conversion(self, event):
        key = event.char
        dvorak_key = self.keyboard_conversion(key)
        self.insert(tk.END, dvorak_key)

    # Function to convert QWERTY input to Dvorak layout
    def keyboard_conversion(self, key):
        if key in dvorak_mapping:
            return dvorak_mapping[key]
        return key

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
