class Carrito:
    def __init__(self):
        self.canasta = []

class Producto:
    def __init__(self, nombre, precio, etiquetas):
        self.nombre = nombre
        self.precio = precio
        self.etiquetas = etiquetas
    def __str__(self):
        return "{} - ${}".format(self.nombre, self.precio)
    def cualquier_metodo(self):
        print("Soy cualquier metodo de Producto")

class Refresco(Producto):
    def __init__(self, nombre, precio, etiquetas, sabor):
        super().__init__(nombre, precio, etiquetas)
        self.sabor = sabor
    def __str__(self):
        return "Refresco sabor {} ==> {}".format(self.sabor, super().__str__())
    def cualquier_metodo(self):
        print("Soy cualquier metodo de refresco")
        super().cualquier_metodo()


class Helado(Producto):
     def __init__(self, nombre, precio, etiquetas, sabor, presentacion):
        super().__init__(nombre, precio, etiquetas)
        self.sabor = sabor
        self.presentacion = presentacion

class Tortillas(Producto):
     def __init__(self, nombre, precio, etiquetas, cantidad):
        super().__init__(nombre, precio, etiquetas)
        self.presentacion = cantidad

class CualquierClase(Refresco):
  def cualquier_metodo(self):
      print("Soy cualquier metodo de cualquier clase")
      super().cualquier_metodo()

print(Refresco("Coca-Cola", 15, 4, "Cola"))
# Producto("Peñafiel", 10, 4, "Agua Mineral")
# Producto("Vienetta", 87, 3, "Vainilla", "Pastel")
# Producto("Mordisco", 17, 3, "Vainilla", "Galleta")
# Producto("Tortillinas", 20, 1, 20)
# Producto("Mateo", 15, 1, 20)

CualquierClase("Cola", "Coca Cola", 15, 4).cualquier_metodo()