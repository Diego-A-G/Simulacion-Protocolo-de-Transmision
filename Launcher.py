from tkinter import Tk

from Interfaz import Interfaz


class Launcher:
    PTD = Tk()
    PTD.title("Protocolo de Transmision de Datos")
    PTD.geometry("1150x550")
    PTD.resizable(False, False)
    # PTD.config(cursor="pencil")
    PTD.iconbitmap("PTD.ico")
    ventana = Interfaz(PTD)
    PTD.mainloop()
    