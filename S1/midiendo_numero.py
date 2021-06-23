print("Ingresa un número: ")
n = input()
num = int(n)

#Importante: Python es un lenguaje identado

if num < 0:
    print("{} es un número negativo".format(num))
elif num > 0:
    print("{} es un número positivo".format(num))
else:
    print("El número es 0")
