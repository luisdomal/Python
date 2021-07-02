# Haciendo peticiones a librerias externas
# Para intalar una libreria externa necesitamos hacer lo siguiente en terminal "py -m pip install /libreria/"

import requests
from requests.models import Response

url = "https://www.google.com"

response = requests.get(url)
print(response)
print(response.text)