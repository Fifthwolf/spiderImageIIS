#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

class SiteData(object):

    #页面全部
    def title0(self, soup):
        return soup.title.get_text()

    def images0(self, soup):
        return soup.find_all('img')

    #AcFun文章区
    def title1(self, soup):
        return soup.find('div', {"class": "art-title-head"}).find('div', {"class": "caption"}).get_text()

    def images1(self, soup):
        return soup.find('div', {"class": "article-content"}).find_all('img')

    #Bilibili专栏
    def title2(self, soup):
        return soup.find('div', {"class": "head-container"}).find('h1', {"class": "title"}).get_text()

    def images2(self, soup):
        return soup.find_all('img')
        #return soup.find('div', {"class": "article-holder"}).find_all('img')

class GetData(object):

    def __init__(self, common):
        self.siteData = SiteData()
        self.common = common

    def get_title_node(self, soup):
        return getattr(self.siteData, 'title' + self.common)(soup)

    def get_images(self, soup):
        images_data = []
        images = getattr(self.siteData, 'images' + self.common)(soup)
        for image in images:
            images_data.append(image['src'])
        return images_data