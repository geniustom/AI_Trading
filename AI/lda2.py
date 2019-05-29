#!/usr/bin/env python  
#-*- coding: utf-8 -*-  
  
''''' 
LDA算法实现 
'''  
  
import os  
import sys  
#import numpy as np  
from numpy import *  
import matplotlib.pyplot as plt  
  
  
def createDataSet():  
    #group=array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1], [1.1, 1.2], [0.1, 0.2]])  
    #labels=['A','A','B','B']  
    #group1=mat([[x for x in range(1,6)], [x for x in range(1,6)]])  
    #group2=mat([[x for x in range(10,15)], [x for x in range(15, 20)]])      
    group1=mat(random.random((2,8))*5+20)  
    group2=mat(random.random((2,8))*5+2)  
    return group1, group2  
#end of createDataSet  
  
def draw(group):  
    fig=plt.figure()  
    plt.ylim(0, 30)  
    plt.xlim(0, 30)  
    ax=fig.add_subplot(111)  
    ax.scatter(group[0,:], group[1,:])  
    plt.show()  
#end of draw  
  
#计算样本均值   
#参数samples为nxm维矩阵，其中n表示维数，m表示样本个数  
def compute_mean(samples):  
    mean_mat=mean(samples, axis=1)  
    return mean_mat  
#end of compute_mean  
  
#计算样本类内离散度  
#参数samples表示样本向量矩阵，大小为nxm，其中n表示维数，m表示样本个数  
#参数mean表示均值向量，大小为1xd，d表示维数，大小与样本维数相同，即d=m  
def compute_withinclass_scatter(samples, mean):  
    #获取样本维数，样本个数      
    dimens,nums=samples.shape[:2]  
    #将所有样本向量减去均值向量  
    samples_mean=samples-mean  
    #初始化类内离散度矩阵   
    s_in=0    
    for i in range(nums):  
        x=samples_mean[:,i]  
        s_in+=dot(x,x.T)  
    #endfor  
    return s_in  
#end of compute_mean  
  
  
if __name__=='__main__':  
    group1,group2=createDataSet()  
    print "group1 :\n",group1  
    print "group2 :\n",group2  
    draw(hstack((group1, group2)))  
    mean1=compute_mean(group1)  
    print "mean1 :\n",mean1  
    mean2=compute_mean(group2)  
    print "mean2 :\n",mean2  
    s_in1=compute_withinclass_scatter(group1, mean1)  
    print "s_in1 :\n",s_in1  
    s_in2=compute_withinclass_scatter(group2, mean2)  
    print "s_in2 :\n",s_in2  
    #求总类内离散度矩阵  
    s=s_in1+s_in2  
    print "s :\n",s   
    #求s的逆矩阵  
    s_t=s.I  
    print "s_t :\n",s_t  
    #求解权向量  
    w=dot(s_t, mean1-mean2)  
    print "w :\n",w  
    #判断(2,3)是在哪一类  
    test1=mat([1,1])  
    g=dot(w.T, test1.T-0.5*(mean1-mean2))  
    print "g(x) :",g  
    #判断(4,5)是在哪一类  
    test2=mat([10,10])  
    g=dot(w.T, test2.T-0.5*(mean1-mean2))  
    print "g(x) :",g  
#endif  