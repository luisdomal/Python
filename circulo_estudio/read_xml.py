import xml.etree.ElementTree as ET
import json

tree = ET.parse('dummy.xml')
root = tree.getroot()

# Búsqueda directa de un nodo:
# for node in root.iter("neighbor"):
#  print(node.attrib["name"])


# Accediendo directamente al nodo a través de posiciones
# print(root[1][3].attrib["name"])

# Accediendo al hijo del nodo raíz
#for child in root:
#  print(child)

resultado = []

for country in root:
  #print("\n<country: {}>".format(country.attrib["name"]))
  dict = { "country": {} }

  for child in country:
    
    if "name" in child.attrib:
        #print("<{}: {}>".format(child.tag, child.attrib["name"]))
        dict["country"][child.tag] = child.attrib["name"]

    if child.text:
        #print("<{}: {}>".format(child.tag, child.text))
        dict["country"][child.tag] = child.text

      
  resultado.append(dict)

print(json.dumps(resultado))