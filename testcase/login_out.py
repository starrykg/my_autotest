import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testcase(unittest.TestCase):
    #正常登录退出
    def test_normal_login_out(self):
        global driver
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=option)
        driver.get("http://10.18.11.77:1443")
        #element = driver.find_element(By.ID, "Username")
        #element.click()
        #driver.find_element(By.ID, "username").send_keys("test")
        driver.find_element(By.ID, "password").send_keys("kS123456")
        #driver.find_element(By.XPATH, "//form/button/span[1]").click()
        img = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/form/span/img")

        data = img.screenshot_as_png

        ocr = ddddocr.DdddOcr()
        # 进行验证码识别
        text = ocr.classification(data)
        # 输入验证码
        driver.find_element(By.XPATH, "//input[@placeholder='Verification Code']").send_keys(text)
        # 点击登录
        driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click()

        time.sleep(2)
        print('当前页面title', driver.title)
        print('当前页面url', driver.current_url)
        #找到Admin
        menu = driver.find_element(By.XPATH, "//span[@class='ant-dropdown-trigger action___3ut1O account___1r_Ku']")
        actions = ActionChains(driver)
        #鼠标移动到admin
        actions.move_to_element(menu).perform()

        #找到退出按钮
        hidden_submenu = driver.find_element(By.XPATH, "//span[@class='anticon anticon-logout']")
        #点击退出
        hidden_submenu.click()