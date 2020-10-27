import requests

headers = {
    "User-Agent": "Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}
url = "http://httpbin.org/get"

response = requests.get(url=url, headers=headers)

print(response.text)
