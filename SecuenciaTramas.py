# -*- coding: utf-8 -*-

class SecuenciaTramas:
    
        global indicador 
        indicador = "10000001"
        global trama
        trama = {}
        global trama_ini
        trama_ini={
            "ACK":"0",  #Cambia a 1 solo al enviar la respuesta
            "ENQ":"0",  #Cambia a 1 cuando se envia la ultima trama
            "CTR":"0",  #Cambia a 1 si es informacion de control
            "DAT":"0",  #Cambia a 1 si es informacion de datos
            "PPT":"0",  #Cambia a 1 cuando se hace la solicitud de transmisión
            "LPR":"0",  #Cambia a 1 en respuesta a la solkicitud de transmisión
            "NUM":"0"   #El numero de la trama a ser enviada
            }
        global msj_recibido
        msj_recibido={}
        global frm_recibido     
        frm_recibido=0
        global cont_envio
        cont_envio=0
        global cont_resp
        cont_resp=0
        global cont_frames
        cont_frames=0
        global info_transmisor
        info_transmisor=""
        global info_receptor
        info_receptor=""
        global info_respuesta
        info_respuesta=""
        

        def __init__(self, mensaje,frames):
            self.msj_recibido=mensaje.split(" ")
            self.frm_recibido=frames  
            
            self.cont_envio=0
            self.cont_resp=0
            
# -----------------------------PRIMER ENVIO------------------------------------
        def permiso(self):
            trama.update(trama_ini)
            trama["CTR"] = "1"
            trama["PPT"] = "1"
            tramas = "".join(trama.values())
            self.info_transmisor=self.msj_recibido[cont_envio]
            print("Trama 1:(Tx) Control, permiso para transmitir")
            return trama,tramas
        
        
        def permiso_concedido(self):
            trama.update(trama_ini)
            trama["LPR"] = "1"
            trama["CTR"] = "1"
            print("Trama 1:(Tx) Control, listo para recibir") 
            return trama
# --------------------------FIN RIMER ENVIO------------------------------------
        
        def transmitir_trama(self):
            trama.update(trama_ini)
            trama["DAT"] = "1"
            trama["NUM"] = self.cont_envio
            # tramas = "".join(trama.values())
            print("Trama",self.cont_envio+1,":(Tx) Datos, Trama",self.cont_envio+1)
            self.info_transmisor=self.msj_recibido[self.cont_envio-1]
            self.info_receptor=self.msj_recibido[self.cont_envio-1]
            print("MENSAJE:-----------",self.msj_recibido[self.cont_envio-1],"------------------")
            # return trama,tramas
        
        def transmitir_ultima_trama(self):
            trama.update(trama_ini)
            trama["DAT"] = "1"
            trama["ENQ"] = "1"
            trama["NUM"] = self.cont_envio
            # tramas = "".join(trama.values())
            
            # return trama,tramas
        
        def recibir_trama(self):
            trama.update(trama_ini)
            trama["ACK"] = "1"
            trama["CTR"] = "1"
            trama["NUM"] = self.cont_envio
            self.info_respuesta=self.msj_recibido[self.cont_envio-1]
            print("Trama",self.cont_envio+1,":(Rx) Control, Trama",self.cont_envio+1,"recibida con éxito.")
            return trama
        
        # def recibir_informacion(self,msj):
        #     msj_recibido.append(msj)
        #     return " ".join(msj_recibido)
        
        def recibir_informacion(self):
            print("mensaje recibido")
        
        
        
        
        
        def enviar(self):
            if self.cont_envio==0:    
                self.permiso()
                
            if self.cont_envio>self.frm_recibido:
                print("ERROR",self.cont_envio,frm_recibido)
            
            if self.cont_envio!=0: 
                self.transmitir_trama()
                self.recibir_trama()
                
            
                
        
        def responder(self):
            if self.cont_resp==0:
                self.permiso_concedido()
            if self.cont_resp!=0:
                self.recibir_informacion()
            self.cont_envio= self.cont_envio+1
            self.cont_resp = self.cont_resp+1



#FALTA: 
#Manejo de que mensaje se envia y que numero de trama es
#Mensaje de seccion de tramas
#Comunicacion con la interfaz
#Finzalizar la transmision y reiniciar
