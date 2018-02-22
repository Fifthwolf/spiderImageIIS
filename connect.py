# -*- coding: UTF-8 -*-
import cgi
import public, spider_main

print("Content-Type: text/html\n")

form =  public.GetValue(cgi.FieldStorage())

info = {
    #页面地址
    'urls': form.get('pageAddress'),
    #图片地址格式，预留不使用
    'imageAddress': form.get('imageAddress')[0],
    #常用页面：Acfun或Bilibili
    'common': form.get('common')[0],
    #图片格式 jpg png gif
    'imageFormat': form.get('imageFormat')
}

obj_spider = spider_main.SpiderMain(info)
print obj_spider.craw()