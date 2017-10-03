from Tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.entrada = Label(self.widget1)
        self.entrada.pack()


        self.analisar = Button(self.widget1)
        self.analisar["text"] = "Analisar"
        self.analisar.pack(side=BOTTOM)




root = Tk()
Application(root)
root.mainloop()