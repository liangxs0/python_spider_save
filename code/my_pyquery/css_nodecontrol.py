from pyquery import PyQuery
doc = PyQuery(filename="demo.html")
li = doc(".item-0.active")
print(li)
li0 = li.remove_class("active")
print(li0)
li1 = li.add_class("lxs")
print(li1)
