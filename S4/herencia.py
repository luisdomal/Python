class Carrito:
    def __init__(self):
        self.canasta = []

class Refresco:
    def __init__(self,nombre, precio, sabor):
        self.nombre = nombre
        self.precio = precio
        self.sabor = sabor

class Helado:
     def __init__(self, nombre, precio, sabor, presentacion):
        self.nombre = nombre
        self.precio = precio
        self.sabor = sabor
        self.presentacion = presentacion

class Tortillas:
     def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.presentacion = cantidad

Refresco("Coca-Cola", 15, "Cola")
Refresco("Peñafiel", 10, "Agua Mineral")

Helado("Vienetta", 87, "Vainilla", "Pastel")
Helado("Mordisco", 17, "Vainilla", "Galleta")

Tortillas("Tortillinas", 25, 20)
Tortillas("Mateo", 15, 20)