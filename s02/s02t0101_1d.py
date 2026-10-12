# array
# from array import *
import array as arr

#creacion de un arreglo
# 1: entero con signo
# I: entero sin signo
# f: numero decimal
# d: numero decimal doble
# u: carcateres unicode
my_array = arr.array('i',[10,22,300,3,7,40,55,80,700,654,35])

# iteracion automatica
#for num in  my_array:
    print(num)

# acceso individual a los elementos
#print(my_array[0]) # primer elemento
#print(my_array[1]) # segundo elemento   
#print(my_array[1]) # tercer elemento  

# tamaño de un arreglo
# Length
#print(len[my_array])

# iteracion por indices
for i in range(len(my_array)):
    if my_array [i]%2==0
       print(f"elemeto num {i+1}:{my_array[i]}")
