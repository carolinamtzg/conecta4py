from juego_functions import crea_tablero, juega, esta_llena

# Test 01: probando el tablero:
def test_crear_tablero():
  tab = crea_tablero(4,3)

  assert tab == [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def test_anyadir_ficha_a_tablero():
  tab = crea_tablero(4,3)
  col = 2
  juega(tab, col, "x")

  assert tab == [[0,0,0,0],[0,0,0,0],[0,0,0,"x"]]

  juega(tab, 1, "o")

  assert tab == [[0,0,0,0],[0,0,0,"o"],[0,0,0,"x"]]

def test_comprobar_columna_llena():
  tab = crea_tablero(4,3)
  juega(tab, 2, "x")
  juega(tab, 2, "x")
  juega(tab, 2, "x")
  juega(tab, 2, "x")
  juega(tab, 2, "x")

  assert esta_llena(tab, 2) == True