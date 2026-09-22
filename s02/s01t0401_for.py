"""
escribir un programa que calcule
 la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculara la suma del 1 al 100
42
"""
# importamos biblioteca time
import time

#tomando el tiempo inicial
timestamp_01 = time.time()

#programa que calcula las sumas
# de los "n" numeros naturales
n = 100
total_sum = 0

#ciclo for
for number in range(1,n+1):
    total_sum = total_sum + number
    # 1: suma = 0 + 1
    # suma = 1
    # 2: suma = 1 + 2
    # sum = 3
    # 3: sum = 3 + 3
    # ...
    # 100: sum = valor anterior suma + 100
print(f"La suma de 1 hasta {n} es: {total_sum}")
# tomando el tiempo final
timestamp_02 = time.time()

#impresion del tiempo de ejecucion
print(f"tiempo de ejecucion {(timestamp_02-timestamp_01) * 1e6:.2f} μs")