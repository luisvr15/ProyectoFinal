import tkinter as tk
from tkinter import messagebox
import heapq

class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_ruta(self, origen, destino, distancia):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        if destino not in self.adyacencia:
            self.adyacencia[destino] = []
        self.adyacencia[origen].append((destino, distancia))
        self.adyacencia[destino].append((origen, distancia))

    def mostrar_rutas(self):
        rutas = ""
        for origen in self.adyacencia:
            for destino, distancia in self.adyacencia[origen]:
                rutas += f"{origen} -> {destino} ({distancia} km)\n"
        return rutas.strip()

    def ruta_mas_cercana(self, origen):
        if origen not in self.adyacencia:
            return None
        return min(self.adyacencia[origen], key=lambda x: x[1], default=None)

    def dijkstra(self, inicio, fin):
        if inicio not in self.adyacencia or fin not in self.adyacencia:
            return float('inf'), []

        distancias = {nodo: float('inf') for nodo in self.adyacencia}
        anteriores = {nodo: None for nodo in self.adyacencia}
        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            distancia_actual, actual = heapq.heappop(cola)

            if actual == fin:
                break

            for vecino, peso in self.adyacencia[actual]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual
                    heapq.heappush(cola, (nueva_distancia, vecino))

        camino = []
        nodo = fin
        while nodo is not None:
            camino.insert(0, nodo)
            nodo = anteriores[nodo]

        return distancias[fin], camino


class InterfazRutas:
    def __init__(self, root):
        self.grafo = Grafo()
        self.root = root
        self.root.title("Gestor de Rutas")
        self.root.config(bg="#f0f0f0")

        # Etiquetas y entradas
        tk.Label(root, text="Origen:", bg="#f0f0f0").grid(row=0, column=0)
        tk.Label(root, text="Destino:", bg="#f0f0f0").grid(row=1, column=0)
        tk.Label(root, text="Distancia (km):", bg="#f0f0f0").grid(row=2, column=0)

        self.origen_entry = tk.Entry(root)
        self.destino_entry = tk.Entry(root)
        self.distancia_entry = tk.Entry(root)

        self.origen_entry.grid(row=0, column=1)
        self.destino_entry.grid(row=1, column=1)
        self.distancia_entry.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Agregar Ruta", bg="#4CAF50", fg="white", command=self.agregar_ruta).grid(row=3, column=0, columnspan=2, pady=5, ipadx=20)
        tk.Button(root, text="Mostrar Rutas", bg="#2196F3", fg="white", command=self.mostrar_rutas).grid(row=4, column=0, columnspan=2, pady=5, ipadx=20)
        tk.Button(root, text="Ruta más corta", bg="#FF9800", fg="white", command=self.calcular_ruta_corta).grid(row=5, column=0, columnspan=2, pady=5, ipadx=20)

        # Entradas para ruta más corta
        tk.Label(root, text="Desde:", bg="#f0f0f0").grid(row=6, column=0)
        tk.Label(root, text="Hasta:", bg="#f0f0f0").grid(row=7, column=0)

        self.origen_busqueda = tk.Entry(root)
        self.destino_busqueda = tk.Entry(root)
        self.origen_busqueda.grid(row=6, column=1)
        self.destino_busqueda.grid(row=7, column=1)

        # Área de salida
        self.salida = tk.Text(root, height=12, width=50, bg="#ffffff")
        self.salida.grid(row=8, column=0, columnspan=2, pady=10)

    def agregar_ruta(self):
        origen = self.origen_entry.get()
        destino = self.destino_entry.get()
        try:
            distancia = float(self.distancia_entry.get())
            self.grafo.agregar_ruta(origen, destino, distancia)
            messagebox.showinfo("Éxito", "Ruta agregada correctamente")
        except ValueError:
            messagebox.showerror("Error", "Distancia inválida")

    def mostrar_rutas(self):
        rutas = self.grafo.mostrar_rutas()
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, rutas if rutas else "No hay rutas registradas.")

    def calcular_ruta_corta(self):
        origen = self.origen_busqueda.get()
        destino = self.destino_busqueda.get()
        distancia, camino = self.grafo.dijkstra(origen, destino)
        self.salida.delete(1.0, tk.END)
        if camino:
            self.salida.insert(tk.END, f"Ruta más corta de {origen} a {destino}:\n")
            self.salida.insert(tk.END, " -> ".join(camino) + f"\nDistancia total: {distancia} km")
        else:
            self.salida.insert(tk.END, "No se encontró una ruta entre los nodos especificados.")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazRutas(root)
    root.mainloop()
