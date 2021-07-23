import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.discord

cursor = db.users.find()

for documento in cursor:
  print(documento)