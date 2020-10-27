from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.taobao.com/")
lis = browser.find_elements_by_css_selector(".service-bd li")
for li in lis:
    print(li)
browser.close()
