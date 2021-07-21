def extraer_vocales(cadena):
  vocales = ["a", "e", "i", "o", "u"]
  return sorted(list(set(vocales).intersection(set(cadena.lower()))))