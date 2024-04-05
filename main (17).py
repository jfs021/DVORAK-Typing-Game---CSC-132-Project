#Jillian Sisson
#IMPORTS
from tkinter import *

#CALCULATRON CLASS
class Calculatron(Frame):

    def __init__(self, master):

        '''
        The initialization
        Inherits from Frame
        Calls setupLayout function
        '''

        Frame.__init__(self, master, bg = "white")
        self.setupLayout()

    def setupLayout(self):

        '''
        The layout of the calculator
        Uses images from given file
        Calls process function
        '''

        self.display = Label(self, text = "", anchor = E, bg = "white", height = 2, width = 15, font = ("Arial", 39))
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = E + W + N + S)

        for row in range(7):
            Grid.rowconfigure(self, row, weight = 1)

        for col in range(4):
            Grid.columnconfigure(self, col, weight = 1)

        img = PhotoImage(file = "images/lpr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("("))
        button.image = img
        button.grid(row = 1, column = 0, sticky = N + S + E + W)

        img = PhotoImage(file = "images/rpr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process(")"))
        button.image = img
        button.grid(row = 1, column = 1, sticky = N + S + E + W)

        img = PhotoImage(file = "images/clr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("AC"))
        button.image = img
        button.grid(row = 1, column = 2, sticky = N + S + E + W)

        img = PhotoImage(file = "images/bak.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("BACK"))
        button.image = img
        button.grid(row = 1, column = 3, sticky = N + S + E + W)

        img = PhotoImage(file = "images/7.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("7"))
        button.image = img
        button.grid(row = 2, column = 0, sticky = N + S + E + W)

        img = PhotoImage(file = "images/8.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("8"))
        button.image = img
        button.grid(row = 2, column = 1, sticky = N + S + E + W)

        img = PhotoImage(file = "images/9.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("9"))
        button.image = img
        button.grid(row = 2, column = 2, sticky = N + S + E + W)

        img = PhotoImage(file = "images/div.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("/"))
        button.image = img
        button.grid(row = 2, column = 3, sticky = N + S + E + W)

        img = PhotoImage(file = "images/4.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("4"))
        button.image = img
        button.grid(row = 3, column = 0, sticky = N + S + E + W)

        img = PhotoImage(file = "images/5.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("5"))
        button.image = img
        button.grid(row = 3, column = 1, sticky = N + S + E + W)

        img = PhotoImage(file = "images/6.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("6"))
        button.image = img
        button.grid(row = 3, column = 2, sticky = N + S + E + W)

        img = PhotoImage(file = "images/mul.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("*"))
        button.image = img
        button.grid(row = 3, column = 3, sticky = N + S + E + W)

        img = PhotoImage(file = "images/1.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("1"))
        button.image = img
        button.grid(row = 4, column = 0, sticky = N + S + E + W)

        img = PhotoImage(file = "images/2.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("2"))
        button.image = img
        button.grid(row = 4, column = 1, sticky = N + S + E + W)

        img = PhotoImage(file = "images/3.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("3"))
        button.image = img
        button.grid(row = 4, column = 2, sticky = N + S + E + W)

        img = PhotoImage(file = "images/sub.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("-"))
        button.image = img
        button.grid(row = 4, column = 3, sticky = N + S + E + W)

        img = PhotoImage(file = "images/0.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("0"))
        button.image = img
        button.grid(row = 5, column = 0, sticky = N + S + E + W)

        img = PhotoImage(file = "images/dot.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("."))
        button.image = img
        button.grid(row = 5, column = 1, sticky = N + S + E + W)

        img = PhotoImage(file = "images/pow.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("**"))
        button.image = img
        button.grid(row = 5, column = 2, sticky = N + S + E + W)

        img = PhotoImage(file = "images/add.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("+"))
        button.image = img
        button.grid(row = 5, column = 3, sticky = N + S + E + W)

        #I didn't like how the blank "button" looked, so I centered the equal sign over three columns
        #I still don't love it, but I like it better than just the blank area
        img = PhotoImage(file = "images/eql-wide.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("="))
        button.image = img
        button.grid(row = 6, column = 0, columnspan = 3, sticky = N + S + E + W)

        img = PhotoImage(file = "images/mod.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda: self.process("%"))
        button.image = img
        button.grid(row = 6, column = 3, sticky = N + S + E + W)

        self.pack(fill = BOTH, expand = 1)

    def process(self, button):

        '''
        Displays things based on buttons pressed
        Evaluates expressions in the label and truncates answers over 14 characters long
        Checks for errors
        '''

        if (self.display["text"] == "ERROR"):
            self.display["text"] = ""
            self.process(button)

        else:
            if (button == "AC"):
                self.display["text"] = ""

            elif (button == "BACK"):
                displayChar = self.display ["text"]
                oneGone = displayChar[:-1]
                self.display["text"] = oneGone

            elif (button == "="):
                expr = self.display["text"]

                try:
                    result = eval(expr)
                    result = str(result)

                    if (len(result) > 14):
                        result = result[0:11]
                        result += "..."

                    self.display["text"] = str(result)

                except:
                    self.display["text"] = "ERROR"

            else:
                self.display["text"] += button

#MAIN
window = Tk()

window.title("The Reckoner")

P = Calculatron(window)

window.mainloop()