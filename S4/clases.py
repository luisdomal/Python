
"""
    Las clases son una plantilla que describe a un objeto (entidad, modelo, cosa)
"""

class MiPrimerClase:
    pass

"""
    Los objetos son instancias de una clase
    Instancia -> Referencia de Memoria
"""

miPrimerObjeto = MiPrimerClase()
#print(miPrimerObjeto)

class moneda1:
    #Atributos de la clase
    valor = 1

class moneda2:
    valor = 2

class moneda5:
    valor= 5

class moneda10:
    valor= 10

#Notacion -> Acceder atributos o metodos (objeto.algo)
Moneda1 = moneda1()

print(Moneda1.valor)

class Moneda:
    """
    Constructor de una clase es una funcion especial que se ejecuta SIEMPRE al momento de 
    crear una instancia del objeto.
    """
    def __init__(self, valor):
        print("Ejecutando el constructor de la clase moneda")
        self.valor = valor

moneda = Moneda(10)

class Monedero:
    def __init__(self):
