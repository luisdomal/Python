print("¿Que toping quieres?: ")
print("* oreo")
print("* fresas")
print("* m&m")
print("* brownie")

toping = input()

if toping == "fresas":
    print("El precio es de $22.00")
elif toping == "oreo":
    print("El precio es de $19.00")
elif toping == "m&m":
    print("El precio es de $25.00")
elif toping == "brownie":
    print("El precio es de $28.00")
else:
    print("El toping no esta disponible")