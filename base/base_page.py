from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#是否后台运行
Silence = False
#测试服务ip等信息
Ip = '10.18.1.185'

Pwd = "kS123456"
UserName = "admin"
LoginUrl = "http://" + Ip + ":1443"
TAB = ["Basic", "SM NAS", "N4", "S5", "SBI", "DNN Config", "Service", "Features"]
LAB = ["PLMN", "LOG", "ID", "N4 CP", "N4 UP", "URR Rules", "BAR Rules", "Qos Data", "PCC Rules", "Applications"]
NF = ["SMF"]
ALL = True


class BasePage(unittest.TestCase):

    def __init__(self):
        global driver
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--ignore-certificate-errors')
        self.option.add_argument('--no-sandbox')
        #self.option.add_argument('--disable-dev-shm-usage')
        #self.option.add_argument('--disable-extensions')
        if Silence:
            self.option.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.maximize_window()
        self.driver.get(LoginUrl)

    # 定位元素的关键字
    def locator_element(self, loc):
        print("locator_element",loc)
        # 加*号解包
        return self.driver.find_element(*loc)

    # 定位元素的关键字,多个匹配
    def locator_elements(self, loc):
        print("locator_element",loc)
        # 加*号解包
        return self.driver.find_elements(*loc)

    # 设置值的关键字
    def set_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 鼠标移动到
    def mouse_over(self, loc):
        menu = self.locator_element(loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu).perform()

    # 显式等待
    def web_driver_wait(self, loc):
        ele = WebDriverWait(self.driver, 5).until(
            lambda _: self.locator_element(loc)
        )

    # 获取标题
    def get_driver_title(self):
        return self.driver.title

    # 设置url到当前
    def set_driver_url(self):
        self.login_url = self.driver.current_url
        return self.login_url

    # 获取url到当前
    def get_driver_url(self):
        return self.driver.current_url

    # 获取截图 todo
    def get_screenshot_as_base(self, url):
        self.driver.get(url)
        return self.driver.get_screenshot_as_base64()

    # 先全选，再删除
    def clear_data(self, in_put):
        try:
            in_put.click()
            in_put.send_keys(Keys.CONTROL, "a")
            in_put.send_keys(Keys.DELETE)
        except:
            print("clear_data fail")
    # 跳转窗口
    def set_driver_switch(self, handles_index):
        self.driver.switch_to.window(handles_index)
