from pyquery import PyQuery
doc = PyQuery(filename="demo.html")
lis = doc("li")
for li in lis.items():
    print(li.text())