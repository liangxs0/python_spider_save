import re

str1 = "hello 123 world 1234 lxs"
str2 = " lxsd s"
content1 = re.findall("\d+", str1)
content2 = re.findall("\d+", str2)
print(content1,content2)
