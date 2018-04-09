#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import os

listinfo = [{"username": "alex0", "email": "78@163.com"}, {"username": "alex1", "email": "78@163.com"},
           {"username": "alex2", "email": "78@163.com"}]
for i in range(300):
    temp = {"username": "hi" + str(i), "email": "5656@com"+str(i)}
    listinfo.append(temp)  # create information


class LoginHandler(tornado.web.RequestHandler):

    def get(self, page):
        try:
            page = int(page)
        except:
            page = 1
        if page < 1:
            page = 1
        start = (page - 1) * 5
        end = page * 5
        current_list = listinfo[start:end]  # show current page
        all_page, c = divmod(len(listinfo), 5)
        if c > 1:
            all_page += 1


        page2 = []
        if all_page < 9:
            s = 1
            t = all_page
        else:
            if page < 5:
                s = 1
                t = 9
            else:
                if (page+5) > all_page:
                    s = all_page - 8
                    t = all_page
                else:
                    s = page - 4
                    t = page + 5

        head_page = "<a class = 'active' href = '/login/1'>首页</a>"
        page2.append(head_page)

        if page <= 1:
            front_page = "<a class = 'active' href = 'javascript:void(0)';></a>"
        else:
            front_page = "<a class = 'active' href = '/login/%s'>上一页</a>" % (page - 1)
        page2.append(front_page)

        for p in range(s, t):
            if p == page:
                temp = "<a class = 'active' href = '/login/%s'>%s</a>" % (p, p)
                page2.append(temp)

            else:
                temp = "<a href = '/login/%s'>%s</a>" % (p, p)
                page2.append(temp)

        if page >= all_page:
            next_page = "<a class = 'active' href = 'javascript:void(0);'></a>"
        else:
            next_page = "<a class = 'active' href = '/login/%s'>下一页</a>" % (page + 1)
        page2.append(next_page)

        tail_page = '<a class = "active"  href = "/login/%s ">尾页</a>' % all_page
        page2.append(tail_page)

        jump = """<input type='text'/><a onclick='J(this);'>GO</a>"""
        script = """<script>
        function J(ths)
        {
        var val = ths.previousElementSibling.value;
        if(val.trim().length>0){
             location.href = '/login/' + val;
            }
        }
        </script>"""
        page2.append(jump)
        page2.append(script)
        # use javascript
        str_page1 = "".join(page2)
        self.render("fenye.html", list_info=current_list, current=page, page2=str_page1)

    def post(self, page):
        username = self.get_argument("username", None)
        email = self.get_argument("email", None)
        data = {"username":username, "email": email}
        listinfo.append(data)
        self.redirect("/login/"+page) # stop current page

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics")
)

application = tornado.web.Application([
    (r"/login/(?P<page>\w*)", LoginHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()