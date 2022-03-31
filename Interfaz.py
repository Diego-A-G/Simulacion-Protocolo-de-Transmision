from tkinter import *

from SecuenciaTramas import SecuenciaTramas
from scrollView import scrollView


class Interfaz(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.listbox = Listbox(self, width=50, height=30)
        self.message = StringVar()
        self.frames= StringVar()
        self.indic = StringVar()
        self.ack = StringVar()
        self.enq = StringVar()
        self.ctr= StringVar()
        self.dat= StringVar()
        self.ppt= StringVar()
        self.lpr= StringVar()
        self.num= StringVar()
        self.info = StringVar()
        self.indic2 = StringVar()
        self.ack_var= BooleanVar(self)
        self.enq_var= BooleanVar(self)
        self.ctr_var= BooleanVar(self)
        self.dat_var= BooleanVar(self)
        self.ppt_var= BooleanVar(self)
        self.lpr_var= BooleanVar(self)
        self.begin_header = StringVar()
        self.end_header = StringVar()
        self.info_received = StringVar()
        self.begin_trailer = StringVar()
        self.indic_resp = StringVar()
        self.ack_resp = StringVar()
        self.enq_resp = StringVar()
        self.ctr_resp = StringVar()
        self.dat_resp = StringVar()
        self.ppt_resp = StringVar()
        self.lpr_resp = StringVar()
        self.num_resp = StringVar()
        self.info_resp = StringVar()
        self.indic2_resp = StringVar()
        self.message_received = StringVar()
        self.primer_envio = True
        self.secuencia_tramas = None
        self.secuences =[]
        self.resp_btn = Button(self, text="Responder", command=self.resp_message, state=DISABLED)
        self.send_btn = Button(self, text="Enviar", command=self.send_message)
        self.config(width=1100, height=500)
        self.parent = master
        self.createWidgets()
        Frame.pack(self)


    def createWidgets(self):

        title_lbl = Label(self, text="TRANSMISOR", font=("Arial", 12))
        title_lbl.place(x=10, y=10)

        message_lbl = Label(self, text="MENSAJE A TRANSMITIR:", font=("Arial", 10))
        message_lbl.place(x=10, y=40)

        message_entry = Entry(self, width=30, textvariable=self.message)
        self.message.set("")
        message_entry.place(x=180, y=40)

        frames_lbl = Label(self, text="NUMERO DE FRAMES:", font=("Arial", 10))
        frames_lbl.place(x=390, y=40)

        frames_entry = Entry(self, width=3, textvariable=self.frames, state=DISABLED)
        self.frames.set("")
        frames_entry.place(x=540, y=40)

        indic_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic_lbl.place(x=20, y=90)

        
        indic_entry = Entry(self, width=12, textvariable=self.indic, state=DISABLED)
        indic_entry.place(x=10, y=120)
        

        ack_lbl = Label(self, text="ACK", font=("Arial", 8))
        ack_lbl.place(x=100, y=90)

        
        ack_entry = Entry(self, width=3, textvariable=self.ack, state=DISABLED)
        ack_entry.place(x=100, y=120)

        
        ack_ckb = Checkbutton(self, variable=self.ack_var, command=self.ack_clicked, state=DISABLED)
        ack_ckb.place(x=100, y=150)

        enq_lbl = Label(self, text="ENQ", font=("Arial", 8))
        enq_lbl.place(x=150, y=90)

        
        enq_entry = Entry(self, width=3, textvariable=self.enq, state=DISABLED) 
        enq_entry.place(x=150, y=120)

        enq_ckb = Checkbutton(self, variable=self.enq_var, command=self.enq_clicked, state=DISABLED)
        enq_ckb.place(x=150, y=150)

        ctr_lbl = Label(self, text="CTR", font=("Arial", 8))
        ctr_lbl.place(x=200, y=90)

        ctr_entry = Entry(self, width=3, textvariable=self.ctr, state=DISABLED)
        ctr_entry.place(x=200, y=120)

        ctr_ckb = Checkbutton(self, variable=self.ctr_var, command=self.ctr_clicked, state=DISABLED)
        ctr_ckb.place(x=200, y=150)

        dat_lbl = Label(self, text="DAT", font=("Arial", 8))
        dat_lbl.place(x=250, y=90)

        dat_entry = Entry(self, width=3, textvariable=self.dat, state=DISABLED)
        dat_entry.place(x=250, y=120)

        dat_ckb = Checkbutton(self, variable=self.dat_var, command=self.dat_clicked, state=DISABLED)
        dat_ckb.place(x=250, y=150)

        ppt_lbl = Label(self, text="PPT", font=("Arial", 8))
        ppt_lbl.place(x=300, y=90)

        ppt_entry = Entry(self, width=3, textvariable=self.ppt, state=DISABLED)
        ppt_entry.place(x=300, y=120)

        ppt_ckb = Checkbutton(self, variable=self.ppt_var, command=self.ppt_clicked, state=DISABLED)
        ppt_ckb.place(x=300, y=150)

        lpr_lbl = Label(self, text="LPR", font=("Arial", 8))
        lpr_lbl.place(x=350, y=90)

        lpr_entry = Entry(self, width=3, textvariable=self.lpr, state=DISABLED)
        lpr_entry.place(x=350, y=120)


        lpr_ckb = Checkbutton(self, variable=self.lpr_var, command=self.lpr_clicked, state=DISABLED)
        lpr_ckb.place(x=350, y=150)

        num_lbl = Label(self, text="NUM", font=("Arial", 8))
        num_lbl.place(x=400, y=90)

        num_entry = Entry(self, width=3, textvariable=self.num, state=DISABLED)
        num_entry.place(x=400, y=120)

        info_lbl = Label(self, text="INFORMACION", font=("Arial", 8))
        info_lbl.place(x=450, y=90)

        
        info_entry = Entry(self, width=12, textvariable=self.info, state=DISABLED)
        info_entry.place(x=450, y=120)

        indic2_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic2_lbl.place(x=550, y=90)

        
        indic2_entry = Entry(self, width=12, textvariable=self.indic2, state=DISABLED)
        indic2_entry.place(x=540, y=120)

        self.send_btn.place(x=640,y=115)

        tdd_lbl = Label(self, text="SEMANTICA: TRAMA DE DATOS", font=("Arial", 10))
        tdd_lbl.place(x=100, y=180)

        title_lbl = Label(self, text="RECEPTOR", font=("Arial", 12))
        title_lbl.place(x=10, y=220)

        trama_lbl = Label(self, text="TRAMA RECIBIDA", font=("Arial", 10))
        trama_lbl.place(x=10, y=250)

        
        header1_entry = Entry(self, width=12, textvariable=self.begin_header, state=DISABLED)
        header1_entry.place(x=10, y=280)

        
        header2_entry = Entry(self, width=12, textvariable=self.end_header, state=DISABLED)
        header2_entry.place(x=100, y=280)

        info_lbl = Label(self, text="HEADER", font=("Arial", 8))
        info_lbl.place(x=70, y=310)

  
        info_received_entry = Entry(self, width=12, textvariable=self.info_received, state=DISABLED)
        info_received_entry.place(x=200, y=280)

        info_lbl = Label(self, text="INFORMACION", font=("Arial", 8))
        info_lbl.place(x=200, y=310)

         
        trailer_entry = Entry(self, width=12, textvariable=self.begin_trailer, state=DISABLED)
        trailer_entry.place(x=300, y=280)

        info_lbl = Label(self, text="TRAILER", font=("Arial", 8))
        info_lbl.place(x=310, y=310)

        resp_lbl = Label(self, text="RESPUESTA", font=("Arial", 10))
        resp_lbl.place(x=10, y=340)

        indic_resp_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic_resp_lbl.place(x=20, y=370)

        
        indic_resp_entry = Entry(self, width=12, textvariable=self.indic_resp, state=DISABLED)
        indic_resp_entry.place(x=10, y=400)

        ack_resp_lbl = Label(self, text="ACK", font=("Arial", 8))
        ack_resp_lbl.place(x=100, y=370)


        ack_resp_entry = Entry(self, width=3, textvariable=self.ack_resp, state=DISABLED)
        ack_resp_entry.place(x=100, y=400)

        enq_resp_lbl = Label(self, text="ENQ", font=("Arial", 8))
        enq_resp_lbl.place(x=150, y=370)

       
        enq_resp_entry = Entry(self, width=3, textvariable=self.enq_resp, state=DISABLED)
        enq_resp_entry.place(x=150, y=400)

        ctr_resp_lbl = Label(self, text="CTR", font=("Arial", 8))
        ctr_resp_lbl.place(x=200, y=370)

        
        ctr_resp_entry = Entry(self, width=3, textvariable=self.ctr_resp, state=DISABLED)
        ctr_resp_entry.place(x=200, y=400)

        dat_resp_lbl = Label(self, text="DAT", font=("Arial", 8))
        dat_resp_lbl.place(x=250, y=370)

        
        dat_resp_entry = Entry(self, width=3, textvariable=self.dat_resp, state=DISABLED)
        dat_resp_entry.place(x=250, y=400)

        ppt_resp_lbl = Label(self, text="PPT", font=("Arial", 8))
        ppt_resp_lbl.place(x=300, y=370)

        
        ppt_resp_entry = Entry(self, width=3, textvariable=self.ppt_resp, state=DISABLED)
        ppt_resp_entry.place(x=300, y=400)

        lpr_resp_lbl = Label(self, text="LPR", font=("Arial", 8))
        lpr_resp_lbl.place(x=350, y=370)

        
        lpr_resp_entry = Entry(self, width=3, textvariable=self.lpr_resp, state=DISABLED)
        lpr_resp_entry.place(x=350, y=400)

        num_resp_lbl = Label(self, text="NUM", font=("Arial", 8))
        num_resp_lbl.place(x=400, y=370)

        
        num_resp_entry = Entry(self, width=3, textvariable=self.num_resp, state=DISABLED)
        num_resp_entry.place(x=400, y=400)

        info_resp_lbl = Label(self, text="INFORMACION", font=("Arial", 8))
        info_resp_lbl.place(x=450, y=370)


        info_resp_entry = Entry(self, width=12, textvariable=self.info_resp, state=DISABLED)
        info_resp_entry.place(x=450, y=400)

        indic2_resp_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic2_resp_lbl.place(x=550, y=370)

        
        indic2_resp_entry = Entry(self, width=12, textvariable=self.indic2_resp, state=DISABLED)
        indic2_resp_entry.place(x=540, y=400)

        self.resp_btn.place(x=640, y=385)

        tdd_lbl = Label(self, text="SEMANTICA: TRAMA DE CONTROL Y RECIBIDA CON EXITO ", font=("Arial", 10))
        tdd_lbl.place(x=100, y=430)

        message_received_lbl = Label(self, text="MENSAJE RECIBIDO", font=("Arial", 10))
        message_received_lbl.place(x=10, y=470)

        
        message_received_entry = Entry(self, width=22, textvariable=self.message_received,state=DISABLED)
        message_received_entry.place(x=150, y=470)

        self.listbox.place(x=750,y=50)

    def send_message(self):
        if self.primer_envio:
            mess = self.message.get()
            frm = len(mess.split(" "))
            if frm==1:
                self.listbox.insert("end","------ERROR, POR FAVOR INGRESE UNA PALABRA-------")
                return
            self.frames.set(frm)
            self.secuencia_tramas = SecuenciaTramas(mess, frm)
            self.secuencia_tramas.enviar()
            self.secuences = self.secuencia_tramas.get_secuences()
            self.show_tramas()
            self.show_trans_info()
            self.show_recep_info()
            self.primer_envio = False
        else:
            self.secuencia_tramas.enviar()
            self.secuences = self.secuencia_tramas.get_secuences()
            self.show_tramas()
            self.show_trans_info()
            self.show_recep_info()
        self.send_btn['state'] = DISABLED
        self.resp_btn['state'] = NORMAL
        if self.secuencia_tramas.cont_envio==self.secuencia_tramas.frm_recibido+1:
            self.send_btn['state'] = DISABLED

    def show_tramas(self):
        self.listbox.delete(0,'end')
        for i in range(len(self.secuences)):
            self.listbox.insert("end", self.secuences[i])

    def resp_message(self):
        index=self.secuencia_tramas.cont_envio + self.secuencia_tramas.cont_resp
        trama=self.secuencia_tramas.secuences_list[index-1]
        self.show_resp_info(index)
        self.secuencia_tramas.recibir_trama()
        #cacambio de lugar linea 319 320
        if not self.primer_envio:
            self.secuencia_tramas.responder()
            self.secuences = self.secuencia_tramas.get_secuences()
            self.show_tramas()
            self.show_resp_info(index)
        self.send_btn['state'] = NORMAL
        self.resp_btn['state'] = DISABLED
        if self.secuencia_tramas.cont_envio==self.secuencia_tramas.frm_recibido+1:
            self.send_btn['state'] = DISABLED
            self.resp_btn['state'] = DISABLED

    def show_trans_info(self):
        index=self.secuencia_tramas.cont_envio + self.secuencia_tramas.cont_resp
        trama=self.secuencia_tramas.secuences_list[index-1]
        self.mostrar_tramas()
        self.validar_tramas()
        self.limpiar_ventanas()
        print("cargando trans info")
    
    
    def limpiar_ventanas(self):
        print("limpio")
        
    
    def mostrar_tramas(self):
        # -----------------------TRANSMISOR-----------------------------
        self.indic.set(self.secuencia_tramas.indicador)
        self.indic2.set(self.secuencia_tramas.indicador)
        self.info.set(self.secuencia_tramas.info_transmisor)
        # self.ack.set(self.secuencia_tramas.lista_tramas[index].ACK)
        # self.enq.set(self.secuencia_tramas.lista_tramas[index].ENQ)
        # self.ctr.set(self.secuencia_tramas.lista_tramas[index].CTR)
        # self.dat.set(self.secuencia_tramas.lista_tramas[index].DAT)
        # self.ppt.set(self.secuencia_tramas.lista_tramas[index].PPT)
        # self.lpr.set(self.secuencia_tramas.lista_tramas[index].LPR)
        self.num.set(self.secuencia_tramas.cont_envio)
        self.ack.set(self.secuencia_tramas.trama_inicial.ACK)
        self.enq.set(self.secuencia_tramas.trama_inicial.ENQ)
        self.ctr.set(self.secuencia_tramas.trama_inicial.CTR)
        self.dat.set(self.secuencia_tramas.trama_inicial.DAT)
        self.ppt.set(self.secuencia_tramas.trama_inicial.PPT)
        self.lpr.set(self.secuencia_tramas.trama_inicial.LPR)
        # print("CTR"self.secuencia_tramas.trama_inicial.CRT)
        # print("PPT"self.secuencia_tramas.trama_inicial.PPT)

        
    
    
    def validar_tramas(self):
        if self.secuencia_tramas.trama_inicial.ACK==1:
            self.ack_var.set(True)
        else:
            self.ack_var.set(False) 
            
        if self.secuencia_tramas.trama_inicial.ENQ==1:
            self.enq_var.set(True)
        else:
            self.enq_var.set(False) 
            
        if self.secuencia_tramas.trama_inicial.CTR==1:
            self.ctr_var.set(True)
        else:
            self.ctr_var.set(False)
            
        if self.secuencia_tramas.trama_inicial.DAT==1:
            self.dat_var.set(True)
        else:
            self.dat_var.set(False) 
            
        if self.secuencia_tramas.trama_inicial.PPT==1:
            self.ppt_var.set(True)
        else:
            self.ppt_var.set(False) 
            
        if self.secuencia_tramas.trama_inicial.LPR==1:
            self.lpr_var.set(True)
        else:
            self.lpr_var.set(False) 

        

    def show_recep_info(self):
        # -----------------------RECEPTOR-------------------------------
        self.begin_header.set(self.secuencia_tramas.indicador)
        self.end_header.set(self.secuencia_tramas.indicador2)
        self.begin_trailer.set(self.secuencia_tramas.indicador)
        self.info_received.set(self.secuencia_tramas.info_transmisor)
        print("cargando recep info")

    def show_resp_info(self,index):
        # -----------------------RESPUESTA------------------------------
        self.indic_resp.set(self.secuencia_tramas.indicador)
        # self.ack_resp.set(self.secuencia_tramas.lista_tramas[index].ACK)
        # self.enq_resp.set(self.secuencia_tramas.lista_tramas[index].ENQ)
        # self.ctr_resp.set(self.secuencia_tramas.lista_tramas[index].CTR)
        # self.dat_resp.set(self.secuencia_tramas.lista_tramas[index].DAT)
        # self.ppt_resp.set(self.secuencia_tramas.lista_tramas[index].PPT)
        # self.lpr_resp.set(self.secuencia_tramas.lista_tramas[index].LPR)
        self.ack_resp.set(self.secuencia_tramas.trama_inicial.ACK)
        self.enq_resp.set(self.secuencia_tramas.trama_inicial.ENQ)
        self.ctr_resp.set(self.secuencia_tramas.trama_inicial.CTR)
        self.dat_resp.set(self.secuencia_tramas.trama_inicial.DAT)
        self.ppt_resp.set(self.secuencia_tramas.trama_inicial.PPT)
        self.lpr_resp.set(self.secuencia_tramas.trama_inicial.LPR)
        self.num_resp.set(self.secuencia_tramas.cont_envio-1)
        self.info_resp.set(self.secuencia_tramas.info_transmisor)
        self.indic2_resp.set(self.secuencia_tramas.indicador)
        self.message_received.set(self.secuencia_tramas.palabra_partes)
        print("cargando resp info")

    def ack_clicked(self):
        print("ack")

    def enq_clicked(self):
        print("enq")

    def ctr_clicked(self):
        print("ctr")

    def dat_clicked(self):
        print("dat")

    def ppt_clicked(self):
        print("ppt")

    def lpr_clicked(self):
        print("lpr")

    def show_sequence(self):
        secuences = []
        app = scrollView(secuences)
