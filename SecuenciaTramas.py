from Trama import Trama


class SecuenciaTramas:
    
        global indicador 
        indicador = "10000001"
        global indicador2
        indicador2 = "0001003"
        global msj_recibido
        msj_recibido = {}
        global frm_recibido
        frm_recibido = 0
        global cont_envio
        cont_envio = 0
        global cont_resp
        cont_resp = 0
        global info_transmisor
        info_transmisor = ""
        global info_receptor
        info_receptor = ""
        global info_respuesta
        info_respuesta = ""
        global secuences_list
        secuences_list = []
        global lista_tramas
        lista_tramas = []
        global trama_inicial
        trama_inicial = Trama()
        global palabra_partes
        palabra_partes=""
        global contnum
        contnum=0


        def __init__(self, mensaje,frames):
            self.indicador="10000001"
            self.indicador2="0001003"
            self.msj_recibido=mensaje.split(" ")
            self.frm_recibido=frames
            self.lista_tramas = []
            self.trama_inicial = Trama()
            self.secuences_list = []
            self.cont_envio=0
            self.cont_resp=0
            self.palabra_partes=""
            self.contnum=0
            
# -----------------------------PRIMER ENVIO------------------------------------
        def solicitar_permiso(self):
            self.trama_inicial=Trama()
            self.trama_inicial.CTR = 1
            self.trama_inicial.PPT = 1
            self.lista_tramas.append(self.trama_inicial)
            self.info_transmisor = self.msj_recibido[cont_envio]
            self.secuences_list.append("Trama 1:(Tx) Control, permiso para transmitir")
            

        def conceder_permiso(self):
            self.trama_inicial=Trama()
            self.trama_inicial.LPR = 1
            self.trama_inicial.CTR = 1
            self.lista_tramas.append(self.trama_inicial)
            self.secuences_list.append("Trama 1:(Tx) Control, listo para recibir")
# --------------------------FIN PRIMER ENVIO------------------------------------
        
        def transmitir_trama(self):
            self.trama_inicial=Trama()
            if self.cont_resp==self.frm_recibido:
                self.trama_inicial=Trama()
                self.trama_inicial.DAT = 1
                self.trama_inicial.ENQ = 1
                self.lista_tramas.append(self.trama_inicial)
                self.trama_inicial.NUM = self.cont_envio 
            else:
                self.trama_inicial.DAT = 1
                self.lista_tramas.append(self.trama_inicial)
                # self.trama_inicial.NUM = str(self.cont_envio)
                self.secuences_list.append("Trama"+str(self.cont_envio)+":(Tx) Datos, Trama"+str(self.cont_envio))
                self.info_transmisor=self.msj_recibido[self.cont_envio-1]
                self.info_receptor=self.msj_recibido[self.cont_envio-1]
             

        def transmitir_ultima_trama(self):
            
            self.trama_inicial=Trama()
            self.trama_inicial.DAT = 1
            self.trama_inicial.ENQ = 1
            self.lista_tramas.append(self.trama_inicial)
            self.trama_inicial.NUM = self.cont_envio
        
        def recibir_trama(self):
            self.trama_inicial=Trama()
            self.trama_inicial.ACK = 1
            self.trama_inicial.CTR = 1
            # self.trama_inicial.NUM = str(self.cont_envio)
            self.lista_tramas.append(self.trama_inicial)
            self.info_respuesta=self.msj_recibido[self.cont_envio-1]
            

        def recibir_informacion(self):
            self.secuences_list.append("Trama"+str(self.cont_envio)+":(Rx) Control, Trama" +str(self.cont_envio)+ "recibida con éxito.")
            self.palabra_partes+= self.msj_recibido[self.cont_envio-1]+" "
            if self.cont_resp==self.frm_recibido:
                self.secuences_list.append("-----EL ENVIO DEL MENSAJE HA FINALIZADO CON EXITO-----")
            print("mensaje recibido")
            

        def enviar(self):
            if self.cont_envio==0:    
                self.solicitar_permiso()
                
            # if self.cont_resp==self.frm_recibido+2:
            #     self.transmitir_ultima_trama()            
            
            elif self.cont_envio!=0: 
                print(self.cont_resp,self.frm_recibido)
                self.transmitir_trama()


                
            

        def responder(self):
            if self.cont_resp==0:
                self.conceder_permiso()

            if self.cont_resp!=0:
                self.recibir_informacion()
                self.recibir_trama()
                
            self.cont_envio= self.cont_envio+1
            self.cont_resp = self.cont_resp+1

        def get_secuences(self):
            return self.secuences_list

        def get_recep_info(self):
            return self.info_receptor

        def get_trans_info(self):
            return self.info_transmisor

        def get_resp_info(self):
            return self.info_respuesta

