# -*- codeing = utf-8 -*-
# @Time : 2023/3/26 22:25
# @Author : xiaoming
# @File : workhard.py
# @Software : PyCharm

# 构造request类

# from urllib import request,parse
#
# url = 'https://www.httpbin.org/post'
#
# headers = {
#     'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)',
#     'HOST':'www.httpbin.org'
# }
# dict = {
#     'name':'xm'
# }
# data = bytes(parse.urlencode(dict),encoding = 'utf-8')
# req = request.Request(url=url,headers=headers,data=data,method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))



#####################################
# import urllib.request,urllib.parse
# data = {'name':'jcak'}
# url = 'https://www.httpbin.org/post'
# bdata = bytes(urllib.parse.urlencode(data),encoding='utf-8')#前面一个是把数据转为不是字典，让他可以被解码
#
# response = urllib.request.urlopen(url,data=bdata)
# print(response.read().decode('utf-8'))

################################
# import urllib.request
#
# url = 'https://www.httpbin.org/get'
# response = urllib.request.urlopen(url,timeout=1)
# print(response.read().decode('utf-8'))


##########################??????????????????soket.timeout
import urllib.request,urllib.error,socket

url = 'https://www.httpbin.org/get'
try:
    response = urllib.request.urlopen(url,timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT!')



