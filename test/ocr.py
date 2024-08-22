from selenium import webdriver
import ddddocr
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 实现无可视化界面（固定写法）
chrome_options = Options()

# # 处理SSL证书错误问题
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# 忽略无用的日志
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
browser = webdriver.Chrome()
browser.get("https://support.huawei.com/enterprise/ecareWechat")
# 隐式等待
browser.implicitly_wait(5)
# 处理内嵌html
element = browser.find_element(By.ID, "if_content")
browser.switch_to.frame(element)
# 定位到图片元素
img = browser.find_element(By.XPATH, '//*[@id="imgObj"]')
# 获取图片bytes数据
data = img.screenshot_as_png
# 获取图片base64数据
#data = img.screenshot_as_base64
ocr = ddddocr.DdddOcr()
# 进行验证码识别
text = ocr.classification(data)  # img_bytes=data 这是bytes数据传入时,但在pycharm 会冒黄，我也不清楚为啥
print(text)

#browser.quit()