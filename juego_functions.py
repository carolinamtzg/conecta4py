# el tablero esta definido como una lista de columnas:

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

def esta_llena(tablero, columna):
  # seleccionar la col que queremos comprobar
  # comprobar si la columna tiene huecos con un in
  # devolver True o False
  c = tablero[columna]
  return 0 not in c

# TAREA:
# El tablero debe detectar si se ha producido una victoria. Hay 3 tipos de victorias:
# Vertical: Comprobar una columna con 4 fichas seguidas iguales
# Horizontal: Comprobar en una fila
# Diagonal ascendente o descendente.
# Hacer test y funcion de victoria vertical y si podeis avanzar las otras

def victoria_vertical(tablero, pos_columna, valor_ficha):
  counter_iguales = 0
  columna = tablero[pos_columna]
  ix = 0
  while ix < len(columna):
    if columna[ix] == valor_ficha:
      counter_iguales += 1
    else:
      counter_iguales = 0
    if counter_iguales == 4:
      return True
    ix += 1
  return False

def victoria_horizontal(tablero, pos_fila, valor_ficha):
  counter_iguales = 0

  for columna in tablero:
    if columna[pos_fila] == valor_ficha:
      counter_iguales += 1
    else:
      counter_iguales = 0
    if counter_iguales == 4:
      return True
  return False


def victoria(tablero, valor_ficha):
  #obtener el num de col de mi tablero
  num_de_col = len(tablero)
  #iterar sobre range(num_col)
  for col_index in range(num_de_col):
    if victoria_vertical(tablero, col_index, valor_ficha):
      return True
  return False
