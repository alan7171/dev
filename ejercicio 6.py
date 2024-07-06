class Paso:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.siguiente = None

class FilaListaEnlazadaPasos:
    def __init__(self):
        self.cabeza = None

    def insertar_paso(self, descripcion, posicion):
        nuevo_paso = Paso(descripcion)
        
        if not self.cabeza or posicion == 0:
            nuevo_paso.siguiente = self.cabeza
            self.cabeza = nuevo_paso
        else:
            actual = self.cabeza
            contador = 0
            
            while actual.siguiente and contador < posicion - 1:
                actual = actual.siguiente
                contador += 1
            
            nuevo_paso.siguiente = actual.siguiente
            actual.siguiente = nuevo_paso

    def imprimir_pasos(self):
        actual = self.cabeza
        while actual:
            print(actual.descripcion)
            actual = actual.siguiente