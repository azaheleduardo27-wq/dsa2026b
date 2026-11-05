"""

Generators

Los generadores son funciones que pueden pausar su ejecucion.

Cuando se invoca una funcion generadora devuelve un objeto generador 

(aka iterador)

El codigo dentro de la funcion se ejecuta unicamente de inmediato, solo se compila.

La funcion se ejecuta unicamente cuando iteras sobre el generador.

"""


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

# se invoca funcion generadora
my_iterador = my_generator()

# Se itera manualmente sobre el generador
# print(next(my_iterador)) #imprime 1
# print(next(my_iterador)) #imprime 2
# print(next(my_iterador)) #imprime 3
# print(next(my_iterador)) #imprime 4

#los iteradores se pueden iterar con un for
for value in my_iterador:
    print(value)

