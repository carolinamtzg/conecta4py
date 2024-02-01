# Crear tablero con 7 filas y 6 columnas:

def crea_tablero(fila, columna):
  salida =[]
  for element in range(fila):
    lista2 = []
    for i in range(columna):
      lista2.append(0)
    salida.append(lista2)
  return salida

print(crea_tablero(6,7))