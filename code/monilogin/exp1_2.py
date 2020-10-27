import requests
from urllib.parse import urljoin

base_url = "https://login2.scrape.cuiqingcai.com/"
login_url = urljoin(base_url, "login")
index_url = urljoin(base_url, "page/1")
username = "admin"
password = "admin"

data = {"username":username,
        "password":password}

session = requests.Session()
response_login = session.post(login_url, data=data)
cookies = session.cookies
print("cookies:",cookies)
response_index = session.get(index_url)
print(response_index.url)
