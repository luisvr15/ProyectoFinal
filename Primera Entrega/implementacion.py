class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def contar_elementos(self):
        contador = 0
        posicion = self.cabeza
        while posicion:
            contador = contador + 1
            posicion = posicion.siguiente
        return contador

    def imprimir_lista(self):
        posicion = self.cabeza
        while posicion:
            print(posicion.dato, end=" -> ")
            posicion = posicion.siguiente
        print("None")

    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def buscar_elemento(self, dato):
        self.ordenar_lista()
        posicion = self.cabeza
        while posicion:
            if posicion.dato == dato:
                return True
            posicion = posicion.siguiente
        return False

    def ordenar_lista(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return

        cambiado = True
        while cambiado:
            cambiado = False
            posicion = self.cabeza
            while posicion.siguiente:
                if posicion.dato > posicion.siguiente.dato:
                    posicion.dato, posicion.siguiente.dato = posicion.siguiente.dato, posicion.dato
                    cambiado = True
                posicion = posicion.siguiente

if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar_inicio(3)
    lista.agregar_inicio(1)
    lista.agregar_inicio(4)
    lista.agregar_inicio(2)

    print("Lista enlazada:")
    lista.imprimir_lista()

    print("Número de elementos:", lista.contar_elementos())

    elemento = 3
    print(f"¿El elemento {elemento} está en la lista? {'Sí' if lista.buscar_elemento(elemento) else 'No'}")
