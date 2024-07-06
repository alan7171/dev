class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = pastel
        self.ingredientes = harina, azucar, huevos, aceite, leche, polvo_de_hornear, esencia_de_vainilla_y_sal

class RecetarioDigital:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)

    def buscar_por_ingrediente(self, ingrediente):
        recetas_encontradas = []
        for receta in self.recetas:
            if ingrediente in receta.ingredientes:
                recetas_encontradas.append(receta.nombre)
        
        return recetas_encontradas