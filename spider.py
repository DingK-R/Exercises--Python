#! /usr/bin/python
# Filename: Spider.py
# -*- coding: UTF-8 -*-
import urllib
import time 
import os

url = 'http://www.baidu.com';
def getData(url):
    delimiter = '/' # should i use const ?
    data = urllib.urlopen(url).read()
    
    fileName = time.strftime( '%Y-%m-%d_%H:%s',time.localtime( time.time() ) ) + '.html'
    filePath = os.getcwd() + delimiter + fileName
    dirPath = os.getcwd() + delimiter + 'html'

    if os.path.exists(dirPath):
         os.chdir(dirPath)
         fopen = open( fileName, 'w')
         fopen.write(data)
         fp = open(fileName, 'r')


         fopen.close
    else:
        os.mkdir(dirPath)
        print 'make dir'



getData(url)
