# -*- codeing = utf-8 -*-
# @Time : 2023/3/29 16:36
# @Author : xiaoming
# @File : daili.py
# @Software : PyCharm

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
