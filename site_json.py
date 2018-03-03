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

    #Bilibili相簿主页最热
    def get_images3_2(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/index?type=hot&page_num=0&page_size=10'
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

    #Bilibili相簿主页最新
    def get_images3_3(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/index?type=new&page_num=0&page_size=10'
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

    #Bilibili相簿插画最热
    def get_images3_4(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=illustration&type=hot&page_num=0&page_size=20'
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

    #Bilibili相簿插画最新
    def get_images3_5(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=illustration&type=new&page_num=0&page_size=20'
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

    #Bilibili相簿插画最热
    def get_images3_6(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=comic&type=hot&page_num=0&page_size=20'
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

    #Bilibili相簿插画最新
    def get_images3_7(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=comic&type=new&page_num=0&page_size=20'
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

    #Bilibili相簿其他最热
    def get_images3_8(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=draw&type=hot&page_num=0&page_size=20'
        comments = requests.get(url)
        comments.encoding = 'utf-8'
        jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
        return jd['data']['items']

    #Bilibili相簿插画最新
    def get_images3_9(self, id):
        url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=draw&type=new&page_num=0&page_size=20'
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