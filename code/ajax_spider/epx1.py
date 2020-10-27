import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}

response = requests.get("http://book.zongheng.com/api/book/hotrecommend?bookId=966275&authorId=96&pageNum=1&pageSize=6&catePid=6&_=1598491085479")

data = response.json()["data"]["hotRecommend"]["items"]
for da in data:
    print(da["bookName"])