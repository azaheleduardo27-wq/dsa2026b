"""
escribir un programa que calcule
 la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculara la suma del 1 al 100
42
"""
# importamos biblioteca time
import time
#funcion que suma los 
# primeros "n" numeros naturales
def sum_of_n(n):
    total_sum = 0
    #sumando los "n" numeros
    #ciclo for
    for number in range(1,n+1):
      total_sum = total_sum + number
      #retorno del total de la suma
    return total_sum
# Variable para guardar
# El data set
dataset = [] #(n,time,sum)(n,time,sum)
#generando el contenido de la matset


for repetition in range(1,11):
   # Tomo el tiempo 1
   #tomando el tiempo inicial
   timestamp_01 = time.time()

   #sumo los "n" numeros
   n = repetition*500
   #guardando el resultado en result
   result = sum_of_n(n)

   # tomando el tiempo final
   timestamp_02 = time.time()
   #calculando el tiempo
   elapsed_time = round ((timestamp_02-timestamp_01) * 1e6,2)

   #agregar la tripleta de los
   # datos al dataset
   dataset.append( (n,elapsed_time,result) )

#imprimir el dataset
for tup in dataset:
   print(tup)
