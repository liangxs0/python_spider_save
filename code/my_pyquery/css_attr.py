from pyquery import PyQuery
doc = PyQuery(filename="demo.html")
a = doc(".item-0.active a")
href = a.attr("href")
href2 = a.attr.href

items = doc("a")
for item in items.items():
    print(item.attr("href"))