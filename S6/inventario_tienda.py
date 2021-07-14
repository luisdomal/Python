class Producto:
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio

  def __str__(self):
    return "{} - ${}".format(self.nombre, self.precio)

inventario = []

def agregar_producto():
  print("Ingresa el nombre:")
  nombre = input()
  
  print("Ingresa el precio:")
  precio = input()

  inventario.append(Producto(nombre, precio))
  almacenar_producto(nombre, precio)
  print("\nProducto agregado")

def ver_productos():
  print("Inventario:\n")
  for producto in inventario:
    print(producto)

# 1. Cargar el inventario del archivo "inventario.txt"
def cargar_productos():
  with open("archivos/inventario.txt") as archivo:
    lineas = archivo.read().splitlines()
    for linea in lineas:
      linea_split = linea.split("|")
      inventario.append(Producto(linea_split[0], linea_split[1]))

# 2. Almacenar el inventario en el mismo archivo
def almacenar_producto(nombre, precio):
  with open("archivos/inventario.txt", "a") as archivo:
    archivo.write("\n{}|{}".format(nombre, precio))

salir = False

cargar_productos()

while not salir:
  print("\n")
  print("1. Agregar productos")
  print("2. Lista de productos")
  print("3. Salir")

  opcion = input()

  print("\n")

  if opcion == "2":
    ver_productos()
  elif opcion == "1":
    agregar_producto()
  elif opcion == "3":
    salir = True
  else:
    print("Opción inválida")

print("Cerrrando sistema")