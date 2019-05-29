# -*- coding: utf-8 -*-
import lib.dblib as dl
import lib.indicator as il
import lib.strategy_lib as sl
import lib.tracking as tl

import numpy as np
import pylab as pl
import scipy as sc
import scipy.linalg as la
import matplotlib.pyplot as plt



try:
    print db.connstr
except:
    db = dl.DBConn(host="localhost",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)

td.DateCount
twidx=[]
for i in range(td.DateCount):
    dayindi=il.indicatorGroup()
    dayindi=td.FetchDateByMem(td.DateList[i])
    vector=dayindi.get(u"指數波動")
    
    if  len(vector)==300 and (vector[10]<1000):
        K_len= abs(vector[299])  
        Down_Shdow_len = abs(min(vector)+K_len)
        Up_Shdow_len = abs(max(vector)-K_len)
        Shdow_len=Down_Shdow_len+Up_Shdow_len 
        K_Range= max(vector)-min(vector)
        low=min(vector)
        hi=max(vector)
        for j in range(len(vector)):
            vector[j]-=low
            
        #實體K棒 >上下影線 ----->258次
        #if K_len>Shdow_len:

        #實體K棒 >30點 且 實體K棒>上下影線----->354次
        #if K_len>Down_Shdow_len and K_len>Up_Shdow_len and K_len>30:

        #實體K棒 >30點 且 實體K棒>上下影線----->354次
        #if K_len>Shdow_len and K_len>30:

        #大型盤整 K棒<30點但震幅>30點 ----->406次
        #if K_len<30 and K_Range>30: 
        
        #小型盤整雙八 上下震幅60點內,但K棒<30點 ----->326次
        #if  K_Range<60 and K_len<30:
        twidx.append(vector)
    
    #plt.plot(dayindi.get(u"大台指數"),"g")
    #lt.hold

#plt.plot(twidx)     
twidxm=np.array(twidx).T
#plt.plot(twidxm)  

twidxcov=np.cov(twidxm)
#plt.plot(twidxcov[:,1:100])    
ev,twidxeig=la.eig(twidxcov)


twidxeigT=twidxeig.T
#plt.plot(ev)     
#plt.hold
for k in range(5):
    plt.plot(twidxeigT[k]) 

#plt.plot(twidxeigT[3]) 
#plt.plot(twidxeig[5]) 
#twidxeig=la.eig(np.matrix(twidx))  

#for i in range(100):    
#    plt.plot(twidxeig[i])    