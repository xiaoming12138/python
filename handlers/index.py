#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import hashlib
from tornado.escape import json_encode
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['userdb']

collection = db.userdb

class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.render("index.html")

    def post(self):  # 处理请求，并返回

        user = self.get_body_argument("user")
        password = str(self.get_body_argument("password"))

        # re = db.userdb.find()
        # for results in re:
        #     print(results)
        res = db.userdb.find_one({"email": user,"password":  hashlib.md5(password).hexdigest()})["userid"]
        # print(user)
        # print(password)
        # print(hashlib.md5(password).hexdigest())
        #listdata = list(res)
        print(res)

        if res != None:
            result = {}
            result["data"] = {"userid":res}
            result["status"] = "true"
            result["code"] = 200
            result["message"] = "登录成功"
            self.write(json_encode(result))
        else:
            result = {}
            result["data"] = user
            result["status"] = "flase"
            result["code"] = 400
            result["message"] = "用户名密码不一致"
            self.write(json_encode(result))
