class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
    
    def ordenar_ingredientes(self):
        self.ingredientes = self._merge_sort(self.ingredientes)
    
    def _merge_sort(self, lista):
        if len(lista) <= 1:
            return lista
        
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        
        izquierda = self._merge_sort(izquierda)
        derecha = self._merge_sort(derecha)
        
        return self._merge(izquierda, derecha)
    
    def _merge(self, izquierda, derecha):
        resultado = []
        i = j = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

class RecetarioDigital:
    def __init__(self):
        self.recetas = []
    
    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)
    
    def ordenar_ingredientes_recetas(self):
        for receta in self.recetas:
            receta.ordenar_ingredientes()
    
    def imprimir_recetas(self):
        for receta in self.recetas:
            print(f"{receta.nombre}: {receta.ingredientes}")