import pymongo
client = pymongo.MongoClient(
    host="127.0.0.1",#host = "localhost"
    port=27017,
)
#这样我们就创建了一个链接对象,以下方法也可以链接
# client = pymongo.MongoClient(
#     "mongondb://localhost:27017"
# )
#指定链接数据库
#db = client.class
db = client["class"]
#指定集合，也就是指定库中的表
# collection = db.students
collection = db["students"]
#插入数据
student = {
    "carid":"101010",
    "name":"曼利湖之父",
    "age":3,
    "gender":"male"
}

# result = collection.insert_one(student)
#运行成功会返回objectid,插入失败会出异常
# print(result)
student2 = {
    "name":"阿古朵",
    "age":12,
}
student3 = {
    "name":"小鲁班",
    "age":7,
}
student4 = {
    "name":"鲁班大师",
    "age":60,
}

result = collection.insert_many([student2,student3,student4])
print(result)