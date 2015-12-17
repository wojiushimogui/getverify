#encoding=utf-8
#Author:wuranghao
#Date   :2015年12月17日20:29:21
#HomePage :http://write.blog.csdn.net/postlist
#email:wuranghao@foxmail.com
#function:get verify
from pytesser import *
import Image
#由于都是数字  
#对于识别成字母的 采用该表进行修正  
rep={'O':'0',  
	'I':'1','L':'1',  
	'Z':'2',  
	'S':'8'  
	};
def getVerify(picName):
	#Step 1:open picture
	im=Image.open(picName)
	#Step 2:make pic to gry
	imgry=im.convert("L")
	#Step 3:set a threshold to trim noise
	table=[]
	threshold=140
	for i in range(256):
		if i<threshold:
			table.append(0)
		else:
			table.append(1)
	#map
	out=imgry.point(table,'1')
	#Step 4:get text
	text=image_to_string(out)
	#Step 5:deal some error
	text=text.strip()
	for r in rep:
		text=text.replace(r,rep[r])
	print text
	return text
getVerify("example_3.jpg")