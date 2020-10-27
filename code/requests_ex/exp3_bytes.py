import requests

url = "http://static.zongheng.com/upload/recommend/ba/5c/ba5cb7104b17c036016a22ba2979d05b.jpeg"

response = requests.get(url=url)

print(response.text)
print(response.content)

with open("favicon.ico", "wb") as f:
    f.write(response.content)