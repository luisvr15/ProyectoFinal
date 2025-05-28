import csv

def guardar_a_csv(self, archivo="rutas.csv"):
    with open(archivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["destino", "distancia"])  # Cabecera
        actual = self.cabeza
        while actual:
            writer.writerow([actual.ruta.destino, actual.ruta.distancia])
            actual = actual.siguiente

def cargar_desde_csv(self, archivo="rutas.csv"):
    try:
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Saltar cabecera
            for row in reader:
                self.agregar_ruta(Ruta(row[0], float(row[1])))
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado.")