from array import array as arr

# Parametros de mi cuadricula 
rows = 3
columns = 2 * rows - 1

#funcion para imprimir la matriz
def print_matrix(input_matrix):
  for row in input_matrix:
    print(list(row))

#Creando el grid 2d 
matrix  = []
#Construyendo el grid 
for _ in range(rows):
  new_row = arr('i', [0] * columns)
  matrix.append(new_row)

# Validando la construccion del grid 
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

#Calculando el centro de la primera fila
center = columns// 2 #se hace division entera 

#Estableciendo el centro en 1 
matrix[0][center] =1

print_matrix(matrix)
# se calcula el resto de la matrx 
#siguiendo la logica del sipersky gasket

for row in range(1, rows):
  for col in range (0, columns):
    left_upper_cell = 0
    rigth_upper_cell = 0

    #Si la columna donde 
    #estamos es mayor a 0 
    if col >0:
      left_upper_cell = matrix[row-1][col-1]

      #si la columnaesta un lemento antes 
      #del borde derecho 
      if col < columns -1:
        rigth_upper_cell = matrix [row-1][col+1] 

        #Guardando el arreglo
        if left_upper_cell != rigth_upper_cell:
          matrix[row][col] = 1
        else:
          matrix[row][col] = 0

print()
print_matrix(matrix)