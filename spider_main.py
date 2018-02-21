#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import html_downloader, html_parser, json

class SpiderMain(object):

    def __init__(self, info):
        self.datas = []
        self.urls = info['urls']
        self.common = info['common']
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def craw(self):
        try:
            for url in self.urls:
                try:
                    html_cont = self.downloader.download(url)
                except:
                    html_cont = ''
                data = self.parser.parse(url, self.common, html_cont)
                self.datas.append(data)
        except:
            print 'craw failed'
        finally:
            return json.dumps(self.datas)