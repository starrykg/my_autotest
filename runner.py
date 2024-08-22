from XTestRunner import HTMLTestRunner
import time
import unittest
#from testcase.amf_test import AmfTestCase
#from testcase.smf_test import SmfTestCase
#from testcase.udm_test import UdmTestCase
from testcase.upf_test import UpfTestCase
from testcase.nrf_test import NrfTestCase
from testcase.ausf_test import AusfTestCase
from testcase.nssf_test import NssfTestCase

"""
运行测试代码
输出文件名： ./reports/5gc_test_ + 当前时间.html
"""

if __name__ == '__main__':
    suit = unittest.TestSuite()
    # suit.addTests([
    #     #LoginTestCase("test_login"),
    #     LoginTestCase("test_logout"),
    #     #LoginTestCase("test_udm_config"),
    # ])

    file_name = "./reports/5gc_test_" + time.strftime('%Y-%m-%d_%H-%M-%S') + ".html"
    with(open(file_name, 'wb')) as fp:
        unittest.main(testRunner=HTMLTestRunner(
            tester='auto',
            stream=fp,
            title='5gc auto test report',
            description=['tool：selenium', 'os：linux', 'browser：Chrome']
        ))

    fp.close()
