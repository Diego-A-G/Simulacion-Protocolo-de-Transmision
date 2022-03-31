from tkinter import *


class scrollView:
    def __init__(self,secuences):
        self.window = Tk()
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox = Listbox(self.window, yscrollcommand=self.scrollbar.set, width=50)
        for i in range(len(secuences)):
            self.listbox.insert("end", secuences[i])
        self.listbox.pack(side="left", fill="both")
        self.scrollbar.config(command=self.listbox.yview)
        self.window.mainloop()
