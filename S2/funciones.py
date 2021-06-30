#Buenas practicas "DRY" (Don't repeat yourself)

def mi_primer_funcion():
    print("mi_primer_funcion")

#Invocar una funcion

mi_primer_funcion()

#Las funciones reciben parametros
def saluda(nombre):
    print("Hola, {}".format(nombre))

saluda("Luis")

def suma(num1, num2):
    return num1 + num2

resultado = suma(1,2)
print(resultado)

print("5 + 5 = {}".format(suma(5,5)))

# Ejercicio 1. 
#     Crear una funcion que reciba como parametro una lista de números
#     Y regresar la suma de todos sus elementos

list1 = [1,2,3,4,5]
print(list1)


def suma_lista(lista):
    result = 0
    for i in lista:
        result = i + result
    return result

print(suma_lista(list1))
print("El resultado de la suma de la lista es: {}".format(suma_lista(list1)))


# Ejercicio 03. Crear las siguientes funciones:
#   Los humanos tienen 10 bases
#   Los marcianos atacan 1 base a la vez
#   Las bases no pueden ser atacadas mas de una vez
#   attack(3) -> Destruir la base 3
#   attack(5) -> Destruir la base 5
#   game_over() -> False, quedan las bases 1 2 4 6 7 8 9 10
#   attack(1)
#   attack(2)
#   attack(10)
#   attack(8)
#   game_over() -> False, quedan las bases 4 6 7 9
#   attack(4)
#   attack(6)
#   attack(7)
#   attack(9)
#   game_over() -> True
#   El objetivo es implementar dichas funciones
#   Por último:
#   attack(3.5) -> Atacaria la mitad de la base 3
#   attack(4.2) -> Atacando el 20% de la base 4 y queda el 80%
#   attack(4.6) -> Atacando el 60% de la base 4 y queda el 20%
#   attack(4.2) -> Destruyo la base 4
#   attack(5) -> Destruye al 100% la base 5

