#! /usr/bin/python
# Filename: Spider.py
# -*- coding: UTF-8 -*-
import urllib
url = 'http://www.google.com';
def getData(url):
    print urllib.urlopen(url).read()

getData(url)
