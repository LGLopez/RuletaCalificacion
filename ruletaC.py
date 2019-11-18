from tkinter import *

class GUIRuleta(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title('Ruleta Calificacion')
        self.btnPlay = Button(text = 'Jugar')
        self.btnPlay.pack()
        

def main():
    root = Tk()
    GUIRuleta(root)
    root.geometry('500x500')
    root.mainloop()

if __name__ == '__main__':
    main()