from pyquery import PyQuery

doc = PyQuery(url="http://www.zongheng.com/")
print(doc("title"))

#以上写法等价于
import requests
doc = PyQuery(requests.get(url="http://www.zongheng.com/").text)
print(doc("title"))