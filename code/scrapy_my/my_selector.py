from scrapy import Selector

body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello world</title>
</head>
<body>

</body>
</html>
"""

selector = Selector(text=body)
title = selector.xpath("//title/text()")
print(title)
print(title.extract_first())
