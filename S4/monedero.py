class Moneda:
    def __init__(self, valor = 1):
        self.valor = valor
    #Ayuda a dar un formato o interpretacion en texto de un objeto
    def __str__(self):
        return "${}".format(self.valor)

#Agregación: Reutilizar objetos dentro de otros objetos.
class Monedero:
    def __init__(self):
        self.monedas = []
    #Acción (método)
    def agregar_moneda(self, valor):
        self.monedas.append(Moneda(valor))
    
    def ver_monedas(self):
        for moneda in self.monedas:
            print(moneda)
    def monto_total(self):
        total = 0
        for moneda in self.monedas:
            total = total + moneda.valor
        return total


monederito = Monedero()

monederito.agregar_moneda(10)
monederito.agregar_moneda(5)
monederito.agregar_moneda(20)

monederito.ver_monedas()

print(monederito.monto_total())

"""
Ejercicio: Implementar un código que simule un carrito de compra
"""
print("Ejercicio Carrito de compra  =====>")

class Producto:
    def __init__(self, producto, valor = 1):
        self.valor = valor
        self.producto = producto
    def __str__(self):
        return "Producto: {} Costo ${}".format(self.producto, self.valor)

class Carrito:
    def __init__(self):
        self.productos = []
    #Acción (método)
    def agregar_producto(self, producto, valor):
        self.productos.append(Producto(producto, valor))
    def ver_productos(self):
        for carrito in self.productos:
            print(carrito)
    def total_pago(self):
        total = 0
        for total_carrito in self.productos:
            total = total + total_carrito.valor
        return "El total a pagar es de: ${}".format(total)

mi_carrito = Carrito()

mi_carrito.agregar_producto("Manzana", 20)
mi_carrito.agregar_producto("Platano", 15)
mi_carrito.agregar_producto("Carne de Res", 80)
mi_carrito.agregar_producto("Pescado", 50)
mi_carrito.agregar_producto("Arroz", 5)
mi_carrito.agregar_producto("Camaron", 120)
mi_carrito.agregar_producto("Vino", 100)

mi_carrito.ver_productos()

print(mi_carrito.total_pago())
