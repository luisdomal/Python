"""
archivo = open("archivos/hello_world.txt", "r")

#Leo una línea
print(archivo.readline())

#IMPORTANTE: Cerrar el archivo

archivo.close()

"""

#Escribiendo en el archivo (Esto sobre escribe todo el archivo)

with open("archivos/hello_world.txt", "w") as archivo:
    archivo.writelines(["Linea 1\n", "Linea 2\n", "Linea 3\n"])

#Agregar una línea sin sobre escribir
with open("archivos/hello_world.txt", "a") as archivo:
    archivo.writelines("Linea 4\n")    

#Leyendo el archivo
with open("archivos/hello_world.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
