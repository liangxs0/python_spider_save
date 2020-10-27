import requests

url = "http://www.baidu.com"

response = requests.get(url=url)#发生请求。获取响应

if response.status_code is requests.codes.ok:#判断是否请求成功
    print(response.cookies)
    for key, value in response.cookies.items():
        print(f"{key} = {value}")
        print("{} = {}".format(key,value))

