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

class EditweekHandler(tornado.web.RequestHandler):
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
        _id=self.get_body_argument("_id")
        content = self.get_body_argument("content")
        startdate = str(self.get_body_argument("startdate"))
        enddate = str(self.get_body_argument("enddate"))
        userid = self.get_body_argument("userid")
        #createtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        edittime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        res=collectionList.update({"_id":_id},{"$set":{"content": content, "startdate": startdate, "enddate": enddate, "userid": userid, "edittime": edittime}})
        print(res)
        #res=collectionList.find().sort("userid",pymongo.DESCENDING)
        # listdata=list(res)
        # print(listdata)

        if res != None:
            result = {}
            result["data"] = res
            result["status"] = "true"
            result["code"] = 200
            result["message"] = "编辑成功"
            self.write(json_util.dumps(result))
        else:
            result = {}
            result["data"] = ''
            result["status"] = "flase"
            result["code"] = 400
            result["message"] = "编辑失败"
            self.write(json_util.dumps(result))
