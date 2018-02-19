#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import url_manager, html_downloader, html_outputer, html_parser

class SpiderMain(object):

    def __init__(self, info):
        self.urls = info['urls']
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):
        try :
            for url in self.urls:
                print 'craw %s' % url
                html_cont = self.downloader.download(url)
                data = self.parser.parse(url, html_cont)
            #self.outputer.collect_data(new_data)
        except :
            print 'craw failed'

        self.outputer.output_html()
