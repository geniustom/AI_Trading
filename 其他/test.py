# coding=UTF-8

import lib.dblib as dl
import lib.indicator as il
import lib.strategy_lib as sl
import lib.tracking as tl

import numpy as np
import pylab as pl
import scipy as sc
import matplotlib.pyplot as plt


try:
    print db.connstr
except:
    db = dl.DBConn(host="localhost",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)


dayindi=il.indicatorGroup()
dayindi=td.FetchDateByDB("15/09/18")


plt.plot(dayindi.get(u"大台指數"),"g")
#plt.plot(dl.seq_diff(dayindi.get(u"大台成交量")),"b")
#plt.plot(dayindi.get(u"大台散戶"),"r")
#plt.plot(dayindi.get(u"小台散戶"),"y")

#plt.plot(dayindi.get(u"大台黑手"),"g")
#plt.plot(dayindi.get(u"小台黑手"),"b")
#plt.plot(dayindi.get(u"指數波動"),"g")
#plt.plot(dayindi.get(u"小台黑手"),"r")
plt.plot(dayindi.get(u"大台高點"),"g")
plt.plot(dayindi.get(u"大台低點"),"r")





'''
#BT1=tl.tracking()
#BT1.BackTracking(strategy1,pStartTick=15,pMaxTrader=3,pMaxLost=100,pName=u"散戶主力策略")

#BT2=tl.tracking()
#BT2.BackTracking(strategy1,pStartTick=15,pMaxTrader=3,pMaxLost=150,pName=u"散戶主力策略")

#indG=BT1.TData.FetchAllData()
#plt.plot(BT1.datelist,BT1.profithist,"b")
#plt.plot(BT2.datelist,BT2.profitcurve,"y")
#plt.plot(BT1.datelist,BT1.profitcurve_nocost,"y")


ttt=dl.timer()
for i in range(0,AT.DateCount):
    tt=dl.timer()
    s1=sl.strategy(AT.DayTrade(AT.DateList[i]),StartTick=15,MaxTrader=5,Name="散戶主力策略")
    s1.Run(strategy1)
    #print s1.ProfitPoint
    #print u"交易日期：%s 績效：%s 耗時：%s"%(AT.DateList[i],s1.ProfitList,tt.spendtime("DB Query Time"))
print ttt.spendtime("Back Testing Total Time")
'''

 