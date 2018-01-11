# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

url = 'http://www.lygrc.net/job/?WorkPlace=0&Trade=0&Property=0&JobProperty=0&MonthPay=0&Degree=0&WorkYears=0&JobTag=0&Weal=0&PublishDate=0&Key=&Orderid=0&Styleid=2&JobType=1200'
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = { 'User-Agent' : user_agent }
 
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
p = 0
j = 0
content_pattern = re.compile('<li class="seaList12".*?>.*?<a.*?>(.*?)</a>.*?', re.S) 
content_list = re.findall(content_pattern, html)
content_pattern1 = re.compile('li class="seaList22".*?>(.*?)</li>.*?', re.S)    
content_list1 = re.findall(content_pattern1, html)

for item in content_list:                                         
    print '\n'
    print content_list[j]                                         
    j = j + 1                                                     
                                                     

    for i in range(0,1):                                          
        print content_list1[i]

    input = raw_input()                                          
    if input == "e":       
        break
    print "******************************下一个******************************\n"
    
