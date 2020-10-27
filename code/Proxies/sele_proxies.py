from selenium import webdriver
proxy = "127.0.0.1:8080"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://"+proxy)
browser = webdriver.Chrome(options=options)
browser.get("http://httpbin.org/get")
print(browser.page_source)
browser.close()