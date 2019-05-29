#-*- coding: UTF-8 -*-
from numpy import *
import numpy as np
import AI.svm as SVM;   reload(SVM);


def lda(c1,c2,maxn):
    #c1 第一类样本，每行是一个样本
    #c2 第二类样本，每行是一个样本

    #计算各类样本的均值和所有样本均值
    m1=mean(c1,axis=0)#第一类样本均值
    m2=mean(c2,axis=0)#第二类样本均值
    c=vstack((c1,c2))#所有样本
    m=mean(c,axis=0)#所有样本的均值

    #计算类内离散度矩阵Sw
    n1=c1.shape[0]#第一类样本数
    print(n1);
    n2=c2.shape[0]#第二类样本数
    print(n2);
    #求第一类样本的散列矩阵s1
    s1=0
    for i in range(0,n1):
        s1=s1+(c1[i,:]-m1).T*(c1[i,:]-m1)
    #求第二类样本的散列矩阵s2
    s2=0
    for i in range(0,n2):
        s2=s2+(c2[i,:]-m2).T*(c2[i,:]-m2)
    Sw=(n1*s1+n2*s2) #/(n1+n2)
    #计算类间离散度矩阵Sb
    Sb=(n1*(m-m1).T*(m-m1)+n2*(m-m2).T*(m-m2)) #/(n1+n2)
    #求最大特征值对应的特征向量
    invSw=linalg.pinv(Sw)
    eigvalue,eigvector=linalg.eig(invSw*Sb)#特征值和特征向量
    indexVec=numpy.argsort(-eigvalue)#对eigvalue从大到小排序，返回索引
    E=sorted(eigvalue,reverse = True)
    nLargestIndex=indexVec[:maxn] #取出最大的特征值的索引
    W=eigvector[:,nLargestIndex] #取出最大的特征值对应的特征向量
    Wc1=mat(W.T*c1.T).T
    Wc2=mat(W.T*c2.T).T
    return E,W,Wc1,Wc2
    
def raw2c1c2(raw,tag):
    #將原始資料根據tag分成兩群,原始資料=一列一個樣本
    n=raw.shape[0]
    c1=[]
    c2=[]
    for i in range(0,n):
        vector=raw[i,:]
        if tag[i]==1:
            c1.append(vector)
        else:
            c2.append(vector)
    return mat(c1),mat(c2)

def testLDA(w, test_x, test_y,wc1,wc2): 
    numTestSamples = test_x.shape[0]
    pred_result=[]
    matchCount=0
    for i in range(0,numTestSamples):
        c1l=np.linalg.norm(wc1-test_x[i]) #/wc1.shape[0]
        c2l=np.linalg.norm(wc2-test_x[i]) #/wc2.shape[0]
        if c1l>c2l:
            predict=-1
        else:
            predict=1
        print [c1l,c2l]
        pred_result.append(predict)
        if predict==test_y[i]:
            matchCount += 1
            
    accuracy = float(matchCount) / numTestSamples  
    return accuracy,array(pred_result)
    
#=============================================================
'''
print "step 0: pre test..."     
TrainData = []  
TrainTag = []  
fileIn = open('D:/GIT/FutureStrategy/AI/testSet.txt')
for line in fileIn.readlines():  
    lineArr = line.strip().split('\t')  
    TrainData.append([float(lineArr[0]), float(lineArr[1])])  
    TrainTag.append(float(lineArr[2]))  
TrainData=array(TrainData)
TrainTag=array(TrainTag).T
#'''

print "step 1: load data..."  
training_count=200
C1,C2=raw2c1c2(TrainData[:training_count,:],TrainTag[:training_count])

  
## step 2: training...  
print "step 2: training..."  
E,Wopt,Wc1,Wc2=lda(C1,C2,200)
dataSet = mat(Wopt.T*TrainData.T).T
labels = mat(TrainTag).T  
train_x = dataSet[:training_count, :]
train_y = labels[:training_count, :]  
test_x = dataSet[:, :]  
test_y = labels[:, :]  
  
## step 3: testing  
print "step 3: testing..."  
accuracy,pred = testLDA(Wopt,test_x,test_y,Wc1,Wc2)  
  
## step 4: show the result  
print "step 4: show the result..."    
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)  
#SVM.showSVM(svmClassifier) 




