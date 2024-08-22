

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#定位元素(好封装)
#driver.find_element(By.ID, "kw").send_keys("必应")
#driver.find_element(By.NAME, "wd").send_keys("必应")
#driver.find_element(By.LINK_TEXT, "新闻").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "闻").click()
#driver.find_element(By.XPATH, "//form/span[1]/input").send_keys("必应")
#driver.find_element(By.XPATH, "//input[@autocomplete='off']").send_keys("必应")
#driver.find_element(By.XPATH, "//*[@autocomplete='off']").send_keys("必应")
#driver.find_element(By.XPATH, "//*[@*='off']").send_keys("必应")
#相对路 + 部分属性定位
#driver.find_element(By.XPATH, "//*[starts-with(@autocomplete,'of')]").send_keys("必应")
#driver.find_element(By.XPATH, "//*[substring(@autocomplete,2)='ff']").send_keys("必应")
#driver.find_element(By.XPATH, "//*[contains(@autocomplete,'of')]").send_keys("必应")

value = driver.find_element(By.XPATH, "//span[text()='按图片搜索']").get_attribute("class")
print("xxxxxxxxx",value)