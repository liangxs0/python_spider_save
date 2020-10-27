html = '''
<div id="container">
    <p>one line</p>
    lines
</div>
'''
from pyquery import PyQuery
doc = PyQuery(html)
div = doc("#container")
print(div.text())
div.find("p").remove()
print(div.text())

