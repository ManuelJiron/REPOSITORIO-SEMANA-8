from models.camion import Camion
from models.cola_camiones import ColaCamiones
from datetime import datetime

class ControladorCamiones:
    def __init__(self):
        """Inicializa el controlador con una cola de camiones."""
        self.cola = ColaCamiones()

    def registrar_camion(self, numero_placa, nombre_conductor, empresa):
        """Registra un nuevo camión con la hora actual."""
        hora_llegada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        camion = Camion(numero_placa, nombre_conductor, empresa, hora_llegada)
        self.cola.agregar(camion)
        return f"Camión {numero_placa} registrado con éxito."

    def descargar_camion(self):
        """Retira el primer camión de la cola."""
        camion = self.cola.retirar()
        if camion:
            return f"Camión {camion.numero_placa} ha sido descargado."
        return "No hay camiones en la cola."

    def mostrar_cola(self):
        """Muestra el estado actual de la cola."""
        return self.cola.mostrar()
