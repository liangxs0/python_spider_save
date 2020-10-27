from selenium import webdriver
url = "http://book.zongheng.com/book/966275.html"
browser = webdriver.Chrome()
browser.get(url)
import time
time.sleep(7)
print(browser.current_url)
print(browser.page_source)
browser.close()

