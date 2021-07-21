from minmax import min_max
import pytest

@pytest.mark.parametrize('digito', [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
])
def test_un_numero(digito):
  assert min_max(digito) == { "min": digito, "max": digito }

@pytest.mark.parametrize('a, b', [
  (0, 1), (10, 20), (50, 100), (-300, -200), (-1, 1)
])
def test_dos_numeros_ordenados(a, b):
  assert min_max(a, b) == { "min": a, "max": b }

@pytest.mark.parametrize('a, b', [
  (1, 0), (-1, -3), (1000, 1), (50, 20)
])
def test_dos_numeros_desordenados(a, b):
  assert min_max(a, b) == { "min": b, "max": a }

@pytest.mark.parametrize('lista, resultado', [
  ([1,2], { "min": 1, "max": 2}),
  ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], { "min": 1, "max": 1 }),
  ([123,12,543,53,654,2433,12,123,324,324,453564], { "min": 12, "max": 453564})
])
def test_cualquier_cantidad(lista, resultado):
  assert min_max(*lista) == resultado