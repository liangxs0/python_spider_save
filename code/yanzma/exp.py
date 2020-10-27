#登录简书
import requests
from hashlib import md5
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

#简书的账号密码
EMAIL = "15383467476"
PASSWORD = "lxs1995104."
#超级鹰的用户名,密码,软件ID,验证码类型
CHAOJIYING_USERNAME = "yuanpangzi"
CHAOJIYING_PASSWORD = "lxs1995104."
CHAOJIYING_SOFT_ID = "f70c3a48cbbe166d95a475ef21029d83"
CHAOJIYING_KIND = 9102

#超级鹰的第三接口类
class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

#简书验证类
class CracToucClick():
    def __init__(self):
        self.url = "https://www.jianshu.com/sign_in"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.chaojiying = Chaojiying_Client(
            CHAOJIYING_USERNAME,
            CHAOJIYING_PASSWORD,
            CHAOJIYING_SOFT_ID
        )

    def __del__(self):
        self.browser.close()

    def open(self):
        '''
        打开网页输出用户名密码
        :return:None
        '''
        self.browser.get(self.url)#打开网页
        #定位账号输入点和密码输入点
        email = self.wait.until(EC.presence_of_element_located((By.ID, "session_email_or_mobile_number")))
        password = self.wait.until(EC.presence_of_element_located((By.ID, "session_password")))
        #填写内容
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_touclick_button(self):
        '''
        获取初始验证按钮，加载验证码图片
        :return:按键
        '''
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sign-in-button")))
        return button

    def get_touclick_element(self):
        '''
        获取验证图片对象
        :return:图片对象
        '''
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "geetest_widget")))
        return element

    def get_position(self):
        '''
        获取验证码位置
        :return: 位置的元组
        '''
        element = self.get_touclick_element()
        time.sleep(2)
        location = element.location
        size = element.size
        print(size,location)
        top,bottom,left,right = location['y']+100, 100+location['y']+size['height'], location['x'],location['x']+size["width"]
        top = int(top)
        bottom = int(bottom)
        left = int(left)
        right = int(right)
        return (top, bottom, left, right)

    def get_screenshot(self):
        '''
        网页截图
        :return:截图对象
        '''
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_touclick_image(self, name="captch.png"):
        '''
        获取图片
        :param name:
        :return:图片对象
        '''
        top, bottom, left, right = self.get_position()
        print("验证码的位置",top, bottom, left, right)
        #截图对象
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((top, bottom, left, right))
        captcha.save(name)
        return captcha

    def get_points(self,captcha_result):
        '''
        解析识别结果
        :param captcha_result:
        :return:
        '''
        groups = captcha_result.get("pic_str").split("|")
        locations = [[int(number) for number in group.split(",")] for group in groups]
        print("locations:", locations)
        return locations

    def touch_click_words(self, locations):
        '''
        点击
        :param locations:
        :return:
        '''
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(
                self.get_touclick_element(), location[0],
                location[1]
            ).click().perform()
            time.sleep(1)


    def touch_click_verify(self):
        '''
        点击验证码
        :return:
        '''
        boutton = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "geetest_commit")))
        boutton.click()

    def login(self):
        '''
        登录
        :return:
        '''
        submit = self.wait.until(EC.presence_of_element_located((By.ID, "_submit")))
        submit.click()
        time.sleep(10)
        print("登录成功")

    def crack(self):
        '''
        入口函数
        :return:
        '''
        self.open()#打开页面
        #获取登录按钮
        button = self.get_touclick_button()
        button.click()
        time.sleep(1)
        #开始获取验证码图片
        image = self.get_touclick_image()
        # bytes_array = BytesIO()
        # image.save(bytes_array, format="PNG")
        # #验证码识别
        # result = self.chaojiying.PostPic(bytes_array.getvalue(), CHAOJIYING_KIND)
        # print(result)
        # locations = self.get_points(result)
        # self.touch_click_words(locations)
        # self.touch_click_verify()
        # #判断是否登录成功
        # try:
        #     success = self.wait.until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "btn write-btn"),"验证成功")
        #     )
        #     print(success)
        # except:
        #     #失败进行重新验证
        #     self.crack()

if __name__ == '__main__':
    crack = CracToucClick()
    crack.crack()





























