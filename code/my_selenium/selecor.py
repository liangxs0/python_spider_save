import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
#打开一个新的选项卡
browser.execute_script("window.open()")
print(browser.window_handles)#获取当前所有窗口的句柄的列表
browser.switch_to.window(browser.window_handles[1])#切换选项卡
browser.get("https://www.taobo.com")
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
time.sleep(2)
browser.close()
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.close()