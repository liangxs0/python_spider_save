from pyquery import PyQuery
doc = PyQuery(filename="demo.html")
li = doc("li:first-child")
print(li)
