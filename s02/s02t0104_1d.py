
#importando funcion de array
#del modulo array
#como arr+
from array import array as arr

#importando la funcion de otro
#  archivo
from s02t0102_1d import print_array

my_array = arr.array('i',[2,10,15,20,10])

print("--- Antes de la eliminacion ---")
print_array(my_array)

# eliminacion
try:
 my_array.remove(100)
except:
 print(f"no se encuentra en el arreglo")
print("--- depues de la eliminacion ---")
print_array(my_array)