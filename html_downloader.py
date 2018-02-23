#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib2

class HtmlDownloader(object):
    #可用
    #def download(self, url):
    def download1(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

    def download(self, url):
    #def download(self, url):
        req = urllib2.Request(url)  
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.5.2000")
        req.add_header("GET", url)
        req.add_header("Referer", url)
        response = urllib2.urlopen(req)

        if response.getcode() != 200:
            return None
        return response.read()