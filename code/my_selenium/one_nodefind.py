from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.taobao.com/")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
input_thrid = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first)
print(input_second)
print(input_thrid)
input_first.send_keys("猛男")
input_first.send_keys(Keys.ENTER)
import time
time.sleep(6)
browser.close()
