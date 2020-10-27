import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["class"]
collection = db["students"]
# res = collection.delete_one({"name":"梁晓声"})
# print(res)
res2 = collection.delete_many({"age":{"$gt":20}})
print(res2)

