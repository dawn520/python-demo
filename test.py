#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
# sentence = raw_input('请输入你想说的话：')
# print sentence
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1


html = getHtml("http://blog.zhouchenxi.cn")

print getImg(html)
