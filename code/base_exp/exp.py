from urllib.parse import urljoin #拼接url地址

url = "http://www.zongheng.com"
str = "upload/cover/2015/06/1434416579785.jpg"
url_new = urljoin(url, str)
print(url_new)