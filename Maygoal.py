from tkinter import *
from fiveLetter import * 
from random import *
class ResultScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.load_pages()
    def load_pages(self):
        self.page1 = Frame(self.master)
        self.page1.grid(row = 0, column = 0, sticky = N + W + E + S )
        self.page2 = Frame(self.master)
        self.page2.grid(row = 0, column = 0, sticky = N + W + E + S )
        self.page3 = Frame(self.master)
        self.page3.grid(row = 0, column = 0, sticky = N + W + E + S)
        # setting up page 1
        self.b1 = Button(self.page1, text = "START", command = lambda:self.SetUpFirstPage())
        self.b1.grid(row = 0, column=5, sticky = N + W + E + S)
        # setting up page 3 
        self.b2 = Button(self.page2, text= " 5 letter words", command = lambda:self.ImportFive() )
        self.b2.grid(row = 0, column =5, sticky= N + W + E + S )


        # setting up for page 3
        self.b3 = Button(self.page3, text = "Restart", command = lambda:self.page1.tkraise())
        self.b3.grid(row = 0, column=5, sticky = N + W + E + S)
        self.l3 = Label(self.page3, text = "WPM")
        self.l3.grid(row = 1, column=5, sticky = N + W + E + S)
        # the start/Welcome page will be the first thing the user sees/ it includes the START button
        self.page1.tkraise()
    
    # fisrt page : it's a page where 
    def SetUpFirstPage(self):
        # generates random 
        self.page2.tkraise()
    def ImportFive(self):
        words = sample(five_letters_words, 100)
        string = ""
        n = 10
        while n <= len(words):
            for i in range(n-10, n):
                string += words[i] + "  "    
            string += "\n"
            n += 10
        self.l2 = Label(self.page2, text = string)
        self.l2.grid(row=1, column= 5, sticky= N + W + E + S )


    
        



#main
win1 =Tk()
win1.geometry("500x500")
win1.title("Speed Typers")
app = ResultScreen(win1)
win1.mainloop()                

def CheckInput(listOfWords, listOfInput):
    for i in len(listOfWords):
        if listOfInput == listOfWords[i]:
            pass
        else:
            pass
            
    
   
