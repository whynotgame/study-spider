# -*- codeing = utf-8 -*-
# @Time : 2023/4/9 16:01
# @Author : xiaoming
# @File : request.py
# @Software : PyCharm


# import urllib.request
#
# request = urllib.request.Request('https://www.baidu.com')
# response = urllib.request.urlopen(request)
#
# print(response.read().decode('utf-8'))

##################################################

# import urllib.request,urllib.parse
#
# url = 'https://www.httpbin.org/post'
# data = {'name':'jack'}
# headers = {
#     'user-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host':'muji'
# }
# bdata = bytes(urllib.parse.urlencode(data),encoding='utf-8')
# req = urllib.request.Request(url,headers=headers,data=bdata,method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

##################################################

import urllib.request,urllib.parse

url = 'https://www.httpbin.org/post'
data = {'name':'jack'}


req = urllib.request.Request(url,data=bytes(urllib.parse.urlencode(data),encoding='utf-8'))
req.add_header('host','jiayu')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

