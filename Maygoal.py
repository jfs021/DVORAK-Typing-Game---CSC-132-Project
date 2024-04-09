from tkinter import *
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
        # setting up page 1
        self.b1 = Button(self.page1, text = "START", command = lambda:self.SetUpFirstPage())
        # setting up for page 2
        self.b2 = Button(self.page2, text = "Restart", command = lambda:self.page1.tkraise())
        self.l2 = Label(self.page2, text = "WPM")


#main
win1=Tk()
win1.geometry("500x500")
win1.title("Speed Typers")
app = App(win1)
win1.mainloop()                

def CheckInput(listOfWords, listOfInput):
    for i in len(listOfWords):
        if listOfInput == listOfWords[i]:
            pass
        else:
            pass
            
    
   
