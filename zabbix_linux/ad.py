# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
import json
import urllib.request

zbx_url = "http://192.168.73.143/zabbix/api_jsonrpc.php"
zabbix_user = "Admin"
zabbix_pwd = "zabbix"


def get_token():  # 得到token值，这是一个令牌，用以获取其他API
    url = zbx_url
    header = {"Content-Type": "application/json"}
    data = '''{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "%s",
        "password": "%s"},
    "id": 0
        }''' % (zabbix_user, zabbix_pwd)
    request = urllib.request.Request(url, data.encode())
    for key in header:
        request.add_header(key, header[key])
    try:
        result = urllib.request.urlopen(request)
    except urllib.request.URLError as e:
        print('error!!', e)
    else:
        response = json.loads(result.read())
        result.close()
        # print('ads')
        return response['result']


print(get_token())




