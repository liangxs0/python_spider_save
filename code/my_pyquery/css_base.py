html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>demo</title>
</head>
<body>
    <div id="container">
        <ul class="list">
            <li class="item-0">first line</li>
            <li class="item-1">second line</li>
            <li class="item-0 active"><a href="http://httpbin.org">third line</a></li>
            <li class="item-1 active"><a href="https://www.baidu.com/"><span class="des">fourth</span></a></li>
            <h1>demo</h1>
        </ul>
    </div>
</body>
</html>
'''

from pyquery import PyQuery
doc = PyQuery(html)
print(doc("#container .list li"))
print(type(doc("#container .list li")))
# #container 选中id属性为container的代码块
# .list 选中class属性值为list的代码块
# li 选中li标签

for li in doc("#container .list li").items():
    print(li)
    print(type(li))
    print(li.text())
