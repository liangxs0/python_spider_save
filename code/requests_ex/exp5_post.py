import requests

url = "http://httpbin.org/post"

data = {
    "type":"post",
    "author":"lxs"
}

files = {
    "files":open("favicon.ico","rb")
}

response = requests.post(url=url, data=data, files=files)

print(response.text)
