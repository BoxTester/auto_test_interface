import unittest
from common.tools.http_request import *


class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    def __init__(self, methodName, url, data, method, expected):
        super(TestLogin, self).__init__(methodName)  # 超继承 保留父类方法
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected

    def test_login(self):
        res = HttpRequest(self.url, eval(self.data)).http_requests(self.method)
        try:
            self.assertEqual(self.expected, res.json()['error_code'])
        except AssertionError as e:
            print('执行是失败的错误时：{0}'.format(e))
            raise e
        finally:
            print(res.json())

    def tearDown(self):
        pass

# def test_login_no_password(self):
#     method = 'post'
#     url = 'http://127.0.0.1:1080/WebTours/login.pl'
#     datas = {'username': 'jojo', 'password': ''}
#     res = HttpRequest(url, datas).http_requests(method)
#     try:
#         self.assertEqual('<bound method Response.json of <Response [200]>>', res, '未通过')
#     except AssertionError as e:
#         print('执行是失败的错误时：{0}'.format(e))
#         raise e
#
# def test_login_no_username(self):
#     method = 'post'
#     url = 'http://127.0.0.1:1080/WebTours/login.pl'
#     datas = {'username': 'jojo', 'password': 'bean1'}
#     res = HttpRequest(url, datas).http_requests(method)
#     try:
#         self.assertEqual('<bound method Response.json of <Response [200]>>', res, '未通过')
#     except AssertionError as e:
#         print('执行是失败的错误时：{0}'.format(e))
#         raise e
#
# def test_login_wrong_password(self):
#     method = 'post'
#     url = 'http://127.0.0.1:1080/WebTours/login.pl'
#     datas = {'username': 'jojo', 'password': 'bean1'}
#     res = HttpRequest(url, datas).http_requests(method)
#     try:
#         self.assertEqual('<bound method Response.json of <Response [200]>>', res, '未通过')
#     except AssertionError as e:
#         print('执行是失败的错误时：{0}'.format(e))
#         raise e
