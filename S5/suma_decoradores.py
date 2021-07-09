def negativos (suma):
    def verdadera_implementacion(*numeros):
        numero_filtrado = []
        for numero in numeros:
            if numero > 0:
                numero_filtrado.append(numero)
        return suma(*numero_filtrado)
    return verdadera_implementacion


@negativos

def suma (*numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total

print(suma(1,2,3,4,5,6,7,8,9,10,-100))