html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>demo</title>
</head>
<body>
    <div class="container">
        <ul class="list">
            <li class="item-0">first line</li>
            <li class="item-1">second line</li>
            <li class="item-0 active"><a href="http://httpbin.org">third line</a></li>
            <li class="item-1 active"><a href="https://www.baidu.com/"><span class="des">fourth</span></a></li>
        </ul>
    </div>
</body>
</html>
'''

#引入库
from pyquery import PyQuery

#构造pyquery对象
doc = PyQuery(html)
# print(doc)
# print(type(doc))
# print(doc("li"))
# print(type(doc("li")))
print(doc("title"))
