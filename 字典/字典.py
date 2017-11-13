Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> dict1 = { 'abc': 456 }
>>> dict1
{'abc': 456}
>>> dict1['abc']
456
>>> dict1['abc']
456
>>> dict1['abc']=678
>>> dict1['abc']
678
>>> del dict1['abc']
>>> users = {
    'A':{
    'first':'yu',
    'last':'lei',
    'location':'hs',
    },
    'B':{
    'first':'liu',
    'last':'wei',
    'location':'hs',    
    },
}
>>>  for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))
	
  File "<pyshell#8>", line 2
    for username, userinfo in users.items():
    ^
IndentationError: unexpected indent
>>>  for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))
	
  File "<pyshell#9>", line 2
    for username, userinfo in users.items():
    ^
IndentationError: unexpected indent
>>>  for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))
	
  File "<pyshell#10>", line 2
    for username, userinfo in users.items():
    ^
IndentationError: unexpected indent
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid£ºB
userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}
>>> dict = {'Name': 'fanlei', 'Age': 20}userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}
SyntaxError: invalid syntax
>>> dict = {'Name': 'fanlei', 'Age':20}
>>> 
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

20
fanlei
>>> 
