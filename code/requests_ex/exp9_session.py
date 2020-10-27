import requests

url = "http://httpbin.org/cookies/set/key/value"
requests.get(url)#设置cookies

#自己在请求我们的cookies

response = requests.get(url="http://httpbin.org/cookies")
print(response.text)

my_session = requests.Session()
my_session.get(url)#利用session先在服务端设置了一个cookies

response = my_session.get(url="http://httpbin.org/cookies")
print(response.text)
