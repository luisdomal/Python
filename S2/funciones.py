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



def suma_lista(lista):
    result = 0
    for i in lista:
        result = i + result
    return result

list1 = [1,2,3,4,5]
print(list1)

print(suma_lista(list1))
print("El resultado de la suma de la lista es: {}".format(suma_lista(list1)))

