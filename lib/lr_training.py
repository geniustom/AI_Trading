# -*- coding: utf-8 -*-
#################################################  
# SVM: support vector machine  
# Author : zouxy  
# Date   : 2013-12-12  
# HomePage : http://blog.csdn.net/zouxy09  
# Email  : zouxy09@qq.com  
#################################################  
  
from numpy import *  
import AI.logRegression as LR;   reload(LR);
  
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
opts = {'alpha': 0.001, 'maxIter': 500, 'optimizeType': 'stocGradDescent'}  # stocGradDescent , smoothStocGradDescent
optimalWeights = LR.trainLogRegres(train_x, train_y, opts)  
  
## step 3: testing  
print "step 3: testing..."  
accuracy,pred = LR.testLogRegres(optimalWeights, test_x, test_y)  
  
## step 4: show the result  
print "step 4: show the result..."    
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)  
LR.showLogRegres(optimalWeights, train_x, train_y)   
