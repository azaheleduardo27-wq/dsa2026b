#importanto funciona array
#del modulo array y reenombrando
#como arr
from array import array as arr

#importando la funcion de otro
#  archivo
from s02t0102_1d import print_array

my_array = arr.array('i',[2,10,15,20])

print("--- Antes de la insercion ---")
print_array(my_array)

# insercion
my_array.insert(1,90)
my_array.append
print("--- depues de la insercion ---")
print_array(my_array)

print("---despues del append---")
my_array.append(1000)
print_array(my_array)

print("---simular un append con insert---")
my_array.insert(len(my_array),90000)
print_array(my_array)
