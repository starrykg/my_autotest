import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr



class Testcase(unittest.TestCase):
    def test_01_login(self):
        global driver
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=option)
        driver.get("http://10.18.1.184:1443")
        #element = driver.find_element(By.ID, "Username")
        #element.click()
        #driver.find_element(By.ID, "username").send_keys("test")
        driver.find_element(By.ID, "password").send_keys("kS123456")
        driver.find_element(By.XPATH, "//form/button/span[1]").click()
        img = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/form/span/img")

        data = img.screenshot_as_png
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxx",data)

        ocr = ddddocr.DdddOcr()
        # 进行验证码识别
        text = ocr.classification(data)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxx",text)
        #输入验证码
        driver.find_element(By.XPATH, "//input[@placeholder='Verification Code']").send_keys(text)
        #点击登录
        driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click()
    # if __name__ == '__main__':
#     print("###################################")
#     unittest.main()