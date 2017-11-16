import urllib  
import urllib2  
 
url = 'http://cuiqingcai.com/954.html'
user_agent = 'Mozilla/5.0 (Windows NT 6.1)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() 
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1)'  ,
                        'Referer':'http://www.cuiqingcai.com/954.html' }  
