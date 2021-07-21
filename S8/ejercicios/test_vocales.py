from vocales import extraer_vocales
import pytest

def test_sin_vocales():
  assert extraer_vocales("") == []

@pytest.mark.parametrize('texto, resultado', [
  ("papa", ["a"]), 
  ("mama", ["a"]), 
  ("pepe", ["e"]),
  ("zapata", ["a"])
])
def test_una_vocal(texto, resultado):
  assert extraer_vocales(texto) == resultado

@pytest.mark.parametrize("texto, resultado", [
  ("Hola Mundo", ["a", "o", "u"]),
  ("Anita Lava La Tina", ["a", "i"]),
  ("Murcielago", ["a", "e", "i", "o", "u"])
])
def test_palabras_completas(texto, resultado):
  assert extraer_vocales(texto) == resultado