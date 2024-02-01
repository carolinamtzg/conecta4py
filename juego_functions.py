def crea_tablero(fila, columna):
  salida =[]
  for element in range(columna):
    lista2 = []
    for i in range(fila):
      lista2.append(0)
    salida.append(lista2)
  return salida

def juega(tablero, columna, valor_ficha):
  # elegir la columna del tablero,
  # recorrer la columna desde atras hacia adelante
  # al encontrar el primer cero, lo sustituyo por valor_ficha

  #c = tablero[columna - 1]
  #for index in range(len(c)-1,-1,-1):
  #  if c[index] == 0:
  #    c[index] = valor_ficha
  #    break

  c = tablero[columna]
  indice = len(c)-1
  while indice >= 0:
    if c[indice] == 0:
      c[indice] = valor_ficha
      break
    indice -= 1
