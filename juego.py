# Crear tablero con 7 filas y 6 columnas:

#tablero = crea_tablero(6,7)

# salida = [
#  [0,0,0,0,0,0],
#  [0,0,0,0,0,0],
#  [0,0,0,0,0,0],
#  [0,0,0,0,0,0],
#  [0,0,0,0,0,0],
#  [0,0,0,0,0,0],
#  [0,0,0,0,0,0],
#]

# Definir la posicion donde se ocupa la ficha. de primero siempre sera la ultima fila de la matrix
# si la columna esta llena no se puede jugar mas fichas
# Crear jugadores, y asignar una ficha cada uno:

jugador_1 = 1
jugador_2 = 2

# ver si la col tiene hueco, si lo tiene en ese hueco poner la ficha.

def juega(columna, jugador):
  if busca_hueco(columna) == True:
    if jugador == 1:
      print(1)
    elif jugador == 2:
      print(2)
    else:
      print(0)

juega([0,0,0,0,0,0], jugador_1)

# buscar la ultima posicion vacia de la columna: (devuelve un entero)

def busca_hueco(columna):
  for c in columna:
    if c == 0:
      print("vacio")
    else:
      print("ocupado")
    

busca_hueco([0,1,0,0,2,0,0])