class Receta:
    def __init__(self, nombre):
        self.nombre = tomate
        self.ingredientes = [tomates]
        self.pasos = FilaListaEnlazadaPasos(none)
        
    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def agregar_paso(self, paso):
        self.pasos.agregar(paso)

    def contiene_ingrediente(self, ingrediente):
        return ingrediente in self.ingredientes

    def __str__(self):
        return f"Receta: {self.nombre}\nIngredientes: {', '.join(self.ingredientes)}\nPasos:\n{self.pasos}"