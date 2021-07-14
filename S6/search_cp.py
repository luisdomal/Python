import sys
import csv
import io

#Input código postal a buscar:
cp = sys.argv[1]

resultados = []

#Lectura del archivo
with io.open("archivos/codigos_postales_cdmx.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    for linea in reader:
        if linea[0] == cp:
            resultados.append(linea[1:])

print(resultados)

