from selenium import webdriver
import time
#构建webdirver的对象
browser = webdriver.Chrome()
url = "http://www.zongheng.com/"
browser.get(url)
time.sleep(3)
#定位
point = browser.find_element_by_css_selector('[title="奇幻玄幻"]')
#文本获取
print(point.text)
print("location:",point.location)
print("tag_name:",point.tag_name)
print("size:",point.size)
print("id:",point.id)
browser.close()