from urllib.parse import urljoin
from selenium import webdriver
import requests
import time

base_url = "https://login2.scrape.cuiqingcai.com/"
login_url = urljoin(base_url, "login")
index_url = urljoin(base_url, "page/1")
username = "admin"
password = "admin"

browser = webdriver.Chrome()
browser.get(login_url)
browser.find_element_by_css_selector('input[name="username"]').send_keys(username)
browser.find_element_by_css_selector('input[name="password"]').send_keys(password)
browser.find_element_by_css_selector('input[type="submit"]').click()
time.sleep(2)
cookies = browser.get_cookies()#获取cookies
browser.close()
session = requests.session()
for cookie in cookies:
    session.cookies.set(cookie["name"], cookie["value"])
res = session.get(index_url)
print(res.url)