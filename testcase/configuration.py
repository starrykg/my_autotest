import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_helper import debugger
from selenium.webdriver.support.ui import Select


LoggerLevelList = ["info", "debug", "trace", "warn", "error", "fatal", "panic"]
LoggerToFileList = ["1", "0"]


class Testcase(unittest.TestCase):
    #正常登录退出
    def test_normal_login_out(self):
        global driver
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=option)
        driver.get("http://10.18.11.113:1443")
        #element = driver.find_element(By.ID, "Username")
        #element.click()
        ##element.clear()
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

        # 显式等待
        ele = WebDriverWait(driver, 10).until(
            lambda _: driver.find_element(By.LINK_TEXT, "Configuration")
        )

        print('当前页面title', driver.title)
        print('当前页面url', driver.current_url)

        #到config页面
        driver.find_element(By.LINK_TEXT, "Configuration").click()

        # 显式等待
        ele = WebDriverWait(driver, 10).until(
            lambda _: driver.find_element(By.ID, "nfType")
        )

        print('当前页面title', driver.title)
        print('当前页面url', driver.current_url)
        driver.find_element(By.ID, "nfType").click()

        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class = 'ant-select-item ant-select-item-option'  and @title='UDM']").click()
        #op = driver.find_element(By.XPATH, "//div[@class = 'ant-select-item ant-select-item-option'  and @title='UDM']")
        #print('UDM===', op.tag_name)
        #print('UDM===', op.accessible_name)
        #print('UDM===', op)
        #print('UDM===', op.get_attribute("title"))
        #debugger(driver)
        # 显式等待
        #op.click()
        time.sleep(1)
        print('当前页面title', driver.title)
        print('当前页面url', driver.current_url)
        ele = WebDriverWait(driver, 10).until(
            lambda _: driver.find_element(By.LINK_TEXT, "Edit")
        )

        #到udm编辑页
        driver.find_element(By.LINK_TEXT, "Edit").click()
        #debugger(driver)
        time.sleep(2)
        # 显式等待
        ele = WebDriverWait(driver, 10).until(
            lambda _: driver.find_element(By.XPATH, "//div[@class='ant-select ant-select-single ant-select-allow-clear ant-select-show-arrow']")
        )

        driver.find_element(By.XPATH, "//div[@class='ant-select ant-select-single ant-select-allow-clear ant-select-show-arrow']").click()
        option = driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item']")
        print("option===",option)
        print("option===1",option.get_attribute("title"))
        #basic_Level_list
        option = driver.find_elements(By.XPATH, "//span[@class='ant-select-selection-item']")[1]
        print("option=====2",option.text)
        print("option=====3",option.get_attribute("title"))
        #断言
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@title='panic']").click()
        #To File
        driver.find_element(By.XPATH, "//div[@class='ant-select ant-select-single ant-select-allow-clear ant-select-show-arrow']").click()
        driver.find_element(By.XPATH,"//div[@title='1']").click()

        #提交修改
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        #debugger(driver)

        #退出
        #time.sleep(20)
        #driver.quit()