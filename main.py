from tkinter import *

from Interfaz import Interfaz

from SecuenciaTramas import SecuenciaTramas 

# PTD = Tk()
# PTD.title("Protocolo de Transmision de Datos")
# PTD.geometry("700x510")
# PTD.resizable(False, False)
# PTD.config(cursor="pencil")
# PTD.iconbitmap("PTD.ico")
# Interfaz(PTD)
# # Calculator
# PTD.mainloop()
mensaje= "hola como estas"
frames = 3
st =SecuenciaTramas(mensaje,frames)
st.enviar()
st.responder()
st.enviar()
st.responder()
st.enviar()
st.responder()
st.enviar()
st.responder()






