import pymongo

client = pymongo.MongoClient(
    "mongodb://localhost:27017"
)
db = client["class"]
collection = db["students"]
res1 = collection.find({"name":"鲁班大师"})
# print(res1)
res2 = collection.find_one({"name":"鲁班大师"})
# print(res2)
# print(type(res2))
#多条查询
res3 = collection.find({"age":3})
for res in res3:
    pass
    # print(res)

#查找年纪大于20岁的
res5 = collection.find({"age":{"$gt":3}})
for res in res5:
    pass
    # print(res)

#计数
count = collection.count_documents({"age":{"$gt":3}})
# print(count)
#排序 pymongo.ASCENDING升序
#排序 pymongo.DESCENDING降序
res01 = collection.find().sort("age", pymongo.ASCENDING)
# for res in res01:
#     print(res)
# print([res["name"] for res in res01])

#偏移
res02 = collection.find().sort("age",pymongo.ASCENDING).skip(2).limit(2)
print([res["name"] for res in res02])
#注意在数据量大的时候，比如说数据以千万，百万。。的数据时，不要使用大数据偏移量，很容易导致内存溢出，这个时候要查询时尽量使用条件查询
#比如
from bson.objectid import  ObjectId
res03 = collection.find({"_id":{"$gt":ObjectId("5f4475c1b78b94ae55df4f1a")}})
print([res["name"] for res in res03])
