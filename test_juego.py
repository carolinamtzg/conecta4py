from juego_functions import crea_tablero, juega, esta_llena, victoria_vertical, victoria, victoria_horizontal

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

def test_victoria_vertical():
  tab = crea_tablero(6,7)
  assert victoria_vertical(tab, 2, "x") == False
  juega(tab, 2, "x")
  juega(tab, 2, "o")
  juega(tab, 2, "x")
  assert victoria_vertical(tab, 2, "x") == False
  juega(tab, 2, "x")
  assert victoria_vertical(tab, 2, "x") == False
  juega(tab, 2, "x")
  assert victoria_vertical(tab, 2, "x") == False
  juega(tab, 2, "x")
  assert victoria_vertical(tab, 2, "x") == True
  juega(tab, 2, "x")

def test_victoria_vertical_tablero():
  tab = crea_tablero(6,7)
  assert victoria(tab, "x") == False
  juega(tab, 2, "x")
  juega(tab, 2, "o")
  juega(tab, 2, "x")
  juega(tab, 2, "x")
  juega(tab, 2, "x")
  juega(tab, 2, "x")

  assert victoria(tab, "x")
  assert victoria(tab, "o") == False

def test_victoria_horizontal():
  tab = crea_tablero(6,7)
  juega(tab, 0, "x")
  juega(tab, 1, "o")
  juega(tab, 2, "x")
  juega(tab, 3, "x")
  juega(tab, 4, "x")
  juega(tab, 5, "x")
  assert victoria_horizontal(tab, 5, "x")