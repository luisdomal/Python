# Decorador es una funcion que regresa una funcion antes de otra funcion
# En Python las funciones son de orden superior: Funciones que reciben funciones y regresan funciones.
# El decorador tiene que regresar una funcion que sustituye a la original

def mi_primer_decorador(f):
    print("Ejecutando mi primer decorador")
    def funcion_dummy():
        print("Esto es una funcion dummy")
        hello_world()
    #Este return sustituye la implementación de la funcion original
    return funcion_dummy

@mi_primer_decorador

def hello_world():
    print("Hello World")

hello_world()