#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re
import site_json

class SiteData(object):

    # 页面全部
    def title0(self, soup, url):
        return soup.title.get_text()

    def get_images0(self, soup, url):
        return soup.find_all('img')

    def append_images0(self, images):
        images_data = []
        for image in images:
            images_data.append(image['src'])
        return images_data

    # AcFun文章区
    def title1(self, soup, url):
        return soup.find('div', {"class": "art-title-head"}).find('div', {"class": "caption"}).get_text()

    def get_images1(self, soup, url):
        return soup.find('div', {"class": "article-content"}).find_all('img')

    def append_images1(self, images):
        images_data = []
        for image in images:
            images_data.append(image['src'])
        return images_data

    # Bilibili专栏
    def title2(self, soup, url):
        return soup.find('div', {"class": "head-container"}).find('h1', {"class": "title"}).get_text()

    def get_images2(self, soup, url):
        return soup.find('div', {"class": "article-holder"}).find_all('img')

    def append_images2(self, images):
        images_data = []
        for image in images:
            images_data.append('http:' + image['data-src'])
        return images_data

    # Bilibili相簿
    def title3(self, soup, url):
        return site_json.GetData(url, 3).get_title_node()

    def get_images3(self, soup, url):
        return site_json.GetData(url, 3).get_images()

    def append_images3(self, images):
        images_data = []
        for image in images:
            images_data.append(image['img_src'])
        return images_data

    # Bilibili相簿主页推荐、主页最热、最新;插画最热、最新;漫画最热、最新;其他最热、最新
    def title3_(self, soup, url):
        return soup.find('title').get_text()

    def get_images3_(self, soup, url, commonIndex, pageNum):
        return site_json.GetData(url, '3_').get_images_(commonIndex, pageNum)

    def append_images3_(self, items):
        ids_data = []
        for item in items:
            ids_data.append(item['item']['doc_id'])
        return ids_data

    # 知乎问题回答
    def title4(self, soup, url):
        return soup.find('head').find('title').get_text()

    def get_images4(self, soup, url):
        return soup.find('div', {"class": "QuestionAnswer-content"}).find_all('img')

    def append_images4(self, images):
        images_data = []
        for image in images:
            if not(re.match(r'^data', image['src'])):
                images_data.append(image['src'])
        return images_data

    # pixiv插图列表
    def title5(self, soup, url):
        return soup.find('head').find('title').get_text()

    def get_images5(self, soup, url):
        return soup.find('section', {"class": "manga"}).find_all('img')

    def append_images5(self, images):
        images_data = []
        for image in images:
            if not(re.match(r'^data', image['src'])):
                images_data.append(image['src'])
        return images_data

    # 微信公众号文章
    def title6(self, soup, url):
        return soup.find('div', {"class": "rich_media_inner"}).find('h2', {"class": "rich_media_title"}).get_text()

    def get_images6(self, soup, url):
        return soup.find('div', {"class": "rich_media_content"}).find_all('img')

    def append_images6(self, images):
        images_data = []
        for image in images:
            images_data.append(image['data-src'])
        return images_data

class GetData(object):

    def __init__(self, common, pageNum):
        self.siteData = SiteData()
        self.common = common
        self.pageNum = pageNum

    def get_title_node(self, soup, url):
        if not(re.match(r'\d_\d', self.common)):
            return getattr(self.siteData, 'title' + self.common)(soup, url)
        else:
            commonIndex = re.findall(r"(\d_)\d", self.common)[0]
            return getattr(self.siteData, 'title' + commonIndex)(soup, url)

    def get_images(self, soup, url):
        if not(re.match(r'\d_\d', self.common)):
            images = getattr(self.siteData, 'get_images' + self.common)(soup, url)
            images_data = getattr(self.siteData, 'append_images' + self.common)(images)
        else:
            commonIndex = re.findall(r"(\d_)(\d)", self.common)[0]
            images = getattr(self.siteData, 'get_images' + commonIndex[0])(soup, url, commonIndex[1], self.pageNum)
            images_data = getattr(self.siteData, 'append_images' + commonIndex[0])(images)
        return images_data