from binarytree import Node

class SistemaRutas:
    def __init__(self):
        self.raiz = None

    def agregar_ruta(self, destino, distancia):
        nueva_ruta = Node(distancia)
        nueva_ruta.destino = destino  
        
        if not self.raiz:
            self.raiz = nueva_ruta
        else:
            self.insertar_ruta(self.raiz, nueva_ruta)

    def insertar_ruta(self, actual, nueva_ruta):
        if nueva_ruta.value < actual.value:
            if actual.left is None:
                actual.left = nueva_ruta
            else:
                self.insertar_ruta(actual.left, nueva_ruta)
        else:
            if actual.right is None:
                actual.right = nueva_ruta
            else:
                self.insertar_ruta(actual.right, nueva_ruta)

    def buscar_ruta_mas_cercana(self):
        actual = self.raiz
        if not actual:
            return None
        while actual.left:
            actual = actual.left
        return f"{actual.destino} ({actual.value} km)"

    def imprimir_rutas(self):
        print(self.raiz)

sistema = SistemaRutas()
sistema.agregar_ruta("Sucursal A", 12)
sistema.agregar_ruta("Sucursal B", 7)
sistema.agregar_ruta("Sucursal C", 19)
sistema.agregar_ruta("Sucursal D", 4)
sistema.agregar_ruta("Sucursal E", 10)

print("Estructura del árbol BST:")
sistema.imprimir_rutas()

print("\nRuta más cercana:", sistema.buscar_ruta_mas_cercana())


