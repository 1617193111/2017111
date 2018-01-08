#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
import re

url = 'http://www.lygrc.net/job/?JobType=1200,1100,1300,1400,1600&Trade=0&WorkPlace=0&Property=0&JobProperty=0&Degree=0&WorkYears=0&Sex=0&MonthPay=0&PublishDate=0&Key='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)
html = response.read()


job = re.compile('li class="seaList12".*?>.*?<a.*?>(.*?)</a>.*?',re.S)

itmes = job.findall(html)

for itmea in itmes:
   print itmea
name = re.compile('li class="seaList13".*?>.*?<a.*?>(.*?)</a>.*?',re.S)
itmess = name.findall(html)
for itmeb in itmess:
        print itmeb
        
  
  
      
