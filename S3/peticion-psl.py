# Python Standard Library

import http.client

server = "www.google.com"
url = "/"

conn = http.client.HTTPSConnection(server)
conn.request("GET", url)

response = conn.getresponse()
data = response.read()

print("status:", response.status)
print(data)
