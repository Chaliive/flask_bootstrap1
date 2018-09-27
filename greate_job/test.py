# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
# sdk api
import urllib.request
import json
from greate_job.ad import get_token
from greate_job import ad
# import os
#
# strr = os.popen("fab -H localhost main -f fab_1.py").read()
#
# print(strr)
# print(s)
# zbx_params = '''{
#     "output": "extend",
#     "filter": {
#     "name": ["Zabbix server"]
#     }
#     }'''  # 只得到Zabbix server的信息
zbx_params = '''{
    "output": "extend",
    "actionids":"3"
    }'''  # 只得到Zabbix server的信息
# zbx_params = '''{
#     "output": "extend",
#     "selectDServices":"extend",
#     "druleids":"4"
#     }'''
# zbx_token = get_token()
# zbx_action = "host.get"
# zbx_action = "alert.get"


def zbx_req(zbx_action_par, zbx_token_par):
    zbx_params_par = '''{
        "output": "extend",
        "actionids":"3"
        }'''
    header = {"Content-Type": "application/json"}
    url = ad.zbx_url
    data = '''{
    "jsonrpc": "2.0",
    "method": "%s",
    "params": %s,
    "auth": "%s",
    "id": 1 }''' % (zbx_action_par, zbx_params_par, zbx_token_par)

    request = urllib.request.Request(url, data.encode())
    for key in header:
        request.add_header(key, header[key])
    try:
        result = urllib.request.urlopen(request)
    except urllib.request.URLError as e:
        print('error')
    else:
        response = json.loads(result.read())
        if 'error' in response:
            print(response['error'])
            return False
        elif not response['result']:
            print(response)
            return False
        else:
            return response['result']
        result.close()


# print(zbx_req(zbx_action, zbx_params, zbx_token))


