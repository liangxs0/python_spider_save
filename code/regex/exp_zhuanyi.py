import re

str = "(hhh).?*/"
content = re.search(r"\(hhh\)\.\?\*\/", str)
print(content)
