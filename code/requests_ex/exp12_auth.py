import requests
from requests.auth import HTTPBasicAuth
url = "http://httpbin.org/basic-auth/liangxs/123"
response = requests.get(url, auth=HTTPBasicAuth("liangxs", "1234"))
print(response.status_code)
print(response.text)
res = requests.get(url, auth=("liangxs", "123"))
print(res.status_code)
print(res.text)
