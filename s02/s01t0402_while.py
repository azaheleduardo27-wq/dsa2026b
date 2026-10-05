"""""
escribir un programa que calcule
 la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculara la suma del 1 al 100
42 usando un ciclo while
"""
# importar la binlioteca de tiempo
import time
n = 100
the_sum = 0


#Crear variables para 
#el problema

#tomando el tiempo 1
timestamp_01 = time.time()

#iniciando la suma
# 100
while(n > 0 ):
    the_sum = the_sum + n # 100 + 99 + 98 ... + 1
    n = n - 1
#tomamos el t2
timestamp_02 = time.time()

#imprimir la solucion
print(f"la suma es (the_sum)")


#calculando el tiempo
elapsed_time = round ((timestamp_02-timestamp_01) * 1e6,2)
print(f"tiempo de ejecucion: {elapsed_time} us")
