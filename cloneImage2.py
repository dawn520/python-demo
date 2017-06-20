#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
# sentence = raw_input('请输入你想说的话：')
# print sentence
import urllib
import re

import time


def getHtml(url):

    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    ##print html
    ##reg = r'src="(.+?\.jpg)"[^>]*width="800"[^>]*'
    reg = r'<img[^>]*src="(.+?\.jpg)"[^>]*width="800"[^>]*>'
    imgre = re.compile(reg,re.IGNORECASE)
    imglist = re.findall(imgre, html)

    for imgurl in imglist:
        x = time.time()
        urllib.urlretrieve(imgurl, '%s.jpg' % x)

for i in range(100):
    pid = str(i)
    html = getHtml("http://www.omiaozu.com/buildDetails/" + pid + "/")
    print getImg(html)


