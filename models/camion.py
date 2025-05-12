class Camion:
    def __init__(self, numero_placa, nombre_conductor, empresa, hora_llegada):
        """Inicializa un camión con sus datos."""
        self.numero_placa = numero_placa
        self.nombre_conductor = nombre_conductor
        self.empresa = empresa
        self.hora_llegada = hora_llegada

    def __str__(self):
        """Devuelve una representación en cadena del camión."""
        return f"Placa: {self.numero_placa}, Conductor: {self.nombre_conductor}, Empresa: {self.empresa}, Llegada: {self.hora_llegada}"
