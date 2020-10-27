from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
browser.execute_script('alert("to Bottom")')
time.sleep(2)
browser.close()