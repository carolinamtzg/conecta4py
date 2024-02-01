from juego_functions import crea_tablero, juega

# Test 01: probando el tablero:
def test_crear_tablero():
  tab = crea_tablero(4,3)

  assert tab == [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def test_anyadir_ficha_a_tablero():
  tab = crea_tablero(4,3)
  tab1 = crea_tablero(6,7)
  juega(tab, 2, "x")

  assert tab == [[0,0,0,0],[0,0,0,0],[0,0,0,"x"]]

  juega(tab, 1, "o")

  assert tab == [[0,0,0,0],[0,0,0,"o"],[0,0,0,"x"]]