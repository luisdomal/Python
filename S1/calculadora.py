print("Igresa el primero número: ")
a = input()
numA = int(a)
print("Ingresa el segundo número: ")
b = input()
numB = int(b)
print("Selecciona la operación a realizar: ")
print("+ ==> Suma")
print("- ==> Resta")
print("* ==> Multiplicación")
print("/ ==> División")
print("% ==> Modulo")

operacion = input()

if operacion == "+":
    print("La Suma de {} y {} = {}".format(numA, numB, numA + numB))
elif operacion == "-":
    print("La Resta de {} y {} = {}".format(numA, numB, numA - numB))
elif operacion == "*":
    print("La Multiplicación de {} y {} = {}".format(numA, numB, numA * numB))
elif operacion == "/":
    if numB == 0:
        print("ERROR: División entre 0")
    else:
        print("La División de {} y {} = {}".format(numA, numB, numA / numB))
elif operacion == "%":
    print("El modulo de {} y {} = {}".format(numA, numB, numA % numB))
else:
    print("Esa operación no esta soportada")



