conjunto0 = {1,1,1,1,1,2,2,2,2,3,3,3,3,4}
print(conjunto0)

conjunto1 = {1,2,3,4}
conjunto2 = {3,4,5,6}

print("Conjunto 1 y 2")
print(conjunto1)
print(conjunto2)

#Union
print("La union: ")
print(conjunto1.union(conjunto2))

print("La Intersección: ")
print(conjunto1.intersection(conjunto2))

print("La Diferencia: ")
print(conjunto1.difference(conjunto2))

print("La Diferencia simetrica: ")
print(conjunto1.symmetric_difference(conjunto2))

#Agregar un elemento

conjunto0.add(6)

print(conjunto0)

