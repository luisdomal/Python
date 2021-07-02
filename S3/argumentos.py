def mi_primer_funcion():
    print("Hola mundo")

mi_primer_funcion()

print("imprimiendo solo con un argumento")

def saluda(nombre):
    print("Hola {}".format(nombre))

saluda("Jorge")

#Metiendo una lista

print("imprimiendo con una lista")

def saluda2(nombres):
    for nombre in nombres:
        print("Hola {}".format(nombre))

saluda2(["Luis","Jorge","Adrian"])

#Utilizando varios argumentos

print("Imprimiendo varios argumentos con *args")

def saluda3(*nombres):
    for nombre in nombres:
        print("Hola {}".format(nombre))

saluda3("Fernando","Luis","Ramon","Adrian")

#Ejercicio 1

#Escribir una funcion que reciba una cantidad indeterminada de números y regrese a la suama de todos ellos:

def suma(*numero):
    result = 0
    for i in numero:
        result = i + result
    return result

print("El resultado de la suma 1,2,3,4,5 es: {}".format(suma(1,2,3,4,5)))

#Utilizando separadores en un print

print("utilizando un separado en un print")
print("Juan", "Pablo", "Pepito", "Maria", "Javier",sep= " - ")

#Se pueden mezclar argumentos comunes con args

def imprime_varias_veces(veces, *argv): 
    for i in range(veces):
        for arg in argv:
            print(arg)

  
imprime_varias_veces(3, 'Bienvenidos ', 'a', 'Bedu') 

#Utilizando varios kwargs args
#Podemos poner en los argumentos de la funcion un keywork arg por default si no se presenta en la ejecución de la función

print("utilizando kwargs args")

def saluda3(*nombres, simbolo = "!"):
    for nombre in nombres:
        print("Hola {}{}".format(nombre, simbolo))

saluda3("Fernando","Luis","Ramon","Adrian", simbolo="!!")

#Usamos kwargs para pasar parametros por nombre y no por posicion

def saludo(**kwargs):
    print('Hola {} de {}'.format(kwargs['nombre'], kwargs['empresa']))

saludo(empresa='Bedu',nombre='Luis')
saludo(nombre='Luis',empresa='Bedu')

#Podemos extraer llaves y valores de kwargs como de diccionarios
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
myFun(nombre ='Fernando', empresa ='Bedu', ciudad='CDMX') 


#Ejercicio 2
#Escribir una funcion que reciba una cantidad indeterminada de números y un parametro adicional para especificar la operación (+, -, *)

print("Ejercicio 2")
  
def ejercicio2(operacion, *numero):
    result = 0
    if operacion == '*':
        result = 1
    for i in numero:
        if operacion == '+':
            result += i
        elif operacion == '*':
            result *= i
        elif operacion == "-":
            result -= i
    return result

print("el resultado de la sumatoria es: {}".format(ejercicio2('+',1,2,3,4,5)))
print("el resultado de la multiplicación es: {}".format(ejercicio2('*',1,2,3,4,5)))
print("el resultado de la resta es: {}".format(ejercicio2('-',1,2,3,4,5)))


#Usamos kwargs para pasar parametros por nombre y no por posicion

def describe_persona(**persona):
    print('Hola {} de {} años'.format(persona['nombre'], persona['edad']))

describe_persona(nombre='Luis',edad='34')

#Podemos extraer llaves y valores de kwargs como de diccionarios

def describe_persona2(**persona):
    for key, value in persona.items():
        print(key,value)


describe_persona(nombre='Luis',edad='34')
describe_persona2(nombre='Luis',edad='34', direccion='Balcon Español 107')




