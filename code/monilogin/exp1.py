import requests
from urllib.parse import urljoin

base_url = "https://login2.scrape.cuiqingcai.com/"
login_url = urljoin(base_url, "login")
index_url = urljoin(base_url, "page/1")
username = "admin"
password = "admin"

data = {"username":username,
        "password":password}

response_login = requests.post(url=login_url,data=data,
                               allow_redirects=False)
cookies = response_login.cookies
print("cookies:",cookies)
response_index = requests.get(url=index_url,cookies=cookies)
print("response status:",response_index)
print("response url",response_index.url)
