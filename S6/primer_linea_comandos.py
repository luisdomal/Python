import sys

"""
sys.argv es una lista con todos los argumentos de la línea de comandos

Nota: El primer argumento siempre es el nombre del archivo. (argv[0])

"""

# print(sys.argv[1:]) Cortar desde la posición 1 hasta el final

print("Argumentos", sys.argv)
resultado = 0

for argumento in sys.argv[1:]:
    resultado = resultado + int(argumento)

print(resultado)

