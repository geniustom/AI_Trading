# -*- coding: utf-8 -*-

import sys   
sys.path.append("..") 

import lib.dblib as dl
import lib.indicator as il
import lib.strategy_lib as sl
import lib.tracking as tl
import lib.analytics as an

import numpy as np
import pylab as pl
import scipy as sc
import matplotlib.pyplot as plt






dbc = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
tdc=dl.TradeData(dbc.conn)
dayindi=il.indicatorGroup()


def getIndiInRange(tag_name,start,end):
    d=[]
    for i in range(start,end,1):
        dayindi=tdc.FetchDateByDB(tdc.DateList[i])
        il.GetSpecialIndicator(dayindi)
        t=np.array(dayindi.get(tag_name))
        d.extend(t)
    return d

def seq_intg(x):
    y=x     #np.zeros(x.shape,dtype=x.dtype)
    y[0]=0
    for i in range(len(x)):  #從0開始
        if i>0: y[i]=x[i]+y[i-1]
    return y


d_start=1342            #1165,1185
d_end=1362
output=[]
t1= getIndiInRange(u"大台指數",d_start,d_end) 
t2= getIndiInRange(u"大台主力",d_start,d_end)
t3= getIndiInRange(u"大台散戶",d_start,d_end)
t4= getIndiInRange(u"大台黑手",d_start,d_end)
t5= getIndiInRange(u"小台未純化主力企圖",d_start,d_end) 
t6= getIndiInRange(u"小台未純化主力作為",d_start,d_end)
t7= getIndiInRange(u"慢市小台未純化主力企圖",d_start,d_end)
t8= getIndiInRange(u"慢市小台未純化主力作為",d_start,d_end)

output.append((t1,t2,t3,t4,t5,t6,t7,t8))
output=np.array(output)

#tg= seq_intg(tt)

#plt.figure(figsize=(8,7),dpi=98)
plt.figure()
p1 = plt.subplot(211)
p2 = plt.subplot(212)
p1.plot(t1)
p2.plot(t2)  #dl.seq_intg(dl.seq_diff(tt))




'''
#dayindi=td.FetchDateByDB("15/07/03")
#dayindi=td.FetchDateByDB("15/07/09")
#dayindi=td.FetchDateByDB("15/07/13")
#dayindi=td.FetchDateByDB("15/08/11")
#dayindi=td.FetchDateByDB("15/03/26")  #史上賠最慘的一天
#dayindi=td.FetchDateByDB("16/01/28")  #該做多但籌碼卻偏空的一天
dayindi=tdc.FetchDateByDB("16/01/22")  #開盤跌80點到11:30後漲了100點 (要想辦法賺兩趟)
il.GetSpecialIndicator(dayindi)

#plt.plot(dayindi.get(u"大台指數"),"g")

plt.plot(-dayindi.get(u"大台散戶"),"r")
plt.plot(dayindi.get(u"大台黑手"),"g")
plt.plot(-dayindi.get(u"小台散戶"),"y")



#plt.plot(dayindi.get(u"慢市金期買賣差"),"r")
#plt.plot(dayindi.get(u"慢市電期買賣差"),"g")

plt.plot(dayindi.get(u"小台未純化主力企圖"),"c")
plt.plot(dayindi.get(u"金期未純化主力企圖"),"r")
plt.plot(dayindi.get(u"電期未純化主力企圖"),"g")

#plt.plot(dayindi.get(u"慢市大台黑手"),"r")
#plt.plot(dayindi.get(u"慢市小台黑手"),"g")

#plt.plot(dayindi.get(u"中市大台黑手"),"b")
#plt.plot(dayindi.get(u"中市小台黑手"),"y")

#plt.plot(dayindi.get(u"大台黑手"),"g")
#plt.plot(dayindi.get(u"小台黑手"),"r")

#plt.plot(dayindi.get(u"中市大台未純化主力企圖")-dayindi.get(u"中市小台未純化主力企圖"),"r")
#plt.plot(dayindi.get(u"中市小台未純化主力企圖"),"g")

#plt.plot(dayindi.get(u"慢市大台散戶"),"r")
#plt.plot(dayindi.get(u"慢市小台散戶"),"g")

#plt.plot(dayindi.get(u"小台黑手"),"g")

#plt.plot(dayindi.get(u"大台純主力買企圖")-dayindi.get(u"大台純主力賣企圖"),"b")
#plt.plot(dayindi.get(u"大台純散戶買企圖")-dayindi.get(u"大台純散戶賣企圖"),"c")
#plt.plot(dayindi.get(u"小台純主力買企圖")-dayindi.get(u"小台純主力賣企圖"),"g")
#plt.plot(dayindi.get(u"小台純散戶買企圖")-dayindi.get(u"小台純散戶賣企圖"),"y")

#plt.plot(dayindi.get(u"上漲家數"),"y")
#plt.plot(dayindi.get(u"下跌家數"),"g")
#plt.plot(dayindi.get(u"平盤家數"),"b")

#plt.plot(dayindi.get(u"慢市小台未純化主力企圖"),"r")
#plt.plot(dayindi.get(u"小台未純化主力企圖"),"g")

#plt.plot(dayindi.get(u"小台買賣差"),"g")
#plt.plot(dayindi.get(u"慢市小台買賣差"),"r")
#plt.plot(dayindi.get(u"慢市大台買賣差"),"g")

#plt.plot(dayindi.get(u"小台黑手"),"g")
#plt.plot(dayindi.get(u"慢市小台黑手"),"r")

#plt.plot(dayindi.get(u"慢市上漲家數變動"),"r")
#plt.plot(dayindi.get(u"慢市下跌家數變動"),"g")

#plt.plot(dayindi.get(u"大台黑手")+dayindi.get(u"小台黑手"),"r")
#plt.plot(-dayindi.get(u"大台散戶")-dayindi.get(u"小台散戶"),"g")

#plt.plot(dayindi.get(u"大台黑手"),"r")
#plt.plot(-dayindi.get(u"小台散戶"),"g")

plt.plot(dayindi.get(u"指數波動"),"b")

'''