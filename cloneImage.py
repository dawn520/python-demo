#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib
import re

import time


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getUrl2(url):
    html = getHtml(url)
    reg = r'<a id="openStation[^>]*href="(.+?)"[^>]*>'
    urlre = re.compile(reg, re.IGNORECASE)
    urlList = re.findall(urlre, html)
    print urlList
    return urlList


def getImg(html):
    ##print html
    ##reg = r'src="(.+?\.jpg)"[^>]*width="800"[^>]*'
    reg = r'<img[^>]*alt="室内图[^>]*src="(.+?\.jpg)[^"]*"[^>]*>'
    imgre = re.compile(reg, re.IGNORECASE)
    imglist = re.findall(imgre, html)
    print imglist

    for imgurl in imglist:
        x = time.time()
        urllib.urlretrieve(imgurl, './images/%s.jpg' % x)


if __name__ == '__main__':
    os.mkdir('./images');
    for i in range(200, 600, 1):
        URL1 = 'http://www.haozu.com/sz_gxbg_' + str(i)
        print URL1 + ':开始下载！'
        URL2 = getUrl2(URL1)
        for item in URL2:
            item = "http://www.haozu.com" + item
            html = getHtml(item)
            print "----" + item + ':开始下载！'
            getImg(html)
            print item + ':下载完成！'
