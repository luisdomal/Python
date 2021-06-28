#Los Diccionarios siempre tienen una llave y un valor
#Mutable
#No se puede actualizar la llave
persona = {"nombre": "Luis", "edad": 34, "vacunado": True}

print(persona["nombre"])

#Modificar

persona["nombre"] = "Juanito"
print(persona)

#Eliminar llaves

del persona["vacunado"]
print(persona)

#Agregar llaves
otro = {"direccion": "Balcon Español 107"}
persona.update(otro)
print(persona)

persona["telefono"] = 4423227630
print(persona)

#Obtener los elementos del diccionario como tuplas
print(persona.items())
#Obtener los valores
print(persona.values())
#Obtener las llaves
print(persona.keys())

