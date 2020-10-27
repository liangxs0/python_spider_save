from selenium import webdriver
#基于web窗口的webdriver的属性来检测
url = "https://antispider1.scrape.cuiqingcai.com/"
option = webdriver.ChromeOptions()#chrome浏览器工具对象
option.add_experimental_option(
    'excludeSwitches',
    ['enable-automation']
)
option.add_experimental_option("useAutomationExtension", False)
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {'source':'Object.defineProperty(navigator, "webdriver",{get: () => undefined})'})
browser.get(url)
import time
time.sleep(5)
browser.close()

