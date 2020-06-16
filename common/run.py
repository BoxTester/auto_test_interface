import unittest
import HTMLTestRunnerCN
from common.cases.test_case import TestLogin
from common.tools.do_excel import DoExcel
from common.tools.do_config import DoConfig
from project_path import *

suite = unittest.TestSuite()

# 读取config中数据
# config_file_name = conf_path
# section = 'MODE'
# option = 'mode'
# mode = DoConfig().read_config(config_file_name, section, option)
# print(mode)
# 数据提前处理放在内存中，对内存要求较高（从excel读取后拼接成可用数据存在test_data中）
# 数据在用的时候取，对硬盘读写要求较高（直接从excel中读取）
# file_name = test_data_path
# sheet_name = 'test'
# test_data = DoExcel(file_name).get_data(sheet_name,mode)
# print(test_data)

test_data = DoExcel().get_data(test_data_path)
print(test_data)

for item in test_data:
    suite.addTest(TestLogin('test_login', item['url'], item['data'], item['method'], item['expected']))

with open(test_result_html_path, 'wb') as file:
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=file, title='测试报告', verbosity=2)
    runner.run(suite)