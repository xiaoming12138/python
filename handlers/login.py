#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import hashlib
from tornado.escape import json_encode
import pymongo
import json
from basehandler import *

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['userdb']

collection = db.userdb

class LoginHandler(BaseHandler):
    # def set_default_headers(self):
    #     self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
    #     self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    #     self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def get(self):
        self.render("index.html")

    def post(self):  # 处理请求，并返回
        try:
            print(self.postParam)
            print(self.postParam.get('action'))
            mark=self.postParam.get('action')
            user = self.postParam.get('user') or False
            password = self.postParam.get('password') or False
            if mark == "login":
                if user != '' and password !='':
                    res = db.userdb.find_one({"email": user,"password":  hashlib.md5(password).hexdigest()})["userid"]
                    # print(user)
                    # print(password)
                    # print(hashlib.md5(password).hexdigest())
                    #listdata = list(res)
                    print(res)

                    if res != None:
                        result = {}
                        result["userid"]=res
                        self.success(result)
                    else:
                        self.error("登录失败")
                else:
                    self.error("数据接受不全")

        except:
            self.error("数据接受不全")

        # data = json.loads(self.request.body.decode('utf-8'))
        # print('Got JSON data:', data)
        # print(data["user"])
        # print(data["password"])
        # print('Got JSON data2:', json_encode(data))

        # user = self.get_body_argument("user")
        # password = str(self.get_body_argument("password"))

        # re = db.userdb.find()
        # for results in re:
        #     print(results)
        # if user != '' and password !='':
        #     res = db.userdb.find_one({"email": user,"password":  hashlib.md5(password).hexdigest()})["userid"]
        #     # print(user)
        #     # print(password)
        #     # print(hashlib.md5(password).hexdigest())
        #     #listdata = list(res)
        #     print(res)
        #
        #     if res != None:
        #         result = {}
        #         result["data"] = {"userid":res}
        #         result["status"] = "true"
        #         result["code"] = 200
        #         result["message"] = "登录成功"
        #         self.write(json_encode(result))
        #     else:
        #         result = {}
        #         result["data"] = user
        #         result["status"] = "flase"
        #         result["code"] = 400
        #         result["message"] = "用户名密码不一致"
        #         self.write(json_encode(result))
        # else:
        #     result = {}
        #     result["data"] = "数据接受不全"
        #     result["status"] = "true"
        #     result["code"] = 400
        #     result["message"] = "数据接受不全"
        #     self.write(json_encode(result))






