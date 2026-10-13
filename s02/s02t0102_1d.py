# importanto el modulo array de
# la biblioteca array y reenombrando como arr
from array import array as arr

def print_array(input):
    print("[",end="")
    for elememt in input:
        print(elememt,end=',')
    print("\b]")   

my_array = arr('i',[5,10,15,20])
print_array(my_array)

# buscar el elemento 15
number_to_search = 100
counter = 0
print (f"se busca {number_to_search} en el arreglo")
for integer in my_array:    
    if integer == number_to_search:
        print("numero encontrado")
        #sirve para terminar el ciclo
        break
    #incrementamos el contador
    counter += 1
    if counter == len(my_array):
        print("numero no encontrado")
