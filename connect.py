# -*- coding: UTF-8 -*-
import cgi
import spider_main

print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<html lang=\"en\">")
print("<head>")
print("<meta charset=\"UTF-8\">")
print("<title>图片获取工具</title>")
print("</head>")

class GetValue(object):

    def __init__(self, form):
        self.form = form

    def get(self, name):
        list = []
        try:
            self.value = self.form[name].value
            list = [self.value]
        except:
            for value in self.form[name]:
                list.append(value.value)
        finally:
            return list

form = GetValue(cgi.FieldStorage())

info = {
    #页面地址
    'urls': form.get('pageAddress'),
    #图片地址格式，预留不使用
    'imageAddress': form.get('imageAddress'),
    #常用页面：Acfun或Bilibili
    'common': form.get('common'),
    #图片格式 jpg png gif
    'imageFormat': form.get('imageFormat')
}

obj_spider = spider_main.SpiderMain(info)
obj_spider.craw()