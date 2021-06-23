print("Ingresa el primer número: ")
a = input()

print("Ingresa el segundo número: ")
b = input()

#Casteo de tipos: Transformar un tipo A en B

numA = int(a)
numB = int(b)

print("El resultado de la suma es: ", numA + numB)

print("Ingresa el tercer número: ")
c = input()

numC = int(c)
numD = numA + numB

print("El resultado de la resta de (a+b)-c es: ", numD - numC)

print("Ingresa el cuarto número: ")
e = input()

numE = int(e)

print("El modulo de ", numD - numC, "Entre e es;",numD % numE)