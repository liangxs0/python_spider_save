import re

str = """hello world 1234
lxs"""

content = re.match("^hello\w*\s(\w{5})\s(\d{1,4})\s\w{3}$", str, re.S)
if content is not None:
    print(content.group(2))
else:
    print(content)
