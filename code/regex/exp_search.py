import re

str = "3123 hello"
# content = re.match("1.*?([a-z]+).*$", str)
# print(content.group(1))
content = re.search("1.*?([a-z]+).*$", str)
print(content.group(1))
