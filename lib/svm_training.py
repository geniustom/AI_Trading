# -*- coding: utf-8 -*-
#################################################  
# SVM: support vector machine  
# Author : zouxy  
# Date   : 2013-12-12  
# HomePage : http://blog.csdn.net/zouxy09  
# Email  : zouxy09@qq.com  
#################################################  
  
from numpy import *  
import AI.svm as SVM;   reload(SVM);
  
################## test svm #####################  
## step 1: load data  
print "step 1: load data..."  
dataSet = TrainData
labels = TrainTag

training_count=200  
dataSet = mat(TrainData)  
labels = mat(TrainTag).T  
train_x = dataSet[:training_count, :]  
train_y = labels[:training_count, :]  
test_x = dataSet[:, :]  
test_y = labels[:, :]  
  
## step 2: training...  
print "step 2: training..."  
'''
C = 100
toler = 0.1
maxIter = 1000
svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('rbf', 99999))  #'rbf or linear'
'''
C = 0.6  
toler = 0.001  
maxIter = 500  
svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0)) 
#'''
  
## step 3: testing  
print "step 3: testing..."  
accuracy,pred = SVM.testSVM(svmClassifier, test_x, test_y)  
  
## step 4: show the result  
print "step 4: show the result..."    
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)  
SVM.showSVM(svmClassifier)  
