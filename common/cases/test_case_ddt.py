import unittest
from ddt import ddt, data  # 处理数据--列表嵌套列表、列表嵌套字典
from common.tools.http_request import *
from common.tools.do_excel import DoExcel
from project_path import *
from common.tools.get_cookie import GetCookie

test_data = DoExcel().get_data(test_data_path)
# print(test_data)

@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        res = HttpRequest(item['url'], eval(item['data'])).http_requests(item['method'], getattr(GetCookie, 'Cookie'))
        if res.cookies:  # 反射设置cookies
            setattr(GetCookie, 'Cookie', res.cookies)
        try:
            self.assertEqual(item['expected'], res.json()['error_code'])
            test_result = 'Pass'
        except AssertionError as e:
            test_result = 'Failed'
            print('执行失败的错误时：{0}'.format(e))
            raise e
        finally:
            print('用例标题：', item['title'])
            print('返回参数：', res.json())
            DoExcel().set_data(test_data_path, item['sheet_name'], item['case_id'] + 1, 8, str(res.json()))
            DoExcel().set_data(test_data_path, item['sheet_name'], item['case_id'] + 1, 9, test_result)

    def tearDown(self):
        pass
