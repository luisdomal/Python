#Importamos modulo que posee clases para fecha
import datetime

#Se crea un objeto date con fechas determinadas
fecha = datetime.date(1937, 10, 8)  #year, month, day
print(fecha)

#Al preguntar el tipo del objeto devuelve clase fecha
print(type (fecha))

#Podemos acceder a elementosdentro del objeto
mes = fecha.month
anyo = fecha.year
print("el mes es:" , mes)
print("el año es ", anyo)

#Las clases también contienen métodos, o funciones asociadas al comportamiento de la clase
print(fecha.strftime("%b %d %Y %H:%M:%S")) #Devuelve una cadena de texto con la fecha

#Para crear una clase usamos la palabra reservada class
#Para crear metodos usamos def
#self se refiere a los elementos(atributos y metodos) de la misma clase
class persona():
    def asignar_nombre(self,nombre):
        self.nombre = nombre
    def saluda(self):
        print("hola, soy {}".format(self.nombre))

#Crea objetos de clase persona
doctor = persona()
ingeniero = persona()

#Asignar a atributos
ingeniero.nombre = 'Gabriel'


#Usa Metodos de clase
doctor.asignar_nombre('Miguel')

#Accede a atributos
print(doctor.nombre)

ingeniero.saluda()
doctor.saluda()

#Reto 1

barco = Vehiculo()
barco.ruedas=0
barco.velocidad='lenta'
barco.medio = 'agua' 
barco.describir()

Avion = Vehiculo()
Avion.ruedas=4
Avion.velocidad='rapido'
Avion.medio = 'aire' 
Avion.describir()

auto = Vehiculo()
auto.ruedas=4
auto.velocidad='media'
auto.medio = 'asfalto' 
auto.describir()