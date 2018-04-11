#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Liufujie@cmcm.com 2017-12-25
#系统基类，用于权限控制，日志记录，公共函数

import json
import traceback
import tornado.web
import os
import hashlib
import tornado
import time


class BaseHandler(tornado.web.RequestHandler):
    print("1111111111")
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.postParam = self.get_body

        # 开放前段跨域
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Origin", "*")


    @property
    def get_body(self):
        try:
            return json.loads(self.request.body)
        except:
            return {}

    def error(self,msg):
        self.finish({
            'status': 400,
            'msg': msg
        })

    def success(self,data):
        self.finish({
            'status': 200,
            'msg': 'success',
            'data':data
        })

    # def pwdMX(self,_str):
    #     pwd_salt = self.conf['pwdSalt']
    #     return md5(pwd_salt + str(_str) + pwd_salt)  # 密码加盐

    def __error_deal(self,code=500, msg='位置错误'):
        self.finish({
            "status": 500,
            "msg": msg
        })
        os._exit(1)


    def options(self):
        self.set_status(204)
        self.finish()


# def md5(_str):
#     se_md5 = hashlib.md5(_str)
#     return se_md5.hexdigest()