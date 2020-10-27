from pyquery import PyQuery
doc = PyQuery(filename="demo.html")
li = doc(".item-0.active")
print(li)
li.attr("name","lxs")#添加一个name属性，数值值为lxs
print(li)
li.text("changed text")#以覆盖的方式改变原来文本内容
print(li)
li.html('<span class="change">change</span>')#新增html文本
print(li)
