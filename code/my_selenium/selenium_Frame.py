import time
from selenium import webdriver
#检测由于当前element
from selenium.common.exceptions import NoSuchElementException
url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser = webdriver.Chrome()
browser.get(url)
browser.switch_to.frame("iframeResult")
try:
    log = browser.find_element_by_class_name("logo")
except NoSuchElementException:
    print("No Logo")
browser.switch_to.parent_frame()#切换到当前页面的父级页面
logo = browser.find_element_by_class_name("logo")
print(logo)
print(logo.text)
