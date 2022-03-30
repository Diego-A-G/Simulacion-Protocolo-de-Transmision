from tkinter import *

from scrollView import scrollView


class Interfaz(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.config(width=800, height=500)
        self.parent = master
        self.createWidgets()
        Frame.pack(self)

    def createWidgets(self):

        title_lbl = Label(self, text="TRANSMISOR", font=("Arial", 12))
        title_lbl.place(x=10, y=10)

        message_lbl = Label(self, text="MENSAJE A TRANSMITIR:", font=("Arial", 10))
        message_lbl.place(x=10, y=40)

        message = StringVar()
        message_entry = Entry(self, width=30, textvariable=message)
        message_entry.place(x=180, y=40)

        frames_lbl = Label(self, text="NUMERO DE FRAMES:", font=("Arial", 10))
        frames_lbl.place(x=390, y=40)

        frames = StringVar()
        frames_entry = Entry(self, width=3, textvariable=frames)
        frames_entry.place(x=540, y=40)

        indic_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic_lbl.place(x=20, y=90)

        indic = StringVar()
        indic_entry = Entry(self, width=12, textvariable=indic)
        indic_entry.place(x=10, y=120)

        ack_lbl = Label(self, text="ACK", font=("Arial", 8))
        ack_lbl.place(x=100, y=90)

        ack = StringVar()
        ack_entry = Entry(self, width=3, textvariable=ack)
        ack_entry.place(x=100, y=120)

        ack_var = BooleanVar(self)
        ack_ckb = Checkbutton(self, variable=ack_var, command=self.ack_clicked)
        ack_ckb.place(x=100, y=150)

        enq_lbl = Label(self, text="ENQ", font=("Arial", 8))
        enq_lbl.place(x=150, y=90)

        enq = StringVar()
        enq_entry = Entry(self, width=3, textvariable=enq)
        enq_entry.place(x=150, y=120)

        enq_var = BooleanVar(self)
        enq_ckb = Checkbutton(self, variable=enq_var, command=self.enq_clicked)
        enq_ckb.place(x=150, y=150)

        ctr_lbl = Label(self, text="CTR", font=("Arial", 8))
        ctr_lbl.place(x=200, y=90)

        ctr = StringVar()
        ctr_entry = Entry(self, width=3, textvariable=ctr)
        ctr_entry.place(x=200, y=120)

        ctr_var = BooleanVar(self)
        ctr_ckb = Checkbutton(self, variable=ctr_var, command=self.ctr_clicked)
        ctr_ckb.place(x=200, y=150)

        dat_lbl = Label(self, text="DAT", font=("Arial", 8))
        dat_lbl.place(x=250, y=90)

        dat = StringVar()
        dat_entry = Entry(self, width=3, textvariable=dat)
        dat_entry.place(x=250, y=120)

        dat_var = BooleanVar(self)
        dat_ckb = Checkbutton(self, variable=dat_var, command=self.dat_clicked)
        dat_ckb.place(x=250, y=150)

        ppt_lbl = Label(self, text="PPT", font=("Arial", 8))
        ppt_lbl.place(x=300, y=90)

        ppt = StringVar()
        ppt_entry = Entry(self, width=3, textvariable=ppt)
        ppt_entry.place(x=300, y=120)

        ppt_var = BooleanVar(self)
        ppt_ckb = Checkbutton(self, variable=ppt_var, command=self.ppt_clicked)
        ppt_ckb.place(x=300, y=150)

        lpt_lbl = Label(self, text="LPT", font=("Arial", 8))
        lpt_lbl.place(x=350, y=90)

        lpt = StringVar()
        lpt_entry = Entry(self, width=3, textvariable=lpt)
        lpt_entry.place(x=350, y=120)

        lpt_var = BooleanVar(self)
        lpt_ckb = Checkbutton(self, variable=lpt_var, command=self.lpt_clicked)
        lpt_ckb.place(x=3500, y=150)

        num_lbl = Label(self, text="NUM", font=("Arial", 8))
        num_lbl.place(x=400, y=90)

        num = StringVar()
        num_entry = Entry(self, width=3, textvariable=num)
        num_entry.place(x=400, y=120)

        info_lbl = Label(self, text="INFORMACION", font=("Arial", 8))
        info_lbl.place(x=450, y=90)

        info = StringVar()
        info_entry = Entry(self, width=12, textvariable=info)
        info_entry.place(x=450, y=120)

        indic2_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic2_lbl.place(x=550, y=90)

        indic2 = StringVar()
        indic2_entry = Entry(self, width=12, textvariable=indic2)
        indic2_entry.place(x=540, y=120)

        tdd_lbl = Label(self, text="SEMANTICA: TRAMA DE DATOS", font=("Arial", 10))
        tdd_lbl.place(x=100, y=180)

        title_lbl = Label(self, text="RECEPTOR", font=("Arial", 12))
        title_lbl.place(x=10, y=220)

        trama_lbl = Label(self, text="TRAMA RECIBIDA", font=("Arial", 10))
        trama_lbl.place(x=10, y=250)

        begin_header = StringVar()
        header1_entry = Entry(self, width=12, textvariable=begin_header)
        header1_entry.place(x=10, y=280)

        end_header = StringVar()
        header2_entry = Entry(self, width=12, textvariable=end_header)
        header2_entry.place(x=100, y=280)

        info_lbl = Label(self, text="HEADER", font=("Arial", 8))
        info_lbl.place(x=70, y=310)

        info_received = StringVar()
        info_received_entry = Entry(self, width=12, textvariable=info_received)
        info_received_entry.place(x=200, y=280)

        info_lbl = Label(self, text="INFORMACION", font=("Arial", 8))
        info_lbl.place(x=200, y=310)

        begin_header = StringVar()
        header1_entry = Entry(self, width=12, textvariable=begin_header)
        header1_entry.place(x=300, y=280)

        info_lbl = Label(self, text="TRAILER", font=("Arial", 8))
        info_lbl.place(x=310, y=310)

        resp_lbl = Label(self, text="RESPUESTA", font=("Arial", 10))
        resp_lbl.place(x=10, y=340)

        indic_resp_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic_resp_lbl.place(x=20, y=370)

        indic_resp = StringVar()
        indic_resp_entry = Entry(self, width=12, textvariable=indic_resp)
        indic_resp_entry.place(x=10, y=400)

        ack_resp_lbl = Label(self, text="ACK", font=("Arial", 8))
        ack_resp_lbl.place(x=100, y=370)

        ack_resp = StringVar()
        ack_resp_entry = Entry(self, width=3, textvariable=ack_resp)
        ack_resp_entry.place(x=100, y=400)

        enq_resp_lbl = Label(self, text="ENQ", font=("Arial", 8))
        enq_resp_lbl.place(x=150, y=370)

        enq_resp = StringVar()
        enq_resp_entry = Entry(self, width=3, textvariable=enq_resp)
        enq_resp_entry.place(x=150, y=400)

        ctr_resp_lbl = Label(self, text="CTR", font=("Arial", 8))
        ctr_resp_lbl.place(x=200, y=370)

        ctr_resp = StringVar()
        ctr_resp_entry = Entry(self, width=3, textvariable=ctr_resp)
        ctr_resp_entry.place(x=200, y=400)

        dat_resp_lbl = Label(self, text="DAT", font=("Arial", 8))
        dat_resp_lbl.place(x=250, y=370)

        dat_resp = StringVar()
        dat_resp_entry = Entry(self, width=3, textvariable=dat_resp)
        dat_resp_entry.place(x=250, y=400)

        ppt_resp_lbl = Label(self, text="PPT", font=("Arial", 8))
        ppt_resp_lbl.place(x=300, y=370)

        ppt_resp = StringVar()
        ppt_resp_entry = Entry(self, width=3, textvariable=ppt_resp)
        ppt_resp_entry.place(x=300, y=400)

        lpt_resp_lbl = Label(self, text="LPT", font=("Arial", 8))
        lpt_resp_lbl.place(x=350, y=370)

        lpt_resp = StringVar()
        lpt_resp_entry = Entry(self, width=3, textvariable=lpt_resp)
        lpt_resp_entry.place(x=350, y=400)

        num_resp_lbl = Label(self, text="NUM", font=("Arial", 8))
        num_resp_lbl.place(x=400, y=370)

        num_resp = StringVar()
        num_resp_entry = Entry(self, width=3, textvariable=num_resp)
        num_resp_entry.place(x=400, y=400)

        info_resp_lbl = Label(self, text="INFORMACION", font=("Arial", 8))
        info_resp_lbl.place(x=450, y=370)

        info_resp = StringVar()
        info_resp_entry = Entry(self, width=12, textvariable=info_resp)
        info_resp_entry.place(x=450, y=400)

        indic2_resp_lbl = Label(self, text="INDICADOR", font=("Arial", 8))
        indic2_resp_lbl.place(x=550, y=370)

        indic2_resp = StringVar()
        indic2_resp_entry = Entry(self, width=12, textvariable=indic2_resp)
        indic2_resp_entry.place(x=540, y=400)

        tdd_lbl = Label(self, text="SEMANTICA: TRAMA DE CONTROL Y RECIBIDA CON EXITO ", font=("Arial", 10))
        tdd_lbl.place(x=100, y=430)

        message_received_lbl = Label(self, text="MENSAJE RECIBIDO", font=("Arial", 10))
        message_received_lbl.place(x=10, y=470)

        message_received = StringVar()
        message_received_entry = Entry(self, width=22, textvariable=message_received)
        message_received_entry.place(x=150, y=470)

        secuencia_btn = Button(text="Ver secuencia de tramas", command=self.show_sequence)
        secuencia_btn.place(x=350, y=470)

    def show_trans_info(self):
        print("cargando trans info")

    def show_recep_info(self):
        print("cargando recep info")

    def show_resp_info(self):
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

    def lpt_clicked(self):
        print("lpt")

    def show_sequence(self):
        secuences = []
        app = scrollView(secuences)
