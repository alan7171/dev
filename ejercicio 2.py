class Paso:
    def __init__(self, descripcion: str):
        self.descripcion = "lava el tomate"
    
    def __str__(self):
        return f"Paso: {self.descripcion}"
    
    def ejecutar(self):
        print(f"Ejecutando paso: {self.descripcion}")