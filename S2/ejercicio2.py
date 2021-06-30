# Ejercicio 02. Fizzbuzz
# Crear una funciona llamada "fizzbuzz" que reciba como parámetro una lista de enteros posiitivos y que calcule lo siguiente:
# Por cada elemento de la lista:
# * Si N es divisible entre 3, poner en pantalla "Fizz"
# * Si N es divisible entre 5, poner en pantalla "Buzz"
# * Si N es divisible entre 3 y 5, poner en pantalla "FizzBuzz"
# * Si N no es divisible entre 3 o 5, poner en pantalla el número
# fizzBuzz([1,2,3,4,5,15])
# 1
# 2
# Fizz
# 4
# Buzz
# FizzBuzz
# Tip: Módulo
# """

def fizzbuzz(list):
    for i in list:
        if(i % 3 == 0) and (i % 5 == 0):
            print("Fizzbuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)

lista = [1,2,3,4,5,15]

fizzbuzz(lista)
