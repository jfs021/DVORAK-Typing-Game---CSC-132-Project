from tkinter import *
from customtkinter import *
from fiveLetter import * 
from threeLetter import *
from sevenLetter import *
from random import *
from time import *
from functools import reduce

class ResultScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        #self.words = []
        self.num_of_letters = 0
        self.start_time = 0
        self.done_time = 0
        self.load_pages()
    def load_pages(self):
        global expr
        expr = StringVar()
        self.page1 = Frame(self.master, bg ="black", border= 1, borderwidth= 300)
        self.page1.grid(row = 0, column = 0, sticky= W + E )
        self.page2 = Frame(self.master,bg ="black", border= 1, borderwidth= 300)
        self.page2.grid(row = 0, column = 0, sticky= N +W + E + S )
        self.page3 = Frame(self.master, bg ="black", border= 1, borderwidth= 300)
        self.page3.grid(row = 0, column = 0, sticky= N +W + E + S)
        self.page4 =Frame(self.master, bg ="black", border= 1, borderwidth= 300)
        self.page4.grid(row=0, column=0, sticky= N +W + E + S)
        # setting up page 1
        self.l10 = Label(self.page1, bg = "Black" , fg="White", text= "Welcome to Speed Typing Program", font=("times new roman", 30, "bold"))
        self.l10.grid(column = 0, row=0)
        self.l11= Label(self.page1, bg = "Black", width=10, height=10)
        self.l11.grid(column = 0, row=1)
        self.b10 = Button(self.page1, bg = "Indigo",fg="BLACK",text = "Start", activebackground="turquoise", activeforeground="WHITE",
                           width=13, height=5, border=1,borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"), command = lambda:self.SetUpFirstPage())
        self.b10.grid(column= 0, row= 2)
       

        # setting up page 2
        self.b20 = Button(self.page2, text= " 5 letter words", bg = "magenta",fg="BLACK",activebackground="turquoise", activeforeground="WHITE",
                           width=10, height=2, border=1, borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"), command = lambda:self.ImportFive() )
        self.b20.grid(row = 2, column =5, sticky= N + W + E + S )
        self.b22 = Button(self.page2,text="3 letter words", bg = "pink",fg="BLACK",activebackground="turquoise", activeforeground="WHITE",
                           width=10, height=2, border=1,borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"), command=lambda:self.ImportThree() )
        self.b22.grid(row=0, column=5, sticky= N + W + E + S)
        self.b23 = Button(self.page2, text= " 7 letter words", bg = "Indigo",fg="BLACK",activebackground="turquoise", activeforeground="WHITE",
                           width=1, height=2, border=1,borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"),command=lambda:self.ImportSeven())
        self.b23.grid(row=4,column=5, sticky= N + W + E + S )
   
        # setting up page 3
        self.e30 = Entry(self.page3, textvariable = expr, width= 30, bg = "grey",fg="BLACK", border=1, borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"))
        self.e30.grid(row= 5, column= 5, sticky = N + W + E + S)
        self.b31 = Button(self.page3, text = "done",bg = "Indigo",fg="BLACK",activebackground="turquoise", activeforeground="WHITE",
                           width=10, height=2, border=1, borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"), command = lambda:self.CheckInput())
        self.b31.grid(row= 7, column = 5, sticky = N + W + E + S )

        # setting up for page 4
        self.b40 = Button(self.page4, text = "Restart", bg = "Indigo",fg="BLACK",activebackground="turquoise", activeforeground="WHITE",
                           width=10, height=2, border=1,borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"), command = lambda:self.restart())
        self.b40.grid(row = 0, column=5, sticky = N + W + E + S)
        self.l40 = Label(self.page4, text = "WPM ", bg = "Magenta",fg="BLACK",activebackground="turquoise", activeforeground="WHITE",
                           width=10, height=2, border=1,borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"))
        self.l40.grid(row = 1, column=5, sticky = N + W + E + S)
        self.l41 = Label(self.page4,text= "Accuracy ", bg = "pink",fg="BLACK",activebackground="turquoise", activeforeground="WHITE",
                           width=10, height=2, border=1,borderwidth= 5, cursor="hand1", font=("times new roman", 20, "bold"))
        self.l41.grid(row = 2, column = 5, sticky = N + W + E + S)
        # the start/Welcome page will be the first thing the user sees/ it includes the START button
        self.page1.tkraise()
    
    # fisrt page : it's a page where 
    def SetUpFirstPage(self):
        # generates random 
        self.page2.tkraise()

    def ImportFive(self):
        self.words = sample(five_letters_words, 100)
        string = ""
        n = 10
        while n <= len(self.words):
            for i in range(n-10, n):
                string += self.words[i] + " "    
            string += "\n"
            n += 10
        self.l3 = Label(self.page3, text = string, bg = "magenta",fg="BLACK", font=("times new roman", 15, "bold"))
        self.l3.grid(row=2, column= 5, sticky= N + W + E + S )
        self.start_time = time()
        self.page3.tkraise() 
        print(self.start_time)
        return self.words 
    
    def ImportThree(self):
        self.words = sample(three_letter_words, 100)
        string = ""
        n = 10
        while n <= len(self.words):
            for i in range(n-10, n):
                string += self.words[i] + " "    
            string += "\n"
            n += 10
        self.l3 = Label(self.page3, text = string, bg = "magenta",fg="BLACK", font=("times new roman", 15, "bold"))
        self.l3.grid(row=1, column= 5, sticky= N + W + E + S )
        self.start_time = time()
        self.page3.tkraise() 
        print(self.start_time)
        return self.words 
    
    def ImportSeven(self):
        self.words = sample(seven_letter_words, 100)
        string = ""
        n = 10
        while n <= len(self.words):
            for i in range(n-10, n):
                string += self.words[i] + " "    
            string += "\n"
            n += 10
        self.l3 = Label(self.page3, text = string, bg = "magenta",fg="BLACK", font=("times new roman", 15, "bold"))
        self.l3.grid(row=1, column= 5, sticky= N + W + E + S )
        self.start_time = time()
        self.page3.tkraise() 
        print(self.start_time)
        return self.words 

    def CheckInput(self):
        self.done_time = time()
        print(self.done_time)
        words = reduce(lambda x, y:x+" "+y, self.words)
        self.inputs = str(self.e30.get())
        print(self.inputs)
        print(words)
        score = 0
        for letter in range(len(self.inputs)):
                if self.inputs[letter] == (words[letter]):
                    score += 1
        print(score)
        self.l41["text"] += f"{round((score /len(words))*100)} %"
        self.l40["text"] += f"({self.callculate_WPM()}l)"
        self.page4.tkraise()

    def callculate_WPM(self):
        time_spent = round(self.done_time - self.start_time, ) 
        print(f"{time_spent}")
        WPM = round(len(self.inputs.split()))/round(time_spent / 60, 2)
        return WPM 

    def restart(self):
        expr.set("")
        self.l41["text"] = "Accuracy: "
        self.l40["text"] = "WPM:  "
        self.l3["text"] = " "
        self.page1.tkraise()            
                    
#main
win1 = CTk() 
win1.geometry("1200x900")
win1.resizable(width=True, height=True)
win1.title("Speed Typers")
app = ResultScreen(win1)
win1.mainloop() 
            
    
   
