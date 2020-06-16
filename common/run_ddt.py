import unittest
import HTMLTestRunnerCN
from common.cases.test_case_ddt import TestApi
from project_path import *

suite = unittest.TestSuite()
# ddt 用loader
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestApi))  # loadTestsFromTestCase加载测试类中指定测试用例

with open(test_result_html_path, 'wb') as file:
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=file, verbosity=2, title='接口自动化测试报告',
                                               description='所有的测试用例', tester='zbx')
    runner.run(suite)
