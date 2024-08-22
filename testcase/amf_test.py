import time
import unittest
from pageobject.project_page import *
#from webdriver_helper import debugger
from base.base_page import *
import logging
import os

class AmfTestCase(unittest.TestCase):
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
        self.assertEqual(self.lg.get_title(), "Dashboard - CORE")
        if self.lg.get_title() != "Dashboard - CORE":
            #删除redis
            print("登录失败")
        # self.images.append(self.lg.get_screenshot(self.lg.driver.current_url))
        self.lg.set_url()

    """退出"""

    def ctest_logout(self):
        self.ctest_login()
        self.lg.logout_5gc()

    # @unittest.skipUnless(ALL or ("Basic" in TAB and "LOG" in LAB), "条件为真执行测试")
    # def test_basic_log(self):
    #     """测试 AMF Basic->LOG """
    #     self.common_func("AMF", "Basic", "LOG")

    # @unittest.skipUnless(ALL or ("Basic" in TAB and "GUAMI" in LAB), "条件为真执行测试")
    # def test_basic_guami(self):
    #     """测试 AMF Basic->GUAMI """
    #     self.common_func("AMF", "Basic", "GUAMI")

    @unittest.skipUnless(ALL or ("Basic" in TAB and "Relative Capacity" in LAB), "条件为真执行测试")
    def test_basic_relative_capacity(self):

        """测试 AMF Basic->Relative Capacity """
        self.common_func("AMF", "Basic", "Relative Capacity")

    @unittest.skipUnless(ALL or ("PLMN" in TAB), "条件为真执行测试") # todo 前端修改后测试
    def test_basic_plmn(self):
        """测试 AMF PLMN """
        self.curl_func("AMF", "PLMN", "")

    @unittest.skipUnless(ALL or ("MM NAS" in TAB), "条件为真执行测试")
    def test_basic_mm_nas(self): #MM NAS todo 最后那个
        """测试 AMF MM NAS """
        self.common_func("AMF", "MM NAS", "")

    @unittest.skipUnless(ALL or ("N2" in TAB), "条件为真执行测试")
    def test_basic_n2(self):
        """测试 AMF N2 """
        self.common_func("AMF", "N2", "")

    @unittest.skipUnless(ALL or ("SBI" in TAB), "条件为真执行测试")
    def test_basic_sbi(self):
        """测试 AMF SBI """
        self.common_func("AMF", "SBI", "")

    @unittest.skipUnless(ALL or ("N26" in TAB), "条件为真执行测试")
    def test_basic_n26(self):
        """测试 AMF N26 """
        self.common_func("AMF", "N26", "")

    @unittest.skipUnless(ALL or ("Security" in TAB), "条件为真执行测试")
    def test_basic_security(self):
        """测试 AMF Security """
        self.common_func("AMF", "Security", "")

    @unittest.skipUnless(ALL or ("LADN" in TAB), "条件为真执行测试")
    def test_basic_ladn(self):
        """测试 AMF LADN """
        self.curl_func("AMF", "LADN", "")

    # @unittest.skipUnless(ALL or ("Features" in TAB), "条件为真执行测试")
    # def test_basic_features(self): #todo
    #     """测试 AMF Features """
    #     self.common_func("AMF", "Features", "")

    def common_func(self, nf, a, b):
        """test log"""
        self.ctest_login()
        time.sleep(1)
        pngs, err = self.lg.link_config_nf(nf)
        for png in pngs:
            self.images.append(png)

        self.assertEqual(err, "")
        set_datas, set_after_datas, pngs = self.lg.common_ts(a, b)
        print('输入参数： {}'.format(set_datas))
        print('输出参数： {}'.format(set_after_datas))
        self.assertEqual(set_datas, set_after_datas)
        for png in pngs:
            self.images.append(png)

    def curl_func(self, nf, a, b):
        """test log"""
        self.ctest_login()
        time.sleep(1)
        pngs, err = self.lg.link_config_nf(nf)
        for png in pngs:
            self.images.append(png)

        self.assertEqual(err, "")
        pngs = self.lg.curl_ts(a, b)
        for png in pngs:
            self.images.append(png)
        # 对比文件
        #self.ctest_file_diff()

    def ctest_file_diff(self):
        try:
            resp1 = self.lg.request_get_yaml()
            resp2 = self.lg.request_nf_show()
            print("yaml 配置文件 resp===", resp1)
            print("etcd 配置文件 resp===", resp2["data"])
            self.cmp(resp1, resp2["data"])
        except:
            pass
            # print("配置文件对比失败")
            # self.assertEqual("配置文件对比失败", "")

    def cmp(self, src_data, dst_data, ks=""):
        if isinstance(src_data, dict):
            """若为dict格式"""
            for key in dst_data:
                if key not in src_data:
                    pass
                    # print("diff src不存在这个key", key)
                    # self.assertEqual(src_data, dst_data)
            for key in src_data:
                if key in dst_data:
                    """递归"""
                    self.cmp(src_data[key], dst_data[key], key)
                else:
                    pass
                    # print("diff dst不存在这个key", key)
                    # self.assertEqual(src_data, dst_data)
        elif isinstance(src_data, list):
            """若为list格式"""
            if len(src_data) != len(dst_data):
                pass
                # print("diff: {} '{}' != '{}'".format(ks, src_data, dst_data))
                # self.assertEqual(src_data, dst_data)
            for src_list, dst_list in zip(src_data, dst_data):
                """递归"""
                self.cmp(src_list, dst_list)
        else:
            if str(src_data) != str(dst_data):
                pass
                # print("diff: {} '{}' != '{}'".format(ks, src_data, dst_data))
                # self.assertEqual(src_data, dst_data)
