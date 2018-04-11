#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import hashlib

from bson import json_util
import json
from bson import ObjectId

from tornado.escape import json_encode
from basehandler import *


import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['userdb']

collectionList = db.weeklist

class WeeklyreportsHandler(BaseHandler):
    def get(self):
        try:
            userid = self.get_arguments('userid') or False       #我的周报列表
            _id = self.get_arguments('_id') or False             #周报详情
            pagenum = self.get_arguments("pagenum") or False     #分页的页数
            pagesize = self.get_arguments("pagesize") or False   #分页的每页条数
            print(userid)
            print(_id)
            print(pagenum)
            print(pagesize)

            #查询所有周报列表的接口
            if userid == False and _id == False and pagenum == False and pagesize == False :
                res = collectionList.find({"isdelete": 0}).sort("createtime", pymongo.DESCENDING)
                print(res)
                print(collectionList.find({"isdelete": 0}).count())
                if res != None:
                    result = {}
                    result = res
                    self.success(json_util.dumps(result))
                else:
                    self.error("数据获取失败")

            #查询我的周报列表接口
            elif userid != False:
                userid=int(userid[0])
                res = collectionList.find({"userid": userid}, {"isdelete": 0}).sort("createtime", pymongo.DESCENDING)
                # print(password)
                # print(hashlib.md5(password).hexdigest())
                # listdata = list(res)

                if res != None:
                    result = {}
                    result = res
                    print(result)
                    self.success(json_util.dumps(result))

                else:
                    self.error("查询失败")
            #周报详情接口
            elif _id != False:
                # _id = _id[0]
                # _id = self.get_argument("_id")
                print(_id[0])
                print("999999999")
                res = collectionList.find_one({"_id": ObjectId(_id[0])})
                if res != None:
                    result = {}
                    result = res
                    print(result)
                    self.success(json_util.dumps(result))

                else:
                    self.error("查询失败")

            # 周报分页接口
            elif pagenum != False and pagesize != False:
                pagenum = int(pagenum[0])
                pagesize = int(pagesize[0])
                pos = pagenum * pagesize
                print(pagenum)
                print(pagesize)
                res = collectionList.find({"isdelete": 0}).sort("createtime", pymongo.DESCENDING).skip(pos).limit(pagesize)
                print(res)
                totalnum = collectionList.find({"isdelete": 0}).count()
                print(totalnum)
                if res != None:
                    result = {}
                    result = res
                    print(result)
                    self.success(json_util.dumps(result))
                else:
                    self.error("查询失败")
            else:
                self.error("数据接受不全")

        except Exception as e:
            import traceback
            print e, traceback.format_exc()
            self.error("失败")


    def delete(self):
        # 删除周报接口
        try:
            print(self.postParam)
            _id = self.postParam.get("_id")
            print(_id)

            if _id != '':
                res = collectionList.update({"_id": ObjectId(_id)}, {"$set": {"isdelete": 1}})
                print(res)
                print(res["updatedExisting"])
                if res != None:
                    result = {}
                    result = res["updatedExisting"]
                    print(result)
                    self.success(json_util.dumps(result))
                else:
                    self.error("删除失败")
            else:
                self.error("数据接受不全")

        except Exception as e:
            import traceback
            print e, traceback.format_exc()
            self.error("失败")

    def put(self):
        try:
            print(self.postParam)
            mark = self.postParam.get('action') or False
            print(mark)

            # 编辑周报接口
            if mark == "editweekly_reports":
                _id = self.postParam.get("_id") or False
                content = self.postParam.gett("content") or False
                startdate = str(self.postParam.get("startdate")) or False
                enddate = str(self.postParam.get("enddate")) or False
                userid = int(self.postParam.get("userid")) or False
                # createtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                edittime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) or False

                if _id != '' and content != '' and startdate != '' and enddate != '' and userid != '' and edittime != '':
                    res = collectionList.update({"_id": ObjectId(_id)}, {"$set": {"content": content, "startdate": startdate, "enddate": enddate, "userid": userid,"edittime": edittime}})
                    print(res)

                    if res != None:
                        result = {}
                        result = res
                        print(result)
                        print(99999999)
                        self.success(json_util.dumps(result))
                    else:
                        self.error("编辑失败")
                else:
                    self.error("数据接受不全")

        except Exception as e:
            import traceback
            print e, traceback.format_exc()
            self.error("失败")


    def post(self):  # 处理请求，并返回
        try:
            print(self.postParam)
            mark = self.postParam.get('action') or False
            print(mark)

            # 添加周报接口
            if mark == "addweekly_reports":
                content = self.postParam.get("content") or False
                startdate = str(self.postParam.get("startdate")) or False
                enddate = str(self.postParam.get("enddate")) or False
                userid = int(self.postParam.get("userid")) or False
                createtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) or False

                if content != '' and startdate != '' and enddate != '' and userid != '' and createtime != '':
                    res = collectionList.insert({"content": content, "startdate": startdate, "enddate": enddate, "userid": userid, "createtime": createtime, "isdelete": 0})
                    print(res)

                    if res != None:
                        result = {}
                        result = res
                        print(result)
                        print(99999999)
                        self.success(json_util.dumps(result))
                    else:
                        self.error("添加失败")
                else:
                    self.error("数据接受不全")


        # except:
        #     self.error("数据接受不全")
        except Exception as e:
            import traceback
            print e, traceback.format_exc()
            self.error("失败")



        # res = collectionList.find({},{'_id':0})
        mogores = None
        # for results in res:
        #     print(results)
        #     mogores = results
        # res=collectionList.find({"isdelete":0}).sort("createtime",pymongo.DESCENDING)
        # listdata=list(res)
        # print(listdata)
        # print(collectionList.find({"isdelete":0}).count())
        #
        # if listdata != None:
        #     result = {}
        #     result["data"] = listdata
        #     result["status"] = "true"
        #     result["code"] = 200
        #     result["message"] = "成功"
        #     self.write(json_util.dumps(result))
        # else:
        #     result = {}
        #     result["data"] = ''
        #     result["status"] = "flase"
        #     result["code"] = 400
        #     result["message"] = "暂无信息"
        #     self.write(json_util.dumps(result))
