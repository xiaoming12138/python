#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

import sys     #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler    #假设已经有了
from handlers.list import ListHandler
from handlers.addweek import AddweekHandler
from handlers.editweek import EditweekHandler
from handlers.deleteweek import DeleteweekHandler

url = [
    (r'/', IndexHandler),
    (r'/list', ListHandler),
    (r'/addweek', AddweekHandler),
    (r'/editweek', EditweekHandler),
    (r'/deleteweek', DeleteweekHandler),
    # (r'/detailweek', DeleteweekHandler),
]