import requests

url = "http://www.zongheng.com/"

response = requests.get(url)

print("header",type(response.headers),response.headers)
print("status",type(response.status_code),response.status_code)
print("URL",type(response.url), response.url)
print("history",type(response.history),response.history)
print("cookie",type(response.cookies), response.cookies)
