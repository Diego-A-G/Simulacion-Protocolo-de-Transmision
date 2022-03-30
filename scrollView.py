from tkinter import *


class scrollView:
    def __init__(self):
        self.window = Tk()

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, yscrollcommand=self.scrollbar.set)
        for i in range(100):
            self.listbox.insert("end", str(i))
        self.listbox.pack(side="left", fill="both")

        self.scrollbar.config(command=self.listbox.yview)

        self.window.mainloop()
