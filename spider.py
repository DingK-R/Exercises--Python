#! /usr/bin/python
# Filename: Spider.py
# -*- coding: UTF-8 -*-
import urllib
import time 
import os
import re

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
        #fopen.write(fileName)
        #fp = open(data, 'r')
        #Read file and get url
        #content = fp.read(fileName);
        content = data
        pattern = '<a\s*href=\"(.*?)\"'
        res = re.compile(pattern)
        matchs = res.findall(content)
        if matchs != None:
            alist = []
            for found in matchs:
                if found not in alist:
                    alist.append(found)
                print alist

        #fp.close
        
        fopen.close
    else:
        os.mkdir(dirPath)
        print 'make dir'



getData(url)
