#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        data = self._get_data(page_url, soup)
        return data

    def _get_data(self, page_url, soup):
        res_data = {}
        res_data['images'] = []

        #url地址
        res_data['url'] = page_url

        #标题
        title_node = soup.find('div', {"class": "art-title-head"}).find('div', {"class": "caption"})
        res_data['title'] = title_node.get_text()

        #图片集
        images = soup.find('div', {"class": "article-content"}).find_all('img', src=re.compile(r"imgs.aixifan.com/"))
        for image in images:
            res_data['images'].append(image['src'])

        return res_data