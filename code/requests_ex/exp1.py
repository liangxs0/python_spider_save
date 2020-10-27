import requests

response = requests.get(url="http://www.zongheng.com/")
print(type(response))
print(response.text)
