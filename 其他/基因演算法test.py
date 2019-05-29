# -*- coding: utf8 -*-
'''
------------題目--------------
y=
sin(1* x1*x2 )
-sin(2* x3*x4 )
+sin(3* x5*x6 )
-sin(4* x7*x8 )
..
..
+sin(15*x29*x30)
 
有30個整數，[1,2,3,.....,30]
分別指定給  x1,x2,x3......., x30
要如何指定，會使得 y --> max
 
------------題目--------------
'''
 
'設定環境變數'
alive = 5      #每代留下幾個最好的基因
child = 20     #一個基因生下幾個孩子
t = 500        #你要玩弄他幾次
 
from numpy import *
from random import *
from time import time
t0 = time()
 
'目標方程式'
def fun(F):
    sum = 0
    for i in xrange(15):
        sum += (-1)**i * sin((i+1)*F[(i+1)*2 - 2] * F[(i+1)*2 - 1])
    return sum
 
'排序方程式,越大的排前面'
def sort_by_last(A, B):
    if A[-1]: return 1
    elif A[-1] > B[-1]: return -1
    else: return 0
 
'產生第一代的基因'
S = range(1,31)    #第一個基因
mother = []        #母體儲存位置
 
for i in xrange(alive*child + alive):
    fir = int(random() * 30)
    sec = int(random() * 30)
    while fir == sec:
        fir = int(random() * 30)
        sec = int(random() * 30)
    tmp = S[fir]
    S[fir] = S[sec]
    S[sec] = tmp
    save = S[:]
    save.append(fun(save))
    mother.append(save)
 
'開始玩弄他'
for i in xrange(t):
    tmp = mother[:]
    tmp.sort(sort_by_last)
    mother = []
    if (i%10) == 0:
        print 'the',i,'th Times ,MAX=',fun(tmp[0])
    for j in xrange(alive):
        mother.append(tmp[j])
        ttt = tmp[j][:]
        for k in xrange(child):
            fir = int(random() * 30)
            sec = int(random() * 30)
            while fir == sec:
                fir = int(random() * 30)
                sec = int(random() * 30)
            kkk = ttt[fir]
            ttt[fir] = ttt[sec]
            ttt[sec] = kkk
            save = ttt[:]
            save[-1] = fun(save)
            mother.append(save)
 
mother.sort(sort_by_last)
print '---------------------------------------'
print 'Times = ', t
print 'take', time()-t0, 'sec'
print 'MAX = ', fun(mother[0])
print 'ANS:', mother[0]