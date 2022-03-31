
class Trama:
    ACK: int = "0"  # Cambia a 1 solo al enviar la respuesta
    ENQ: int = "0"  # Cambia a 1 cuando se envia la ultima trama
    CTR: int = "0"  # Cambia a 1 si es informacion de control
    DAT: int = "0"  # Cambia a 1 si es informacion de datos
    PPT: int = "0"  # Cambia a 1 cuando se hace la solicitud de transmisión
    LPR: int = "0"  # Cambia a 1 en respuesta a la solkicitud de transmisión
    NUM: int = "0"  # El numero de la trama a ser enviada

