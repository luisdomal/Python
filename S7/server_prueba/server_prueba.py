from flask import Flask, request


# Crear una aplicación de Flask
# Para correr Flask tenemos que poner en terminal "py -m flask run" adicional tenemos que nombrar el archivo como app.py ó podemos asignar la variable FLASK_APP en un archivo nuevo que nombraremos .flaskenv

app = Flask(__name__)

# Creando la ruta raiz "/"

@app.route("/")

def hello():
    return "Hello World"

# Agregamos la variable FLASK_ENV=development en el archivo .flaskenv para poder actualizar el navegador y corra los cambios.


# Podemos crear las rutas que queramos, simplemente en el navegador vamos a agregar la ruta por ejemplo "http://127.0.0.1:5000/test"
@app.route("/test")
def test():
    return "Esto es una prueba"

# Querystring

@app.route("/suma")
def suma():
    # Acceder a un parametro en Querystring
    #request.args.get('parametro', 'valor por defecto', 'tipo') tambien debemos importar request
    param1 = request.args.get('a', 0, int)
    param2 = request.args.get('b', 0, int)
    resultado = param1 + param2
    return "La suma de {} + {} = {}".format(param1, param2, resultado)

# Querystring ===>  tenemos que usar la url ej "http://127.0.0.1:5000/suma" agregamos un "?" posterior K "parametro"=V 'valor'

# <<===================================================================================================================================================>>

# URL

@app.route("/saluda/<nombre>/<edad>")
def saluda(nombre, edad):
    return "Hola {} de {} años".format(nombre, edad)

#Colocando el parametro entre <> lo hace dinámico
#Consultandolo por url ejemplo "http://127.0.0.1:5000/saluda/Luis/34"

"""
Ejercicio:

Implementar una ruta que a traves de la URL le indique la opeación matemática a realizar y por Query String los operandos.

"""

@app.route("/calculadora/<operador>")
def calculadora(operador):
    param1 = request.args.get('a', 0, int)
    param2 = request.args.get('b', 0, int)
    if operador == "suma":
        return "La Suma de {} y {} = {}".format(param1, param2, param1 + param2)
    elif operador == "resta":
        return "La Resta de {} y {} = {}".format(param1, param2, param1 - param2)
    elif operador == "multiplicacion":
        return "La Multiplicación de {} y {} = {}".format(param1, param1, param1 * param2)
    elif operador == "division":
        if param1 == 0:
            return "ERROR: División entre 0"
        else:
            return "La División de {} y {} = {}".format(param1, param2, param1 / param2)