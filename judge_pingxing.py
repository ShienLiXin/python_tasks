# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:14:29 2020

@author: shine
"""

import math  # 引入math模块 计算角度用

class point(object): # 定义空间点类
	"""docstring for point"""
	def __init__(self,x,y,z,name):
		self.x = x
		self.y = y
		self.z = z
		self.name = name
		
def distance(A, B):  # 就算两点之间的直线距离
	""""docstring for count distance bewteen two points"""
	return  math.sqrt((A.x-B.x)**2+(A.y-B.y)**2+(A.z-B.z)**2)
		
class triangle(object):  # 定义三角形类
	"""docstring for triangle"""
	def __init__(self, A,B,C,name):
		self.points=[A,B,C]  # 一个三角形三个点
		self.points_name=[A.name,B.name,C.name]  # 点的名字
		self.name = name  # 三角形的名字
		self.n=[]  # 三角形的法向量
		# self.istriangle()
		# self.norm()
		
	def istriangle(self):  # 判断这三个点是否能构成三角形
		ab = distance(self.points[0], self.points[1])
		ac = distance(self.points[0], self.points[2])
		bc = distance(self.points[1], self.points[2])
		if ab + bc > ac and ab + ac > bc and bc + ac > ab:
			print('Points:', *self.points_name, "can form triangle!")
		else:
			return print('Points:', *self.points_name, "cannot form triangle!")
		
	def normal(self):  # 获得该三角形的法向量
		self.istriangle()  # 获得该三角形的法向量前提是能构成三角形
		A,B,C=self.points  # 对应三个点
		AB=[B.x-A.x,B.y-A.y,B.z-A.z]  # 向量AB
		AC=[C.x-A.x,C.y-A.y,C.z-A.z]  # 向量AC
		B1,B2,B3=AB  # 向量AB的xyz坐标
		C1,C2,C3=AC  # 向量AC的xyz坐标
		self.n=[B2*C3-C2*B3,B3*C1-C3*B1,B1*C2-C1*B2]  # 已知该三角形的两个向量,求该三角形的法向量的叉乘公式
	
	def parallel(self, P2):  # 两个三角形的法向量是否平行
		x1,y1,z1=self.n  # 该三角形的法向量的xyz坐标
		x2,y2,z2=P2.n  # 另一个三角形的法向量的xyz坐标
		cosθ=((x1*x2)+(y1*y2)+(z1*z2))/(((x1**2+y1**2+z1**2)**0.5)*((x2**2+y2**2+z2**2)**0.5)) # 平面向量的二面角公式
		if cosθ == 1 or cosθ == -1:
			return print('三角形', self.name, P2.name, '平行')
		else:
			return print('三角形', self.name, P2.name, '不平行')

#测试
print('-'*25)
T1=point(1,0,1,'T1')  # 六个点
T2=point(0,1,1,'T2')
T3=point(0,0,1,'T3')
Tri1=triangle(T1,T2,T3,'Tri1')  # 三角形Tri1

T4=point(1,0,0,'T4')  # 六个点
T5=point(0,1,0,'T5')
T6=point(0,0,0,'T6')
Tri2=triangle(T4,T5,T6,'Tri2')  # 三角形Tri2

Tri1.normal()  # 求三角形Tri1和Tri2的法向量
Tri2.normal()
Tri1.parallel(Tri2)  # 判断三角形Tri1 和Tri 2是否平行

print('-'*25)
T7=point(1,0,1,'T7')  # 六个点
T8=point(0,1,1,'T8')
T9=point(0,0,1,'T9')
Tri3=triangle(T7,T8,T9,'Tri3')#p1平面

T10=point(1,0,0,'T10')#六个点
T11=point(0,1,0,'T11')
T12=point(0,0,1,'T12')
Tri4=triangle(T10,T11,T12,'Tri4')#p1平面

Tri3.normal()#求平面p1 p2的法向量
Tri4.normal()
Tri3.parallel(Tri4)#求平面p1 p2的夹角