from selenium import webdriver

url = "https://www.baidu.com/"
browser = webdriver.Chrome()
browser.get(url)
point = browser.find_element_by_css_selector("#s-top-left")
print(point)
print(point.get_attribute("class"))
print(point.text)
import time
time.sleep(2)
browser.close()