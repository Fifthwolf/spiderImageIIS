#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import requests, json, re

class JsonData(object):

    #Bilibili相簿
    def title3(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=' + str(id)
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['item']['title']

    def get_images3(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id=' + str(id)
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['item']['pictures']

    #Bilibili相簿插画最新
    def get_images3_(self, commonIndex, pageNum):
        data = {
            #主页推荐
            'homeurl0': 'https://api.vc.bilibili.com/link_draw/v2/Doc/index?type=recommend&page_num=',
            
            #分栏页面
            'detailurl0': 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=',
            'detailurl1': '&page_num=',
            
            #主页最热
            '2': 'all&type=hot',
            #主页最新
            '3': 'all&type=new',
            #插画最热
            '4': 'illustration&type=hot',
            #插画最新
            '5': 'illustration&type=new',
            #漫画最热
            '6': 'comic&type=hot',
            #漫画最新
            '7': 'comic&type=new',
            #其他最热
            '8': 'draw&type=hot',
            #其他最新
            '9': 'draw&type=new'
        }
        if int(commonIndex) == 1:
            url = data['homeurl0'] + pageNum
        else:
            url = data['detailurl0'] + data[str(commonIndex)] + data['detailurl1'] + pageNum
        
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

class GetData(object):

    def __init__(self, url, common):
        self.jsonData = JsonData()
        self.common = common
        self.id = str(re.findall(r"\/([^/]+$)", url)[0])
        
    def get_title_node(self):
        return getattr(self.jsonData, 'title' + str(self.common))(self.id)

    def get_images(self):
        images = getattr(self.jsonData, 'get_images' + str(self.common))(self.id)
        return images

    def get_images_(self, commonIndex, pageNum):
        images = getattr(self.jsonData, 'get_images' + str(self.common))(commonIndex, pageNum)
        return images