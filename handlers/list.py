#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import hashlib

from bson import json_util
import json
from bson import ObjectId

from tornado.escape import json_encode


import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['userdb']

collectionList = db.weeklist

class ListHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.render("list.html")

    def post(self):  # 处理请求，并返回
        # res = collectionList.find({},{'_id':0})
        # mogores = None
        # for results in res:
        #     print(results)
        #     mogores = results
        res=collectionList.find({"isdelete":0}).sort("createtime",pymongo.DESCENDING)
        listdata=list(res)
        print(listdata)
        print(collectionList.find({"isdelete":0}).count())

        if listdata != None:
            result = {}
            result["data"] = listdata
            result["status"] = "true"
            result["code"] = 200
            result["message"] = "成功"
            self.write(json_util.dumps(result))
        else:
            result = {}
            result["data"] = ''
            result["status"] = "flase"
            result["code"] = 400
            result["message"] = "暂无信息"
            self.write(json_util.dumps(result))
