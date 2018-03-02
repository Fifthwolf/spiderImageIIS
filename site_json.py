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

    #Bilibili相簿主页推荐
    def get_images3_1(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/index?type=recommend&page_num=0&page_size=10'
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