import unittest
from time import sleep
from XTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class YouTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://cn.bing.com/"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_success(self):
        """测试bing搜索：XTestRunner """
        self.driver.get(self.base_url)
        sleep(2)
        search = self.driver.find_element(By.ID, "sb_form_q")
        search.send_keys("s")
        search.submit()
        sleep(2)

    def test_error(self):
        """测试bing搜索，定位失败 """
        self.driver.get(self.base_url)
        sleep(2)
        self.driver.find_element(By.ID, "sb_form_qxxx").send_keys("python")
        sleep(2)

    def test_fail(self):
        """测试bing搜索，断言失败 """
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "sb_form_q").send_keys("unittest")
        self.assertEqual(self.driver.title, "unittest")

    def test_screenshots(self):
        """测试截图"""
        self.driver.get(self.base_url)
        sleep(2)
        # 元素截图
        elem = self.driver.find_element(By.ID, "sb_form_q")
        self.images.append(elem.screenshot_as_base64)
        # 竖屏截图
        self.images.append(self.driver.get_screenshot_as_base())
        # 最大化截图
        self.driver.maximize_window()
        self.images.append(self.driver.get_screenshot_as_base())


if __name__ == '__main__':
    report = "./reports/selenium_result.html"
    with(open(report, 'wb')) as fp:
        unittest.main(testRunner=HTMLTestRunner(
            stream=fp,
            title='5gc auto test report',
            description=['类型：selenium', '操作系统：linux', '浏览器：Chrome']
        ))