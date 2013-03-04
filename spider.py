#! /usr/bin/python
# Filename: Spider.py
import urllib
url = 'http://www.google.com';
def getData(url):
    """ 读取google页面
    """
    print urllib.urlopen(url).read()

getData(url)
