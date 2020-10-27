from pyquery import PyQuery

doc = PyQuery(filename="demo.html")
print(doc("title"))
print(doc("li"))
