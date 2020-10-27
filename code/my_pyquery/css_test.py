from pyquery import PyQuery
doc = PyQuery(filename="demo.html")
a = doc("a")
print(type(a.html()))
print(type(a.text()))
print(a.text())
print("-"*30)
print(a.html())