import requests

url = "http://httpbin.org/get"
data = {
    "name":"lxs",
    "age":"8888"
}
response = requests.get(url=url, params=data)
print(response.text)