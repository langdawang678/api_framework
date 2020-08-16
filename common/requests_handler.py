import requests

"""
封装requests方法
"""

# 基于HttpHandler.py（requests库的简单封装）
class RequestsHandler:
    def __init__(self):
        self.session = requests.Session()

    def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        """
        根据入参method判断请求的方法
        """
        # if method.lower() == "get":
        #     res = self.session.get(url, params=params, **kwargs)
        # elif method.lower == "post":
        #     res = self.session.post(url, params=params, data=data, json=json, **kwargs)
        # else:

        # sessions模块里的Session()类的request方法，可以自动判断method
        '''
            def request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
        '''
        # 一个session对象理解为一个浏览器对象，会自动关闭（建议在测试用例的灵活关闭）
        res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("result is not json")

    def close_session(self):
        self.session.close()

# 保持测试用例的独立性，所以这里注释掉，不然每个方法都是同一个浏览器对象，有些要cookies，有些不要
# req = RequestsHandler()

if __name__ == '__main__':
    httpHandle = RequestsHandler()
    httpHandle.visit("https://wwww.baidu.com", "get", )  # result is not json
