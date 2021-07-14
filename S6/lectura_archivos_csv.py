import csv

# Escritura

with open("archivos/padron_electoral_fake.csv", "a") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Juan Perez", "40", "Avenida Reforma #223 Cuautemoc"])

# Lectura de un archivo CSV
with open("archivos/padron_electoral_fake.csv", "r") as archivo:
    reader = csv.reader(archivo)
    for linea in reader:
        print(linea)