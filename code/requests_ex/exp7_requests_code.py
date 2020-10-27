import requests

url = "http://httpbin.org/get"

res = requests.get(url)

print(res.status_code)
if res.status_code == requests.codes.ok:
    print("ok")
