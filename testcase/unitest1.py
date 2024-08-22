import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr



class Testcase(unittest.TestCase):
    #登录
    def test_01_login(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://10.18.11.113:8000/")
        element = driver.find_element(By.ID, "username")
        element.click()
        #driver.find_element(By.ID, "username").send_keys("test")
        #driver.find_element(By.ID, "password").send_keys("123456")
        driver.find_element(By.ID, "password").send_keys("kS123456")
        driver.find_element(By.XPATH, "//form/button/span[1]").click()
        img = driver.find_element(By.XPATH, "//img[@data-inspector-line='237']")

        data = img.screenshot_as_png
        ocr = ddddocr.DdddOcr()
        # 进行验证码识别
        text = ocr.classification(data)
        print("验证码===",text)
        #输入验证码
        driver.find_element(By.XPATH, "//input[@data-inspector-line='231']").send_keys(text)
        #点击登录
        driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click()


    # if __name__ == '__main__':
#     print("###################################")
#     unittest.main()