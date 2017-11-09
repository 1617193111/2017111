Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y = 'localpath C:\code\cnkiCrawl'
>>> inport re
SyntaxError: invalid syntax
>>> import re
>>> re.findall('\w+,y)
	   
SyntaxError: EOL while scanning string literal
>>> re.findall('\d+,y)
	   
SyntaxError: EOL while scanning string literal
>>> re.findall('\d+',y)
[]
>>> re.findall('\w+',y)
['localpath', 'C', 'code', 'cnkiCrawl']
>>> 
