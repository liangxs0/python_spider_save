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
        </ul>
    </div>
<div id="container2">
        <ul class="list2">
            <li class="item2-0">first line</li>
            <li class="item2-1">second line</li>
            <li class="item2-0 active"><a href="http://httpbin.org">third line</a></li>
            <li class="item2-1 active"><a href="https://www.baidu.com/"><span class="des">fourth</span></a></li>
        </ul>
    </div>
</body>
</html>
'''

from pyquery import PyQuery

doc = PyQuery(html)
items = doc(".list")
parents = items.parents()
daye = parents.find("#container2")
print(daye)

