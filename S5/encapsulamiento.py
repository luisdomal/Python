#Los atributos nombre, edad y vacunado son prublicos.


class Persona:
    nombre= "Luis"
    edad= 34
    vacunado= False

    def presentate(self):
        print("Hola me llamo", self.nombre)
    
luis = Persona()

#Sobreescribiendo el valor del atributo "nombre".
luis.nombre = "Paquito"

luis.presentate()

class CuentaBancaria:
    _monto= 0
    def __init__(self, abonoInicial):
        self._monto = abonoInicial
    def abonar(self, abono):
        self._monto = self._monto + abono
    def estado_cuenta(self):
        print(self._monto)



guardadito = CuentaBancaria(50)
guardadito.abonar(100)
guardadito.estado_cuenta()

#De esta manera la variable ya es privada y no se puede acceder de forma externa.
#Los atributos privados no se heredan, siempre se quedan en la clase original se tiene que declarar con un doble __ "por ejemplo __monto"


#guardadito.__monto(10000)

#Atributos protegidos (Protected)pueden ser leidos y actualizado dentro dela misma clase y sus herencias pero no desde afuera. estos se declaran con un _ por ejemplo "_monto"

class CuentePremium(CuentaBancaria):
    def __init__(self):
        super().__init__(10000)
    def estado_cuenta_premium(self):
        print("Usuario premium su estado de cuenta es:", self._monto)

premium = CuentePremium()
premium.estado_cuenta_premium()


"""
Ejercicio: Diseñar una maquina expendedora de Dulces
"""

class Articulos:
    def __init__(self, codigo, descripcion, cantidad, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        return "Codigo {}, Prodcuto {}, Cantidad {}, costo ${}".format(self.codigo, self.descripcion, self.cantidad, self.precio )


class MaquinaExpendedora:
    def __init__(self):
        self.__producto = []
    def agregar_producto(self, codigo, descripcion, cantidad, precio):
        self.__producto.append(Articulos(codigo, descripcion, cantidad, precio))
    def ver_producto(self):
        for maquina in self.__producto:
            print(maquina)
    def comprar_producto(self, codigo):
        for producto in self.__producto:
            if codigo == producto.codigo:
                print("El total articulo comprado es: {}".format(producto.precio))

maquina = MaquinaExpendedora()

maquina.agregar_producto("A01", "Chocolate", 20, 20)
maquina.agregar_producto("A02", "Dona", 5, 15)
maquina.agregar_producto("A03", "Galleta", 10, 10)

maquina.ver_producto()
maquina.comprar_producto("A02")