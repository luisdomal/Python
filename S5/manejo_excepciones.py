# Errores lanzados en tiempo de ejecución
# TypeError: Se intenta operar con tipos diferentes
# NameError: No existen variables
# ZeroDivisionError: Que se intento dividir entre 0
# Exception: Un error generico

#Error manual o customizado
#raise: Lanza un error creado desde programación
#raise  Exception("Algo Malo Paso Aqui")

from fibo_decoradores import fibo

print("Ingresa un número para la secuencia de Fibonacci: ")
x = input()

try: #Ejecutar codigo potencialmente peligroso (puede provocar un error)
    resultado = fibo(int(x))
    print("El resultado es: ", resultado)
except ValueError: # Bloque exclusivo para errores de tipo ValueError
    print("Error: Ingresaste un valor que no es un número")
except Exception as error: # Bloque generico (Atrapa cualquier error)
    print(error)

