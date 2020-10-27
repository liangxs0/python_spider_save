import requests

proxies = {
    "https":"https://221.229.252.98:9797",
    "http":"http://221.229.252.98:9797"
}

url = "http://httpbin.org/get"
response = requests.get(url, proxies=proxies)
print(response.text)


