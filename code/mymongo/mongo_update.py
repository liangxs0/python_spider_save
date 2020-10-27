import pymongo
condtion = {"age":{"$gt":3}}
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["class"]
collection = db["students"]
# student = collection.find_one({"name":"小鲁班"})
# student["age"] = 25
# result = collection.update({"name":"小鲁班"}, student)
# print(result)
res = collection.update_many(condtion,{"$inc":{"age":1}})
print(res)