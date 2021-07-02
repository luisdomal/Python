# Importar todos archivos o funciones de un documento
# Usando el import as es para asignar una alias

import calculadora as calc

print(calc.suma(1,2))
print(calc.resta(2,4))

# Importar una o varias funciones en específico

from calculadora import division, multiplicacion

print(division(4,4))

# Imporar todas las funciones de un archivo
# Sin especificar las funciones

from calculadora import *

print(modulo(2,2))
