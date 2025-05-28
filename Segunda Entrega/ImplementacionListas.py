# Representación de una ruta con destino y distancia
class Ruta:
    def __init__(self, destino, distancia):
        self.destino = destino
        self.distancia = distancia  # en kilómetros, por ejemplo

    def __str__(self):
        return f"{self.destino} ({self.distancia} km)"

# Nodo de la lista simplemente enlazada
class Nodo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.siguiente = None

# Lista simplemente enlazada enfocada en rutas de entrega
class ListaRutas:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_ruta(self, ruta):
        nuevo_nodo = Nodo(ruta)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir_rutas(self):
        actual = self.cabeza
        while actual:
            print(actual.ruta, end=" -> ")
            actual = actual.siguiente
        print("None")

    def contar_rutas(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def ordenar_por_distancia(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return

        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.cabeza
            while actual.siguiente:
                if actual.ruta.distancia > actual.siguiente.ruta.distancia:
                    actual.ruta, actual.siguiente.ruta = actual.siguiente.ruta, actual.ruta
                    cambiado = True
                actual = actual.siguiente

    def buscar_ruta_mas_cercana(self):
        if self.esta_vacia():
            return None

        self.ordenar_por_distancia()
        return self.cabeza.ruta  # El primer nodo después de ordenar es el más cercano

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaRutas()

    # Agregar rutas (destino, distancia)
    lista.agregar_ruta(Ruta("Sucursal A", 12))
    lista.agregar_ruta(Ruta("Sucursal B", 7))
    lista.agregar_ruta(Ruta("Sucursal C", 19))
    lista.agregar_ruta(Ruta("Sucursal D", 4))

    print("Rutas ingresadas:")
    lista.imprimir_rutas()

    print("\nTotal de rutas registradas:", lista.contar_rutas())

    print("\nRuta más cercana:")
    ruta_cercana = lista.buscar_ruta_mas_cercana()
    if ruta_cercana:
        print(f"- {ruta_cercana}")
    else:
        print("No hay rutas disponibles.")
