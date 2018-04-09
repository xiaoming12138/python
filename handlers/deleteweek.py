#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import hashlib

from bson import json_util
import json
from bson import ObjectId

from tornado.escape import json_encode

import time
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['userdb']

collectionList = db.weeklist

class DeleteweekHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.render("deleteweek.html")

    def post(self):  # 处理请求，并返回
        _id=self.get_body_argument("_id")
        print(_id)

        #print(json_util.dumps(list( self.request.arguments)))
        # res=collectionList.remove({"_id": ObjectId(_id)})
        if _id != '':
            res=collectionList.update({"_id":ObjectId(_id)},{"$set":{"isdelete":1}})
            print(res)
            print(res["updatedExisting"])
            #res=collectionList.find().sort("userid",pymongo.DESCENDING)
            # listdata=list(res)
            # print(listdata)

            if res != None:
                if res["updatedExisting"]==True:
                    result = {}
                    result["data"] = "删除成功"
                    result["status"] = "true"
                    result["code"] = 200
                    result["message"] = "删除成功"
                    self.write(json_util.dumps(result))
            else:
                result = {}
                result["data"] = ''
                result["status"] = "flase"
                result["code"] = 400
                result["message"] = "删除失败"
                self.write(json_util.dumps(result))
        else:
            result = {}
            result["data"] = "数据接受不全"
            result["status"] = "true"
            result["code"] = 400
            result["message"] = "数据接受不全"
            self.write(json_util.dumps(result))
