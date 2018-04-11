#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

import sys     #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.login import LoginHandler    #假设已经有了
from handlers.weekly_reports import WeeklyreportsHandler
from handlers.addweek import AddweekHandler
from handlers.editweek import EditweekHandler
from handlers.deleteweek import DeleteweekHandler
from handlers.detailweek import DetailweekHandler
from handlers.myweek import MyweekHandler
from handlers.weekpage import WeekpageHandler

url = [
    (r'/login', LoginHandler),
    (r'/weekly_reports', WeeklyreportsHandler),
    (r'/addweek', AddweekHandler),
    (r'/editweek', EditweekHandler),
    (r'/deleteweek', DeleteweekHandler),
    (r'/detailweek', DetailweekHandler),
    (r'/myweek', MyweekHandler),
    (r'/weekpage', WeekpageHandler),

]