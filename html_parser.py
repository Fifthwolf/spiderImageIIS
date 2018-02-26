#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import site_data
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parse(self, page_url, site_common, html_cont):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        data = self._get_data(page_url, site_common, soup)
        return data

    def _get_data(self, page_url, common, soup):
        self.get_data = site_data.GetData(common)
        res_data = {}

        #url地址
        res_data['url'] = page_url

        #标题
        try:
            res_data['title'] = self.get_data.get_title_node(soup, page_url)
        except :
            res_data['title'] = '无效地址'
        
        #图片集
        try:
            res_data['images'] = self.get_data.get_images(soup, page_url)
        except:
            res_data['images'] = ['empty']
        
        return res_data