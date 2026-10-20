
from array import array as arr
 #impresion de una tabla
def print_table  (input_table):
     for row in input_table:
       for column in row:
         print(column, end=",")
       print("\b ")

table=[
   arr('i',[1,2,3]),
   arr('i',[4,5,6]),
   arr('i',[7,8,9])
]
#imprimiendo cada elemento
for row in table:
 for column in row:
        print(column, end=" ")
 print("\b ")

#inserccion
row = 1
column = 2
value = 99

#insertar en la fila 1 columna 2 el valor 99
table[row].insert(column, value)

#imprimiendo mensaje
print("------Despues de la insercion de fila----")
print_table(table)#DRY

#insertando una fila completa
new_row = arr(   arr('i',[100,200,300]),)
pos = 1
table.insert(pos, new_row)

#imprimiendo mensaje
print("------Despues de la insercion de fila----")
print_table(table)

# eliminacion de elementos
del table[2]

#imprimiendo mensaje
print("------Despues de la eliminacion de fila 2----")
print_table(table)
