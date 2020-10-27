import re
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <a href="hhhhhh"></a>
</head>
<body>

</body>
</html>
'''
conten = re.findall("<a.*</a>", html)
print(conten)
conten_s = re.sub("<a|</a>|>","",conten[0])
print(conten_s)