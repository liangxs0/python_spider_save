import re

str1 = "2020-1-2 12:10"
str2 = "2020-1-3 12:14"
str3 = "2020-1-4 12:15"
pattern = re.compile("\d{2}:\d{2}", re.I)
cont1 = re.sub(pattern,"",str1)
cont2 = re.sub("\d{2}:\d{2}","",str2)
print(cont1,cont2)