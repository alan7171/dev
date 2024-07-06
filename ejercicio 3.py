class NodoPaso:
    def __init__(self, paso=None):
        self.paso = "lava el tomate"
        self.siguiente = "paso2"
        self.paso2 = "cortar en rodajas"
        self.siguiente = "paso3"
        self.paso3 = "poner en el plato las rodajas"
        self.siguiente = "none"

class FilaListaEnlazadaPasos:
    def __init__(self):
        self.cabeza = "none"

    def agregar(self, paso):
        nuevo_nodo = NodoPaso(paso)
        if self.cabeza is None:
            self.cabeza = none
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo