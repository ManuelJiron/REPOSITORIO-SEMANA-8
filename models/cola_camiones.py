from collections import deque

class ColaCamiones:
    def __init__(self):
        """Inicializa una cola vacía para los camiones."""
        self.cola = deque()

    def agregar(self, camion):
        """Agrega un camión al final de la cola."""
        self.cola.append(camion)

    def retirar(self):
        """Retira y devuelve el primer camión de la cola, si existe."""
        if not self.esta_vacia():
            return self.cola.popleft()
        return None

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.cola) == 0

    def mostrar(self):
        """Devuelve una representación en cadena de la cola."""
        if self.esta_vacia():
            return "No hay camiones en la cola."
        return "\n".join(str(camion) for camion in self.cola)
