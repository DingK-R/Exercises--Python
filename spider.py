#! /usr/bin/python
# Filename: Spider.py
# -*- coding: UTF-8 -*-
# author: David Ding

import urllib
import time 
import os
import re

url = 'http://www.baidu.com';
def getData(url):
    delimiter = '/' # should i use const ?
    fileName = time.strftime( '%Y-%m-%d_%H:%I:%S',time.localtime( time.time() ) ) + '.md'
    filePath = os.getcwd() + delimiter + fileName
    dirPath = os.getcwd() + delimiter + 'data'
    
    data = urllib.urlopen(url).read()
    
    if os.path.exists(dirPath):
        pattern = '<a\s*href=\"(.*?)\"'
        res = re.compile(pattern)
        matchs = res.findall(data)
        if matchs != None:
            alist = []
            for found in matchs:
                if found not in alist:
                    alist.append(found)
            
            os.chdir(dirPath)
            fopen = open( fileName, 'w')
            fopen.write(str(alist))
            fopen.close
    else:
        os.mkdir(dirPath)
        print 'make dir'



getData(url)
