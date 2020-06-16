import requests


class HttpRequest:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def http_requests(self, method, cookie=None):
        if method.upper() == 'GET':
            try:
                res = requests.get(self.url, self.data, cookies=cookie)
            except Exception as e:
                print('get请求报错{0}'.format(e))
                raise e
        elif method.upper() == 'POST':
            try:
                res = requests.post(self.url, self.data, cookies=cookie)
            except Exception as e:
                print('post请求报错{0}'.format(e))
                raise e
        else:
            res = ('请求方法错误{0}'.format(method))
        return res

# if __name__ == '__main__':
#     method = 'post'
#     url = r'http://127.0.0.1:1080/WebTours/login.pl'
#     datas = {'username': 'jojo', 'password': 'bean','login.x':'56','login.y':'10','JSFormSubmit':'off'}
#     res = HttpRequest(url, datas).http_requests(method)
#     print(res)
