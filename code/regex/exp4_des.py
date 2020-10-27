import re

str = "Hello World"
content = re.match("^([a-z]).*$", str, re.I)
print(content.group(1))

