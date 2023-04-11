# -*- codeing = utf-8 -*-
# @Time : 2023/4/6 17:42
# @Author : xiaoming
# @File : cookie.py
# @Software : PyCharm

# import http.cookiejar,urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + "=" + item.value)

# import urllib.request,http.cookiejar
#
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

import urllib.request,http.cookiejar
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))


