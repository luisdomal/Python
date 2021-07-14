from sys import argv

def suma(*numeros):
  resultado = 0
  for numero in numeros:
    resultado = resultado + numero
  return resultado

def resta(*numeros):
  resultado = numeros[0]
  for numero in numeros[1:]:
    resultado = resultado - numero
  return resultado

def multiplicacion(*numeros):
  resultado = 1
  for numero in numeros:
    resultado = resultado * numero
  return resultado

def division(*numeros):
  resultado = numeros[0]
  try:
    for numero in numeros[1:]:
      resultado = resultado / numero
    return resultado
  except ZeroDivisionError:
    print("Error: División por 0")
    return 0

# Eliminar el primer argumento y tomar solo los numeros
argumentos = argv[2:]
operacion = argv[1]

numeritos = []

for argumento in argumentos:
  numeritos.append(int(argumento))

if operacion == "+":
  print(suma(*numeritos))
elif operacion == "-":
  print(resta(*numeritos))
elif operacion == "*":
  print(multiplicacion(*numeritos))
elif operacion == "/":
  print(division(*numeritos))
else:
  print("Operación invalida")