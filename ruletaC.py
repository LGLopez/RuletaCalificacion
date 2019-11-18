import random
import  time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class GUIRuleta(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        imgMas = ImageTk.PhotoImage(Image.open("numero 0.jpg"))

        rows = 0
        while rows < 50:
            self.parent.rowconfigure(rows , weight =1)
            self.parent.columnconfigure(rows, weight = 1)
            rows+=1

        self.parent.title('Ruleta Calificacion')

        #self.btnPlay = Button(text = 'Jugar')
        #self.btnPlay.grid(row = 0, column = 25)

        self.lblSign = Label(image = imgMas)
        self.lblSign.pack()

def main():
    root = Tk()
    GUIRuleta(root)
    root.geometry('500x500')
    root.mainloop()

if __name__ == '__main__':
    main()