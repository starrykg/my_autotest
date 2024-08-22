import time
from base.base_page import *
from selenium.webdriver.common.by import By
import ddddocr
#from webdriver_helper import debugger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import random
import struct
import socket
import redis
import requests


class LoginPage(BasePage):
    """
    # 登录信息
    """
    username_loc = (By.ID, "Username")
    password_loc = (By.ID, "password")
    ver_code = (By.XPATH, "//*[@id='root']/div/div/div[2]/form/span/img")
    send_code = (By.XPATH, "//input[@placeholder='Verification Code']")
    submit_loc = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg']")
    """
    # admin
    """
    admin_menu = (By.XPATH, "//span[@class='ant-dropdown-trigger action___3ut1O account___1r_Ku']")
    hidden_submenu = (By.XPATH, "//span[@class='anticon anticon-logout']")

    NfList = ["Udm", "Amf", "Smf", "Nrf", "Pcf", "Ausf", "Nssf", "Upf"]
    """
    # Configuration
    """
    config = (By.LINK_TEXT, "Configuration")
    config_nf_type = (By.ID, "nfType")
    """
    # 网元名称
    """
    #config_Edit = (By.LINK_TEXT, "Edit")
    config_Edit = (By.XPATH, '//*[@class="ant-space-item" and contains(., "Edit") ]')
    config_UDM = (By.XPATH, "//div[@class = 'ant-select-item ant-select-item-option'  and @title='%s']")
    config_Text = "//div[@class = 'ant-select-item ant-select-item-option' and @title='%s']"
    config_Text_AMF = "//div[@class = 'ant-select-item ant-select-item-option ant-select-item-option-active'  and @title='%s']"
    config_Register = (By.XPATH, "//span[@class = 'Mouse___159SR']")
    """
    # Configuration
    # Logger
    """
    #config_Logger = (By.XPATH, '//*[@id="rc-tabs-4-tab-Logger"]')
    config_Logger = (By.XPATH, "//div[@class='ant-tabs-tab-btn' and contains(., 'Logger')]")
    config_Logger_Edit = (
        By.XPATH, "//div[@class='ant-select ant-select-single ant-select-allow-clear ant-select-show-arrow']")
    config_Logger_ToFile = (By.XPATH, "//div[@id='basic_Level_list']")
    config_Logger_Now = (By.XPATH, "//span[@class='ant-select-selection-item']")
    # Logger 配置可修改选项
    Logger_text = "//div[@title='%s']"
    ToFile_text = "//div[@title='%s']"
    config_ToFile_Now = (
        By.XPATH, "//div[@class='ant-select ant-select-single ant-select-allow-clear ant-select-show-arrow']")
    config_Logger_Submit = (By.XPATH, "//button[@type='submit']")
    LoggerLevelList = ["info", "debug", "trace", "warn", "error", "fatal", "panic"]
    LoggerToFileList = ["1", "0"]
    BPSList = ["bps", "Kbps", "Mbps", "Gbps", "Tbps"]
    NEAList = ["NEA0", "NEA2", "NEA3", "NEA0,NEA2", "NEA0,NEA3", "NEA2,NEA3", "NEA0,NEA2,NEA3"]
    NIAList = ["NIA0", "NIA2", "NIA3", "NIA0,NIA2", "NIA0,NIA3", "NIA2,NIA3", "NIA0,NIA2,NIA3"]
    PREEMPTIONLIST = ["PREEMPTABLE", "NOT_PREEMPTABLE"]
    OPRANGELIST = ["10.0.246.123/23", "10.0.246.122/23", "10.0.246.121/23", "10.0.246.122/23", "10.0.246.120/23"]
    #测试add时候为空
    ADDLIST = ["basic_PlmnId", "basic_DnnName", "basic_IpRange", "basic_IPv6Prefix", "basic_DNS_IPV4", "basic_DNS_IPV6",
               "basic_PCSCF_IPV4", "basic_PCSCF_IPV6"]
    """
    # Configuration
    # Sbi修改
    """
    #config_Sbi_Edit = (By.XPATH, '//*[@id="rc-tabs-1-tab-SBI"]')
    config_Sbi_Edit = (By.XPATH, "//div[@class='ant-tabs-tab-btn' and contains(., 'SBI')]")
    config_Sbi_Ip = "//input[@id='basic_%s_Addr_Ip']"
    config_Sbi_Port = "//input[@id='basic_%s_Addr_Port']"
    """
    # Configuration
    # Service修改
    """
    #config_Service_Edit = (By.XPATH, '//div[@class="ant-tabs-tab ant-tabs-tab-active"]')
    #config_Service_Edit = (By.XPATH, "//*[@id='rc-tabs-31-tab-SBI']")
    # rc-tabs-31-tab-service
    # rc-tabs-1-tab-service
    config_Service_Edit = (By.XPATH, "//div[@class='ant-tabs-tab-btn' and contains(., 'Service')]")
    config_Service_Form = (By.XPATH, '//*[@id="basic"]')
    """
    # Configuration
    # Timer修改
    """
    config_Common = "//div[@class='ant-tabs-tab-btn' and contains(., '%s')]"


    """
    # Configuration
    # test data
    """
    config_Test_Ip_List = ["127.0.0.1", "127.0.0.2"]
    config_Test_Port_List = ["38412", "38414"]
    #LOG
    CONFIG_SPAN_DATA = (By.XPATH, '//*[@class="ant-select-selection-item"]')
    CONFIG_SPAN_PLMN = (By.XPATH, '//*[@id="basic_PlmnId"]')
    CONFIG_SPAN_LOG_TEXT = '//*[@class="ant-select-selection-item" and @title="%s"]'
    CONFIG_SPAN_TO_FILE_TEXT = '//*[@class="ant-select-item ant-select-item-option" and @title="%s"]'
    CONFIG_SPAN_TO_ALREADY_SELECT = '//*[@class="ant-select-selection-item" and @title="%s"]'
    CONFIG_LOG_CONTROL = (By.XPATH, '//*[@id="basic_Control"]')
    CONFIG_BASIC_CONTROL = (By.XPATH, '//input[@id="basic_Control"]')
    #CONFIG_BASIC_NEW_INPUT = (By.XPATH, '//*[@id="basic_InstanceId"]')
    CONFIG_BASIC_NEW_INPUT = (By.XPATH, '//*[@class="ant-input"]')
    CONFIG_BASIC_NEW_INPUT_SUCCESS = (By.XPATH, '//*[@class="ant-input ant-input-status-success"]')
    CONFIG_BASIC_NEW_INPUT_BAR_RULES = (By.XPATH, '//*[@id="basic_DLDataNotificationDelay"]')
    CONFIG_ADD = (By.XPATH, '//*[text()="Add"]')
    CONFIG_OK = (By.XPATH, '//*[text()="OK"]')
    CONFIG_EDIT_LIST = (By.XPATH, '//*[@class="ant-table-row ant-table-row-level-0"]')
    CONFIG_EDIT = (By.XPATH, '//*[text()="Edit"]')
    CONFIG_DELETE = (By.XPATH, '//*[text()="Delete"]')
    CONFIG_DELETE_YES = (By.XPATH, '//*[text()="Yes"]')
    CONFIG_DELETE_BUTTON_YES = (By.XPATH, '//*[@class="ant-btn ant-btn-primary ant-btn-sm" and (@type="submit" or @type="button") and contains(., "Yes")]')
    CONFIG_EDIT_PLMN_SELECT = (By.XPATH, '//*[@class="ant-select-item ant-select-item-option ant-select-item-option-active" and @title="46000"]')
    # 登录
    def login_5gc(self, username=UserName, pwd=Pwd):
        # self.locator_element(LoginPage.username_loc)
        attempts = 0
        success = False
        while attempts < 3 and not success:
            try:
                time.sleep(1)
                self.clear_data(self.locator_element(LoginPage.password_loc))
                self.set_keys(LoginPage.password_loc, pwd)
                img = self.locator_element(LoginPage.ver_code)
                data = img.screenshot_as_png
                ocr = ddddocr.DdddOcr()
                # 进行验证码识别
                text = ocr.classification(data)
                print("verify_code===", text)
                #debugger(self.driver)
                self.clear_data(self.locator_element(LoginPage.send_code))
                self.set_keys(LoginPage.send_code, text)
                self.locator_element(LoginPage.submit_loc).click()
                time.sleep(1)
                #self.web_driver_wait(LoginPage.config)
                #判断是否·登录成功，登录失败则重新登录
                if self.get_title() != "Dashboard - Lite5gc":
                    #删除登录redis
                    self.delete_login_redis()
                    self.login_5gc()
                    success = True
            except:
                attempts += 1
                if attempts == 3:
                    return
        #debugger(self.driver)
        # todo 验证码识别率，可以多做几次尝试，判断验证码错误时候

    # 退出
    def logout_5gc(self):
        self.mouse_over(LoginPage.admin_menu)
        self.locator_element(LoginPage.hidden_submenu).click()

    # 跳转 Configuration
    def link_config(self):
        self.locator_element(LoginPage.config).click()

    # 跳转网元编辑页面
    def link_config_nf(self, name):
        # todo 多个网元需要按照数据区分
        self.link_config()
        time.sleep(1)
        self.locator_element(LoginPage.config_nf_type).click()
        time.sleep(1)
        pngs = []
        try:
            if name == "AMF":
                self.locator_element((By.XPATH, (LoginPage.config_Text_AMF % name))).click()
            else:
                self.locator_element((By.XPATH, (LoginPage.config_Text % name))).click()
            time.sleep(1)
            #self.web_driver_wait(LoginPage.config_Edit)
            self.locator_element(LoginPage.config_Edit).click()
            return pngs, ""
        except:
            time.sleep(3)
            try:
                self.locator_element((By.XPATH, (LoginPage.config_Text % name))).click()
                time.sleep(1)
                #self.web_driver_wait(LoginPage.config_Edit)
                self.locator_element(LoginPage.config_Edit).click()
                return pngs, ""
            except:
                self.link_config_nf(name)


    # 编辑 logger的配置信息
    def config_logger_edit(self):
        # todo AMF+n2 的都在amf，amf需要两次
        # 到logger页面
        time.sleep(1)
        self.locator_element(LoginPage.config_Logger).click()
        level = self.locator_element(LoginPage.config_Logger_Now).get_attribute("title")
        print("level===", level)
        self.web_driver_wait(LoginPage.config_Logger_Edit)
        self.locator_element(LoginPage.config_Logger_Edit).click()
        # 修改Level
        # 下拉框需要等待后才能点击
        time.sleep(1)
        to_level = LoginPage.LoggerLevelList[0]
        if level == LoginPage.LoggerLevelList[0]:
            to_level = LoginPage.LoggerLevelList[1]

        time.sleep(1)
        # 点击下拉框
        self.locator_element((By.XPATH, (LoginPage.Logger_text % to_level))).click()

        # 修改to file
        file_now = self.locator_elements(LoginPage.config_Logger_Now)[1].get_attribute("title")
        print("file_now===", file_now)
        self.locator_element(LoginPage.config_Logger_Edit).click()
        to_file = LoginPage.LoggerToFileList[0]
        if to_file == file_now:
            to_file = LoginPage.LoggerToFileList[1]

        time.sleep(1)
        self.locator_element((By.XPATH, (LoginPage.ToFile_text % to_file))).click()
        self.locator_element(LoginPage.config_Logger_Submit).click()
        # 提交修改
        time.sleep(1)
        level = self.locator_element(LoginPage.config_Logger_Now).get_attribute("title")
        file_now = self.locator_elements(LoginPage.config_Logger_Now)[1].get_attribute("title")
        # 返回现在的显示
        return level, to_level, file_now, to_file

    # 获取 Sbi的配置信息
    def config_sbi_show(self):
        time.sleep(1)
        cards = self.locator_element((By.XPATH, "//div[@class='ant-col ant-col-8']"))
        try:
            puts = []
            subs = []
            in_puts = cards.find_elements(By.XPATH, '//input[@class="ant-input"]')
            for in_put in in_puts:
                if in_put.is_displayed():
                    puts.append(in_put)
            submits = cards.find_elements(By.XPATH, '//button[@type="submit"]')
            for submit in submits:
                if submit.is_displayed() and submit.get_attribute("type") == "submit":
                    subs.append(submit)
            return puts, subs
        except:
            print("No input")
        return "", ""

    # 编辑 Sbi的配置信息
    def config_sbi_edit(self):
        # 到sbi页面
        time.sleep(1)
        # debugger(self.driver)
        self.locator_element(LoginPage.config_Sbi_Edit).click()
        time.sleep(1)
        after_ip_list, after_port_list = [], []
        ip_list, port_list = [], []
        try:
            in_put, submit = self.config_sbi_show()
            if in_put == "" or submit == "":
                return
            i, sub = 0, 0,
            ip, port = in_put[0], in_put[1]
            for put in in_put:
                i += 1
                if i == 1:
                    ip = put
                else:
                    i = 0
                    port = put
                    now_ip = ip.get_attribute("value")
                    now_port = port.get_attribute("value")
                    set_ip = LoginPage.config_Test_Ip_List[0]
                    set_port= LoginPage.config_Test_Port_List[0]
                    if now_ip == LoginPage.config_Test_Ip_List[0]:
                        set_ip = LoginPage.config_Test_Ip_List[1]
                    if now_port == LoginPage.config_Test_Port_List[0]:
                        set_port = LoginPage.config_Test_Port_List[1]
                    # 输入ip
                    self.clear_data(ip)
                    ip.send_keys(set_ip)
                    # 输入port
                    self.clear_data(port)
                    port.send_keys(set_port)
                    submit[sub].click()
                    sub += 1
                    ip_list.append(set_ip)
                    port_list.append(set_port)

            # 再次检查数据
            in_put, submit = self.config_sbi_show()
            if in_put == "" or submit == "":
                return
            ip, port = in_put[0], in_put[1]
            i = 0
            for put in in_put:
                i += 1
                if i == 1:
                    ip = put
                else:
                    i = 0
                    port = put
                    after_ip_list.append(ip.get_attribute("value"))
                    after_port_list.append(port.get_attribute("value"))
        except:
            print("run error")
        return ip_list, port_list, after_ip_list, after_port_list

    # 获取 Service的配置信息
    def config_service_show(self):
        time.sleep(1)
        forms = self.locator_element(LoginPage.config_Service_Form)
        return forms

    # 编辑 Service的配置信息
    def config_service_edit(self):
        # 到sbi页面
        time.sleep(1)
        self.locator_element(LoginPage.config_Service_Edit).click()
        time.sleep(1)
        # AMF
        forms = self.config_service_show()
        set_datas = []
        set_after_datas = []

        in_puts = forms.find_elements(By.XPATH, '//input[@class="ant-input"]')
        submits = forms.find_elements(By.XPATH, '//button[@class="ant-btn ant-btn-primary"]')
        # 修改数据并提交
        flag = False
        for submit in submits:
            i = 0
            for in_put in in_puts:
                if not in_put.is_displayed() or in_put.get_attribute("value") == "":
                    continue
                in_put.click()
                self.clear_data(in_put)
                # 获取设置的数据
                data = str(random.randint(0, 9))
                if flag:
                    data = set_datas[i]
                else:
                    set_datas.append(data)
                i += 1
                in_put.send_keys(data)
            flag = True
            if submit.is_displayed():
                submit.click()
        # 再次读取元素，进行对比
        forms = self.config_service_show()
        in_puts = forms.find_elements(By.XPATH, '//input[@class="ant-input"]')
        for in_put in in_puts:
            if in_put.get_attribute("value") != "":
                set_after_datas.append(in_put.get_attribute("value"))

        return set_datas, set_after_datas

    # 获取 Service的配置信息
    def config_common_show(self):
        time.sleep(1)
        forms = self.locator_element(LoginPage.config_Service_Form)
        return forms

    # 编辑 Timer的配置信息
    def config_common_edit(self, tab):
        # 到sbi页面
        time.sleep(1)
        debugger(self.driver)
        self.locator_element((By.XPATH, LoginPage.config_Common % tab)).click()
        time.sleep(1)
        # AMF
        forms = self.config_service_show()
        set_datas = []
        set_after_datas = []

        in_puts = forms.find_elements(By.XPATH, '//input[@class="ant-input"]')
        submits = forms.find_elements(By.XPATH, '//button[@class="ant-btn ant-btn-primary"]')
        # 修改数据并提交
        flag = False
        for submit in submits:
            i = 0
            for in_put in in_puts:
                if not in_put.is_displayed() or in_put.get_attribute("value") == "":
                    continue
                in_put.click()
                self.clear_data(in_put)
                # 获取设置的数据
                data = self.get_random_data(in_put.get_attribute("id"),in_put.get_attribute("value"))
                if flag:
                    data = set_datas[i]
                else:
                    set_datas.append(data)
                i += 1
                in_put.send_keys(data)
            flag = True
            if submit.is_displayed():
                submit.click()
                # N2 submit需要确认
                if tab == "N2":
                    time.sleep(1)
                    self.locator_element((By.XPATH, '//*[@class="ant-btn ant-btn-primary ant-btn-sm"]')).click()
        # 再次读取元素，进行对比
        forms = self.config_service_show()
        in_puts = forms.find_elements(By.XPATH, '//input[@class="ant-input"]')
        for in_put in in_puts:
            if in_put.is_displayed() and in_put.get_attribute("value") != "":
                set_after_datas.append(in_put.get_attribute("value"))

        return set_datas, set_after_datas

    def get_title(self):
        return self.get_driver_title()

    def get_screenshot(self, url):
        time.sleep(1)
        return self.get_screenshot_as_base(url)

    def set_url(self):
        return self.set_driver_url()

    def get_url(self):
        self.get_driver_url()

    # 跳转窗口
    def driver_switch(self, handles_index):
        self.set_driver_switch(handles_index)

    # 随机数据
    def get_random_data(self, key, now_data):
        value = str(random.randint(0, 9))
        if "RegionId" in key or "RelativeAmfCapacity" in key:
            value = str(random.randint(0, 255))  # Integer between 0-255
        elif "SetId" in key:
            value = str(random.randint(0, 1023))  # Integer between 0-1023
        elif "Pointer" in key:
            value = str(random.randint(0, 63)) #Integer between 0-63
        elif "FiveQI" in key:
            value = str(random.randint(1, 60))
        elif "IpRange" in key:
            value = LoginPage.OPRANGELIST[random.randint(0, 3)]
            #10.0.246.123/23
        elif "IPv6Prefix" in key:
            value = str(random.randint(2000, 9999)) + "::/64"
        elif "IPV6" in key:
            #2001:4860:4860::8888
            value = str(random.randint(2000, 8888)) + ":" + str(random.randint(2000, 8888)) + ":" + str(random.randint(2000, 8888)) + ":" + str(random.randint(2000, 8888))
        elif "Ip" in key or "IP" in key:
            if "127.0.0." in key:
                value = "127.0.0." + str(random.randint(1, 240))
            else:
                value = self.get_random_ip()
        elif "Port" in key:
            #1025~65535
            value = str(random.randint(1025, 65535))
        elif "PlmnId" in key:
            value = str(random.randint(10000, 999999))  # The PlmnId is not a 5-bit or 6-bit integer string
        elif "ID" in key or "level_help" in key:
            value = str(random.randint(1, 63))  # basic_QosDataID 1-63 basic_Arp_priority_level_help
        elif key == "basic_Log":
            value = LoginPage.LoggerLevelList[random.randint(0, 6)]
        elif key == "basic_ToFile":
            value = LoginPage.LoggerToFileList[random.randint(0, 1)]
        elif key == "NEA":
            value = LoginPage.NEAList[random.randint(0, 6)]
        elif key == "NIA":
            value = LoginPage.NIAList[random.randint(0, 6)]
        elif key == "bps":
            value = LoginPage.BPSList[random.randint(0, 4)]
        elif key == "Preemption":
            value = LoginPage.PREEMPTIONLIST[random.randint(0, 1)]
        elif key == "bool":
            if now_data == "true":
                value = "false"
            else:
                value = "true"

        #不与现在的值相等
        if value == now_data:
            return self.get_random_data(key, now_data)
        print("-------------------------------", key, now_data, value)
        return value

    # 随机ip
    def get_random_ip(self):
        RANDOM_IP_POOL = ['127.0.0.1/0']
        str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
        str_ip_addr = str_ip.split('/')[0]
        str_ip_mask = str_ip.split('/')[1]
        ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
        mask = 0x0
        for i in range(31, 31 - int(str_ip_mask), -1):
            mask = mask | (1 << i)
        ip_addr_min = ip_addr & (mask & 0xffffffff)
        ip_addr_max = ip_addr | (~mask & 0xffffffff)
        return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

    # 普通测试
    def config_common_ts(self, tab, lab=""):
        # 到sbi页面
        time.sleep(1)
        self.locator_element((By.XPATH, LoginPage.config_Common % tab)).click()
        time.sleep(1)
        if lab != "":
            self.locator_element((By.XPATH, LoginPage.config_Common % lab)).click()
            time.sleep(1)
        # AMF
        forms = self.config_service_show()
        set_datas = []
        set_after_datas = []

        in_puts = forms.find_elements(By.XPATH, '//input[@class="ant-input"]')
        submits = forms.find_elements(By.XPATH, '//button[@class="ant-btn ant-btn-primary"]')
        # 修改数据并提交
        flag = False
        for submit in submits:
            i = 0
            for in_put in in_puts:
                if not in_put.is_displayed() or in_put.get_attribute("value") == "":
                    continue
                in_put.click()
                self.clear_data(in_put)
                # 获取设置的数据
                data = self.get_random_data(in_put.get_attribute("id"),in_put.get_attribute("value"))
                if flag:
                    data = set_datas[i]
                else:
                    set_datas.append(data)
                i += 1
                in_put.send_keys(data)
            flag = True
            if submit.is_displayed():
                submit.click()
                # N2 submit需要确认
                if tab == "N2":
                    time.sleep(1)
                    self.locator_element((By.XPATH, '//*[@class="ant-btn ant-btn-primary ant-btn-sm"]')).click()
        # 再次读取元素，进行对比
        forms = self.config_service_show()
        in_puts = forms.find_elements(By.XPATH, '//input[@class="ant-input"]')
        for in_put in in_puts:
            if in_put.is_displayed() and in_put.get_attribute("value") != "":
                set_after_datas.append(in_put.get_attribute("value"))

        return set_datas, set_after_datas

    # 获取配置信息
    def config_form(self):
        time.sleep(1)
        forms = self.locator_element(LoginPage.config_Service_Form)
        return forms


    # 编辑 logger的配置信息
    def config_logger_ts(self, tab, lab=""):
        # todo AMF+n2 的都在amf，amf需要两次
        # 到logger页面
        time.sleep(1)
        self.locator_element((By.XPATH, LoginPage.config_Common % tab)).click()
        time.sleep(1)
        if lab != "":
            self.locator_element((By.XPATH, LoginPage.config_Common % lab)).click()
            time.sleep(1)
        #查找需要修改的数据
        time.sleep(1)
        forms = self.config_form()
        span_datas = forms.find_elements(*LoginPage.CONFIG_SPAN_DATA)
        submits = forms.find_elements(By.XPATH, '//button[@class="ant-btn ant-btn-primary" and @type="submit"]')
        pngs = []
        pngs.append(self.driver.get_screenshot_as_base64())

        lg = []
        tf = []
        now_lg = []
        now_tf = []
        for submit in submits:
            time.sleep(1)
            for span_data in span_datas:
                if span_data.is_displayed and (span_data.get_attribute("title") in LoginPage.LoggerLevelList):
                    self.locator_element((By.XPATH, (LoginPage.CONFIG_SPAN_LOG_TEXT % span_data.get_attribute("title")))).click()
                    data = self.get_random_data("basic_Log", span_data.get_attribute("title"))
                    log = self.locator_element((By.XPATH, (LoginPage.CONFIG_SPAN_TO_FILE_TEXT % data)))
                    lg.append(data)
                    time.sleep(1)
                    log.click()
                elif span_data.is_displayed and (span_data.get_attribute("title") in LoginPage.LoggerToFileList):
                    self.locator_element((By.XPATH, (LoginPage.CONFIG_SPAN_LOG_TEXT % span_data.get_attribute("title")))).click()
                    data = self.get_random_data("basic_ToFile", span_data.get_attribute("title"))
                    file = self.locator_element((By.XPATH, (LoginPage.CONFIG_SPAN_TO_FILE_TEXT % data)))
                    tf.append(data)
                    time.sleep(1)
                    file.click()
            if submit.is_displayed():
                submit.click()
        time.sleep(1)
        forms = self.config_form()
        span_datas = forms.find_elements(*LoginPage.CONFIG_SPAN_DATA)
        for span_data in span_datas:
            if span_data.is_displayed and (span_data.get_attribute("title") in LoginPage.LoggerLevelList):
                now_lg.append(span_data.get_attribute("title"))
            elif span_data.is_displayed and (span_data.get_attribute("title") in LoginPage.LoggerToFileList):
                now_tf.append(span_data.get_attribute("title"))
        # 返回现在的显示
        pngs.append(self.driver.get_screenshot_as_base64())
        return lg, tf, now_lg, now_tf, pngs

    # 普通测试，通用
    def common_ts(self, tab, lab=""):
        # 到logger页面
        time.sleep(1)
        self.locator_element((By.XPATH, LoginPage.config_Common % tab)).click()
        time.sleep(1)
        if lab != "":
            self.locator_element((By.XPATH, LoginPage.config_Common % lab)).click()
        #查找需要修改的数据
        time.sleep(1)
        forms = self.config_form()
        pngs = []
        pngs.append(self.driver.get_screenshot_as_base64())

        set_datas = []
        set_after_datas = []

        in_puts = self.locator_elements(LoginPage.CONFIG_BASIC_NEW_INPUT)
        submits = forms.find_elements(By.XPATH, '//button[@class="ant-btn ant-btn-primary" and (@type="submit" or @type="button") and contains(., "Submit")]') # amf GUAMI type="button"
        span_datas = forms.find_elements(*LoginPage.CONFIG_SPAN_DATA)
        # 去掉不展示的
        submits = self.del_no_display(submits)
        in_puts = self.del_no_display(in_puts)
        span_datas = self.del_no_display(span_datas)
        # 修改数据并提交
        flag = False
        repeat = False
        time.sleep(1)
        exist_span = bool
        for submit in submits:
            i = 0
            dict = {'name': 0} #用于重复的元素出现
            for in_put in in_puts:
                if not in_put.is_displayed() or in_put.get_attribute("value") == "":
                    continue
                in_put.click()
                self.clear_data(in_put)
                # 获取设置的数据
                data = self.get_random_data(in_put.get_attribute("id"), in_put.get_attribute("value"))
                if flag:
                    data = set_datas[i]
                else:
                    set_datas.append(data)
                i = i + 1
                in_put.send_keys(data)
            if exist_span:
                # 多下拉框多个提交按钮，第二次提交值变了
                span_datas = forms.find_elements(*LoginPage.CONFIG_SPAN_DATA)
            if tab == "PM":
                span_datas = self.locator_elements((By.XPATH, '//span[@class="ant-select-selection-item" and @title="true" or @title="false"]'))
            for span_data in span_datas:
                dict_key = ""
                if span_data.is_displayed:
                    if lab or tab == "LOG" and span_data.get_attribute("title") in LoginPage.LoggerLevelList:
                        dict_key = "basic_Log"
                    elif lab or tab == "LOG" and span_data.get_attribute("title") in LoginPage.LoggerToFileList:
                        dict_key = "basic_ToFile"
                    elif span_data.get_attribute("title") in LoginPage.NEAList:
                        dict_key = "NEA"
                    elif span_data.get_attribute("title") in LoginPage.NIAList:
                        dict_key = "NIA"
                    elif span_data.get_attribute("title") in LoginPage.BPSList:
                        dict_key = "bps"
                    elif span_data.get_attribute("title") == "true" or span_data.get_attribute("title") == "false":
                        dict_key = "bool"
                        #span_data.click()
                        exist_span = True
                    else:
                        continue
                    data = self.get_random_data(dict_key, span_data.get_attribute("title"))
                    if dict_key in dict:
                        dict[dict_key] = dict[dict_key] + 1
                    else:
                        dict[dict_key] = 0
                    if flag:
                        data = set_datas[i]
                        i += 1
                    else:
                        set_datas.append(data)
                    try:
                        if data != "true" and data != "false" or tab == "Features":
                            clicks = self.locator_elements(
                                (By.XPATH, (LoginPage.CONFIG_SPAN_LOG_TEXT % span_data.get_attribute("title"))))
                                  #dict[dict_key], LoginPage.CONFIG_SPAN_LOG_TEXT % span_data.get_attribute("title"))
                            if len(clicks) > dict[dict_key]:
                                clicks[dict[dict_key]].click()
                            else:
                                clicks[0].click()
                        time.sleep(1)
                        #debugger(self.driver)
                        select = self.locator_elements((By.XPATH, (LoginPage.CONFIG_SPAN_TO_FILE_TEXT % data)))
                        if len(select) < 1:
                            select = self.locator_elements((By.XPATH, (LoginPage.CONFIG_SPAN_TO_ALREADY_SELECT % data)))
                        #set_datas.append(data)
                        if len(select) > dict[dict_key]:
                            select[dict[dict_key]].click()
                        else:
                            select[0].click()
                    except:
                        print("该元素不可交互")
            flag = True
            time.sleep(1)
            if submit.is_displayed():
                pngs.append(self.driver.get_screenshot_as_base64())
                submit.click()
                # N2 submit需要确认
                if tab == "N2" or lab == "GUAMI":
                    time.sleep(1)
                    self.locator_element((By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-sm"]')).click()
        time.sleep(1)
        # 再次读取元素，进行对比
        in_ps = self.locator_elements(LoginPage.CONFIG_BASIC_NEW_INPUT_BAR_RULES)
        in_puts = self.locator_elements(LoginPage.CONFIG_BASIC_NEW_INPUT_SUCCESS)
        if len(in_puts) <= 0 or lab == "BAR Rules":
            in_puts = self.locator_elements(LoginPage.CONFIG_BASIC_NEW_INPUT)
        span_datas = forms.find_elements(*LoginPage.CONFIG_SPAN_DATA)
        fs = True
        for in_put in in_puts:
            # react不讲武德，id会变
            if fs and len(in_ps) > 0:
                fs = False
                set_after_datas.append(in_ps[0].get_attribute("value"))
            if in_put.is_displayed() and in_put.get_attribute("value") != "":
                set_after_datas.append(in_put.get_attribute("value"))
        #if exist_span:
        for span_data in span_datas:
            if span_data.is_displayed:
                if self.judge_span(span_data.get_attribute("title"), tab, lab):
                    set_after_datas.append(span_data.get_attribute("title"))

        # 返回现在的显示
        pngs.append(self.driver.get_screenshot_as_base64())
        if tab == lab and tab == "Service":
            return set_datas[0], set_after_datas[0], pngs
        if lab == "Relative Capacity" and len(set_datas) > 2 and len(set_after_datas) > 2:
            return set_datas[:2], set_after_datas[:2], pngs
        return set_datas, set_after_datas, pngs

    def del_no_display(self, ls):
        for l in ls:
            if not l.is_displayed():
                ls.pop(ls.index(l))
            if not l.is_enabled():
                ls.pop(ls.index(l))
        return ls



    #判断span是否展示
    def judge_span(self, title="", tab="", lab=""):
        if title in LoginPage.BPSList:
            return True
        elif title in LoginPage.NEAList:
            return True
        elif title in LoginPage.NIAList:
            return True
        elif lab or tab == "LOG" and (title in LoginPage.LoggerLevelList or title in LoginPage.LoggerToFileList or (title == "true" or title == "false")):
            return True
        return False

    # 增删改查
    def curl_ts(self, tab, lab=""):
        pngs = []
        # 到logger页面
        time.sleep(1)
        self.locator_element((By.XPATH, LoginPage.config_Common % tab)).click()
        time.sleep(1)
        if lab != "":
            self.locator_element((By.XPATH, LoginPage.config_Common % lab)).click()
        #查找需要修改的数据
        time.sleep(1)
        pngs.append(self.driver.get_screenshot_as_base64())
        #############################################
        # Add
        #############################################
        # 输入提交流程
        self.edit_ts(tab, lab, "ADD")
        self.edit_ts(tab, lab, "EDIT")
        self.edit_ts(tab, lab, "DELETE")
        pngs.append(self.driver.get_screenshot_as_base64())
        return pngs

    def edit_ts(self, tab, lab, typ):
        time.sleep(1)
        if typ == "ADD":
            adds = self.locator_elements(LoginPage.CONFIG_ADD)
            if len(adds) == 1:
                adds[0].click()
            elif len(adds) > 0:
                for add in adds:
                    if add.is_displayed():
                        add.click()
        elif typ == "EDIT":
            edits = self.locator_elements(LoginPage.CONFIG_EDIT)
            if len(edits) > 0:
                edits[len(edits) - 1].click()
            else:
                print("当前无数据可修改")
                return
        elif typ == "DELETE":
            deletes = self.locator_elements(LoginPage.CONFIG_DELETE)
            if len(deletes) > 0:
                deletes[len(deletes) - 1].click()
                time.sleep(1)
                self.locator_element(LoginPage.CONFIG_DELETE_BUTTON_YES).click()
                # 有确认框 deletes
                return
            else:
                print("当前无数据可删除")
                return
        forms = self.config_form()
        pngs = []
        pngs.append(self.driver.get_screenshot_as_base64())
        set_datas = []
        set_after_datas = []

        in_puts = self.locator_elements(LoginPage.CONFIG_BASIC_NEW_INPUT)
        # 兼容编辑smf PLMN ID时候找不到
        if typ == "EDIT" or len(in_puts) < 1:
            in_puts = self.locator_elements(LoginPage.CONFIG_BASIC_NEW_INPUT_SUCCESS)
            if len(in_puts) < 1:
                in_puts = self.locator_elements(LoginPage.CONFIG_BASIC_NEW_INPUT)
        submits = forms.find_elements(By.XPATH, '//button[@class="ant-btn ant-btn-primary" and @type="button"]')
        span_datas = forms.find_elements(*LoginPage.CONFIG_SPAN_DATA)
        #basic_PlmnId
        submits = self.del_no_display(submits)
        in_puts = self.del_no_display(in_puts)
        span_datas = self.del_no_display(span_datas)
        if lab == "Supported Nssai In PLMN List":
            in_puts = forms.find_elements(*LoginPage.CONFIG_SPAN_PLMN)
        # 修改数据并提交
        flag = False
        repeat = False
        time.sleep(1)
        exist_span = bool
        for submit in submits:
            i = 0
            for in_put in in_puts:
                i = 0
                # nssf 的 TA List
                if lab == "TA List" and i == 0:
                    self.locator_element((By.XPATH, '//*[@id="basic_Tai_PlmnId"]')).click()
                    time.sleep(1)
                    self.locator_element((By.XPATH, '//div[@aria-label="basic_Tai_PlmnId_list_0"]')).click()
                if lab == "Supported Nssai In PLMN List" and typ == "ADD":
                    in_put.click()
                    self.locator_element(LoginPage.CONFIG_EDIT_PLMN_SELECT).click()
                    break
                #basic_PlmnId
                if not in_put.is_displayed() or (in_put.get_attribute("value") == "" and typ != "ADD"):
                    continue
                elif typ == "ADD" and ("basic" not in in_put.get_attribute("id")):
                    continue
                in_put.click()
                self.clear_data(in_put)
                # 获取设置的数据
                data = self.get_random_data(in_put.get_attribute("id"), in_put.get_attribute("value"))
                if flag:
                    data = set_datas[i]
                else:
                    set_datas.append(data)
                i += 1
                in_put.send_keys(data)

            if exist_span:
                # 多下拉框多个提交按钮，第二次提交值变了
                span_datas = forms.find_elements(*LoginPage.CONFIG_SPAN_DATA)
            for span_data in span_datas:
                if span_data.is_displayed:
                    data = ""
                    loc = ""
                    if lab == "LOG" and span_data.get_attribute("title") in LoginPage.LoggerLevelList:
                        data = self.get_random_data("basic_Log", span_data.get_attribute("title"))
                    elif lab == "LOG" and span_data.get_attribute("title") in LoginPage.LoggerToFileList:
                        data = self.get_random_data("basic_ToFile", span_data.get_attribute("title"))
                    elif span_data.get_attribute("title") in LoginPage.BPSList:
                        data = self.get_random_data("bps", span_data.get_attribute("title"))
                    elif span_data.get_attribute("title") in LoginPage.PREEMPTIONLIST:
                        data = self.get_random_data("Preemption", span_data.get_attribute("title"))
                    elif span_data.get_attribute("title") == "true" or span_data.get_attribute("title") == "false":
                        data = self.get_random_data("bool", span_data.get_attribute("title"))
                        span_data.click()
                        exist_span = True
                    else:
                        continue

                    if flag:
                        data = set_datas[i]
                        i += 1
                    else:
                        set_datas.append(data)
                    try:
                        if data != "true" and data == "false":
                            self.locator_element(
                                (By.XPATH, (LoginPage.CONFIG_SPAN_LOG_TEXT % span_data.get_attribute("title")))).click()
                        #debugger(self.driver)
                        select = self.locator_element((By.XPATH, (LoginPage.CONFIG_SPAN_TO_FILE_TEXT % data)))
                        #set_datas.append(data)
                        time.sleep(1)
                        select.click()
                    except:
                        print("该元素不可交互")
                # 点击ok提交代码
            if typ == "ADD" or typ == "EDIT":
                pngs.append(self.driver.get_screenshot_as_base64())
                oks = self.locator_elements(LoginPage.CONFIG_OK)
                if len(oks) == 1:
                    oks[0].click()
                for ok in oks:
                    if ok.is_displayed():
                        try:
                            ok.click()
                        except:
                            self.driver.execute_script("arguments[0].click();", ok)
                break
            flag = True
            if submit.is_displayed():
                submit.click()
                # N2 submit需要确认
                if tab == "N2":
                    time.sleep(1)
                    self.locator_element((By.XPATH, '//*[@class="ant-btn ant-btn-primary ant-btn-sm"]')).click()
        time.sleep(1)
        # 返回现在的显示
        pngs.append(self.driver.get_screenshot_as_base64())
        return "", "", pngs


    # 用于删除登录验证码失败的redis key
    def delete_login_redis(self):
        try:
            pool = redis.ConnectionPool(host=Ip, port=16379, password="123456", db=0)
            r = redis.StrictRedis(connection_pool=pool)
            r.delete(*r.keys(UserName + '*'))
        except:
            print("暂时无需要删除的key")

    #获取yaml文件信息
    def request_get_yaml(self):
        url = 'http://' + Ip + ':8895/yaml/show'
        postdata = ""
        p = requests.post(url, data=postdata)
        #print("get_yaml resp===", p.json())
        return p.json()

    #获取etcd配置信息
    def request_nf_show(self):
        url = 'http://' + Ip + ':8887/nfshow'
        postdata = {"nftype": "SMF", "nfno": "b233b902-d2c4-975f-e1e1-9782097cb432", "ifce": {}}
        p = requests.post(url, json=postdata)
        #print("nf_show resp===", p.json())
        return p.json()
