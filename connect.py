# -*- coding: UTF-8 -*-
import cgi
import public, spider_main

print("Content-Type: text/html\n")

form = public.GetValue(cgi.FieldStorage())

info = {
    #页面地址
    'urls': form.get('pageAddress'),
    #常用页面：Acfun或Bilibili
    'common': form.get('common')[0],
}

#页面序号
try:
	info['pageNum'] = form.get('pageNum')[0]
except :
	info['pageNum'] = 0

obj_spider = spider_main.SpiderMain(info)
print obj_spider.craw()