import requests
from selenium import webdriver
url = "https://maoyan.com/films?showType=3&offset=90"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
#            "Cookie": 'uuid_n_v=v1; uuid=4A26E890F0A711EA886C81724AFA0D3B71DF51E8BEAC4C4888FFA9A668324191; mojo-uuid=fa3a2218b47d41f0fa7d5ae84fa00ce9; _lxsdk_cuid=174661fd28cc8-0e5978185aa7c5-f7b1332-144000-174661fd28cc8; _lxsdk=4A26E890F0A711EA886C81724AFA0D3B71DF51E8BEAC4C4888FFA9A668324191; _csrf=b1053ea50f4d88ed9993a423769ea8e1bcdca15a4abc3f48efa7f82cddaf2334; mojo-session-id={"id":"66b0414aa367fce941ec1fe2fd01c8c3","time":1599618642342}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1599441195,1599618642; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; mojo-trace-id=11; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1599618685; __mta=43473562.1599441197994.1599618681399.1599618685480.17; _lxsdk_s=17470b37295-98e-e71-f78%7C%7C14'}
# res = requests.get(url,headers=headers)
# print(res.text)
browser = webdriver.Chrome()
browser.get(url)
import time
time.sleep(5)
print(browser.page_source)
browser.close()