#encoding=utf-8
#Author:wuranghao
#Date   :2015年12月17日20:29:21
#HomePage :http://write.blog.csdn.net/postlist
#email:wuranghao@foxmail.com
#function:get verify

from pytesser import *
import Image
#第一步：打开图像
Image.open("example_3.PNG").convert('RGB').save('example_5.jpg')#进行格式转换
im=Image.open("example_5.jpg")
#im.show()
#第二步：把彩色图像转化为灰度图像
imgry=im.convert('L')
#第三步：把图像中的噪声去除掉这里的图像比较简单，直接阈值化就行了。我们把大于阈值threshold的像素置为1，其他的置为0。
#对此，先生成一张查找表，映射过程让库函数帮我们做。
threshold=140
table=[]
for i in range(256):
	if i<threshold:
		table.append(0)
	else:
		table.append(1)
##映射
out=imgry.point(table,'1')
##第四步：把图片中的字符转化为文本，采用pytesser中的image_to_string函数
text=image_to_string(out)

print text
