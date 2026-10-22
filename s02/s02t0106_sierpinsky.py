from array import array as arr

# parametros de mi cuadricula
rows  = 8
columns = 2 * rows - 1

# Creando el grid 2D
matrix = []
# construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# validando la construccion del grid
print(f"cantidad de filas: {len(matrix)}")
print(f"cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))