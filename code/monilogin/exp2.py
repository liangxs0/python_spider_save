import requests
from urllib.parse import urljoin

base_url = "https://login3.scrape.cuiqingcai.com/"
login_url = urljoin(base_url, "/api/login")
index_url = urljoin(base_url, "/api/book")
username = "admin"
password = "admin"
data = {
    "username":username,"password":password
}
response_login = requests.post(login_url, data=data)
data_json = response_login.json()
print("data_json",data_json)
jwt = data_json.get("token")
print("jwt",jwt)
data_params = {
    "limit":18,
    "offset":0
}
headers = {
    "authorization":f"jwt {jwt}"
}
response_index = requests.get(index_url,params=data_params,headers=headers)
print(response_index.url)
print(response_index.status_code)
print(response_index.json())


