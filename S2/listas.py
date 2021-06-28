lista_vacia = []
lista_vacia2 = list()

#Lista Poblada
list1 = [100,200,300,400,500]
print(list1)

#Operaciones

#Lectura de indice
print("list1 en posición 2:")
print(list1[1])

#Agregar elementos
list1.append(600)
list1 = list1 + [700] #Concatenando

print("Despues de agregar 600 y 700: ", list1)

#Agregar elementos a una lista en una posición especifica
list1 = [800] + list1
list1.insert(0, 900)


print("Despues de agregar el 800 y 900: ", list1)

list1.insert(1, 150)
print("Despues de agregar el 150 en la posición 2: ", list1)

#Longitud de una lista
print("Longitud de lista: ")
print(len(list1))

#Actualización
list1[3] = 1000
print(list1)

#Eliminación
del list1[3]
print(list1)

#Buscar
print(list1.index(500))

#Ordenar
print(sorted(list1))

