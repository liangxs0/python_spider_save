import requests

headers = {
    "Cookie": "cookies_value",
    "User-Agent": "user-angent_value"
}

response = requests.get(url="https://github.com/", headers=headers, timeout=1)

if response.status_code is requests.codes.ok:
    print(response.text)

