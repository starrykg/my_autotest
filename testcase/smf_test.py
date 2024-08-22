import time
import unittest
from pageobject.project_page import *
#from webdriver_helper import debugger
from base.base_page import *
import logging
import os

class SmfTestCase(unittest.TestCase):
    """测试用例说明"""

    def setUp(self) -> None:
        self.images = []  # 初始化存放测试截图的列表
        self.lg = LoginPage()
        self.resultPath = os.path.join('logs')  # 存放log文件的路径
        if not os.path.exists(self.resultPath):  # 判断Logs路径是否存在
            os.mkdir(self.resultPath)  # 创建Logs文件
        self.logger = logging.getLogger()
        logging.root.setLevel(logging.NOTSET)
        self.backup_count = 5  # 最多存放日志的数量

    """登录"""

    def ctest_login(self):
        self.lg.login_5gc()
        """执行成功"""
        print("get_title", self.lg.get_title())
        self.assertEqual(self.lg.get_title(), "Dashboard - Lite5gc")
        if self.lg.get_title() != "Dashboard - Lite5gc":
            #删除redis
            print("登录失败")
        # self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))
        self.lg.set_url()

    """退出"""

    def ctest_logout(self):
        self.ctest_login()
        self.lg.logout_5gc()

    """config"""
    # 老页面
    def ctest_config_logger(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("NRF")
        level, to_level, file_now, to_file = self.lg.config_logger_edit()
        print("level, to_level, file_now, to_file===", level, to_level, file_now, to_file)
        self.assertEqual(level, to_level)
        self.assertEqual(file_now, to_file)
        self.images.append(self.lg.driver.get_screenshot_as_base())

    def ctest_config_Sbi(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("AMF")
        ip_list, port_list, after_ip_list, after_port_list = self.lg.config_sbi_edit()
        print("期待：ip_list, port_list===", ip_list, port_list)
        print("输出：after_ip_list, after_port_list===", after_ip_list, after_port_list)
        self.assertEqual(ip_list, after_ip_list)
        self.assertEqual(port_list, after_port_list)
        #self.lg.driver_switch(self.lg.driver.window_handles[0])
        self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))

    def ctest_config_Service(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("AMF")
        set_datas, set_after_datas = self.lg.config_service_edit()
        self.assertEqual(set_datas, set_after_datas)
        print("set_datas, set_after_datas===", set_datas, set_after_datas)
        self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))

    def ctest_config_Timer(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("SMF")
        set_datas, set_after_datas = self.lg.config_common_edit("Timer")
        self.assertEqual(set_datas, set_after_datas)
        print("set_datas, set_after_datas===", set_datas, set_after_datas)
        self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))

    def ctest_config_n4(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("SMF")
        set_datas, set_after_datas = self.lg.config_common_edit("N4")
        self.assertEqual(set_datas, set_after_datas)
        print("set_datas, set_after_datas===", set_datas, set_after_datas)
        self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))

    def ctest_config_n4(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("SMF")
        set_datas, set_after_datas = self.lg.config_common_edit("N4")
        self.assertEqual(set_datas, set_after_datas)
        print("set_datas, set_after_datas===", set_datas, set_after_datas)
        self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))

    def ctest_config_n2(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("AMF")
        set_datas, set_after_datas = self.lg.config_common_edit("N2")
        self.assertEqual(set_datas, set_after_datas)
        print("set_datas, set_after_datas===", set_datas, set_after_datas)
        self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))

    def ctest_config_n26(self):
        self.ctest_login()
        """执行成功"""
        time.sleep(1)
        self.lg.link_config_nf("AMF")
        set_datas, set_after_datas = self.lg.config_common_edit("N26")
        self.assertEqual(set_datas, set_after_datas)
        print("set_datas, set_after_datas===", set_datas, set_after_datas)
        self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))

    def ctest_basic(self):
        """test log"""
        self.ctest_login()
        time.sleep(1)
        pngs,  err = self.lg.link_config_nf("SMF")
        for png in pngs:
            self.images.append(png)

        self.assertEqual(err, "")
        lg, tf, now_lg, now_tf, pngs = self.lg.config_logger_ts("Basic", "LOG")
        print('输入参数： {} {}'.format(lg, tf))
        print('输出参数： {} {}'.format(now_lg, now_tf))
        self.assertEqual(lg, now_lg)
        self.assertEqual(tf, now_tf)
        for png in pngs:
            self.images.append(png)

    @unittest.skipUnless(ALL, "条件为真执行测试")
    def ctest_login_logout(self):
        """测试 登录退出 """
        self.ctest_logout()

    # @unittest.skipUnless(ALL or ("Basic" in TAB and "LOG" in LAB), "条件为真执行测试")
    # def test_smf_basic_log(self):
    #     """测试 Basic->LOG """
    #     self.common_func("SMF", "Basic", "LOG")

    @unittest.skipUnless(ALL or ("Basic" in TAB and "ID" in LAB), "条件为真执行测试")
    def test_smf_basic_id(self):
        """测试 Basic->ID """
        self.common_func("SMF", "Basic", "ID")

    @unittest.skipUnless(ALL or ("SM NAS" in TAB), "条件为真执行测试")
    def test_smf_sm_nas(self):
        """测试 SM NAS """
        self.common_func("SMF", "SM NAS", "")

    @unittest.skipUnless(ALL or ("N4" in TAB and "N4 CP" in LAB), "条件为真执行测试")
    def test_smf_n4_cp(self):
        """测试 N4->N4 CP """
        self.common_func("SMF", "N4", "N4 CP")

    @unittest.skipUnless(ALL or ("N4" in TAB and "N4 UP" in LAB), "条件为真执行测试")
    def test_smf_n4_up(self):
        """测试 N4->N4 UP """
        self.common_func("SMF", "N4", "N4 UP")

    @unittest.skipUnless(ALL or ("S5" in TAB), "条件为真执行测试")
    def test_smf_s5(self):
        """测试 S5 """
        self.common_func("SMF", "S5", "")

    @unittest.skipUnless(ALL or ("SBI" in TAB), "条件为真执行测试")
    def ctest_smf_sbi(self):
        """测试 SBI """
        self.common_func("SMF", "SBI", "")      # todo NSSF沒配置

    @unittest.skipUnless(ALL or ("Service" in TAB and "URR Rules" in LAB), "条件为真执行测试")
    def test_smf_service_urr_rules(self):
        """测试 Service->URR Rules """
        self.common_func("SMF", "Service", "URR Rules")

    @unittest.skipUnless(ALL or ("Service" in TAB and "BAR Rules" in LAB), "条件为真执行测试")
    def test_smf_service_bar_rules(self):
        """测试 Service->BAR Rules """
        self.common_func("SMF", "Service", "BAR Rules")

    # @unittest.skipUnless(ALL or ("Service" in TAB and "Qos Data" in LAB), "条件为真执行测试")
    # def ctest_smf_service_qos_data(self):
    #     """测试 Service->Qos Data """
    #     self.curl_func("SMF", "Service", "Qos Data")  # todo 部分

    @unittest.skipUnless(ALL or ("Service" in TAB and "PCC Rules" in LAB), "条件为真执行测试")
    def test_smf_service_pcc_rules(self):
        """测试 Service->PCC Rules """
        self.curl_func("SMF", "Service", "PCC Rules")

    @unittest.skipUnless(ALL or ("Service" in TAB and "Applications" in LAB), "条件为真执行测试")
    def test_smf_service_applications(self):
        """测试 Service->Applications """
        self.curl_func("SMF", "Service", "Applications")

    @unittest.skipUnless(ALL or ("Features" in TAB), "条件为真执行测试")
    def test_smf_features(self):
        """测试 Features """
        self.common_func("SMF", "Features", "")  # todo 部分

    @unittest.skipUnless(ALL or ("DNN Config" in TAB), "条件为真执行测试")
    def test_smf_features(self):
        """测试 DNN Config """
        self.common_func("SMF", "DNN Config", "")

    @unittest.skipUnless(ALL or ("Basic" in TAB and "PLMN" in LAB), "条件为真执行测试")
    def test_smf_basic_plmn(self):
        """测试 Basic->PLMN """
        self.curl_func("SMF", "Basic", "PLMN")

    def common_func(self, nf, a, b):
        """test log"""
        self.ctest_login()
        time.sleep(1)
        pngs,  err = self.lg.link_config_nf(nf)
        for png in pngs:
            self.images.append(png)

        self.assertEqual(err, "")
        time.sleep(1)
        set_datas, set_after_datas, pngs = self.lg.common_ts(a, b)
        if a == "Service" and b == "BAR Rules":
            set_datas = set_datas[:2]
            set_after_datas = set_after_datas[1:3]
        if a == "Basic" and b == "ID":
            set_datas = set_datas[0]
            set_after_datas = set_after_datas[0]
        if (a == "N4" and b == "N4 CP") or (a == "N4" and b == "N4 UP") or (a == "Service" and b == "URR Rules"):
            set_datas = set_datas[:2]
            set_after_datas = set_after_datas[:2]
        print('输入参数： {}'.format(set_datas))
        print('输出参数： {}'.format(set_after_datas))
        self.assertEqual(set_datas, set_after_datas)
        for png in pngs:
            self.images.append(png)

    def curl_func(self, nf, a, b):
        """test log"""
        self.ctest_login()
        time.sleep(1)
        pngs,  err = self.lg.link_config_nf(nf)
        for png in pngs:
            self.images.append(png)

        self.assertEqual(err, "")
        pngs = self.lg.curl_ts(a, b)
        for png in pngs:
            self.images.append(png)
        #对比文件
        self.ctest_file_diff()


    def ctest_file_diff(self):
        try:
            resp1 = self.lg.request_get_yaml()
            resp2 = self.lg.request_nf_show()
            print("yaml 配置文件 resp===", resp1)
            print("etcd 配置文件 resp===", resp2["data"])
            self.cmp(resp1, resp2["data"])
        except:
            pass
            #print("配置文件对比失败")
            #self.assertEqual("配置文件对比失败", "")

    def cmp(self, src_data, dst_data, ks=""):
        if isinstance(src_data, dict):
            """若为dict格式"""
            for key in dst_data:
                if key not in src_data:
                    pass
                    #print("diff src不存在这个key", key)
                    #self.assertEqual(src_data, dst_data)
            for key in src_data:
                if key in dst_data:
                    """递归"""
                    self.cmp(src_data[key], dst_data[key], key)
                else:
                    pass
                    #print("diff dst不存在这个key", key)
                    #self.assertEqual(src_data, dst_data)
        elif isinstance(src_data, list):
            """若为list格式"""
            if len(src_data) != len(dst_data):
                pass
                #print("diff: {} '{}' != '{}'".format(ks, src_data, dst_data))
                #self.assertEqual(src_data, dst_data)
            for src_list, dst_list in zip(src_data, dst_data):
                """递归"""
                self.cmp(src_list, dst_list)
        else:
            if str(src_data) != str(dst_data):
                pass
                #print("diff: {} '{}' != '{}'".format(ks, src_data, dst_data))
                #self.assertEqual(src_data, dst_data)
