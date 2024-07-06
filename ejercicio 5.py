class RecetarioDigital:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def ordenar_por_nombre(self):
        self.recetas.sort(key=lambda x: x.nombre)

    def __str__(self):
        if not self.recetas:
            return "Recetario vacío"
        else:
            recetario_str = "Recetario:\n"
            for receta in self.recetas:
                recetario_str += f"{receta}\n"
            return recetario_str