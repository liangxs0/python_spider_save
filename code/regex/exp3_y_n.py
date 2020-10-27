import re
str = "hello world 1234 lxs"
#贪婪匹配
content0 = re.match("^h.*(\d+).*$", str)
content1 = re.match("^h.*?(\d+).*$", str)
content2 = re.match("^h.*?(\d+)\s(.*)",str)
content3 = re.match("^h.*?(\d+)\s(.*?)",str)
print(content2)
print(content3)
