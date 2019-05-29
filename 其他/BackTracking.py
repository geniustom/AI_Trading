# -*- coding: utf-8 -*-
import lib.dblib as dl
import lib.indicator as il
import lib.strategy_lib as sl
import lib.tracking as tl

import numpy as np
import pylab as pl
import scipy as sc
import matplotlib.pyplot as plt


################################  大台散戶主力策略  #################################
def strategy3(self,PRICE,i,I):
    if I.get("大台散戶")[i-1]>600  and I.get("大台主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台散戶")[i-1]<-600  and I.get("大台主力")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)

##################################  大台散戶策略  ##################################
def strategy1(self,PRICE,i,I):
    if I.get("大台散戶")[i-1]>600 : self.EnterShort(PRICE)
    if I.get("大台散戶")[i-1]<600 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)

#################################  大小台散戶策略  #################################
def strategy2(self,PRICE,i,I):
    if I.get("小台散戶")[i-1]>500  and I.get("大台散戶")[i-1]>500 : self.EnterShort(PRICE)
    if I.get("小台散戶")[i-1]<500 and I.get("大台散戶")[i-1]<500 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)



try:
    print db.connstr
except:
    db = dl.DBConn(host="localhost",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)
        

BackTest=tl.tracking(db.conn,td)
#BackTest.BackTrackingbyMem(strategy3,pStartTick=15,pMaxTrader=3,pName=u"大台散戶策略",pDays=0)
BackTest.BackTrackingbyMem(strategy2,pStartTick=15,pMaxTrader=3,pName=u"大小台散戶策略",pDays=360)



plt.plot(BackTest.datelist,BackTest.profitcurve_nocost,"r")
plt.hold
plt.plot(BackTest.datelist,BackTest.profitcurve,"b")























'''
def GetAllData(T):
    db = dl.DBConn(host="localhost",uid="sa",pwd="geniustom",cata="FutureHis")
    TradeData = dl.TradeData(db.conn)
    try: 
        if type(T.AllData.len) == int :
            print "Data Already Loded"
    except:
        tt=dl.timer()
        TradeData.FetchAllData()
        print tt.spendtime("DB Get All Data")
    return TradeData
    
#TradeData=None
#TradeData=GetAllData(TradeData)
tt=dl.timer()
day=TradeData.FetchDateByMem("14/09/05")
print tt.spendtime("DB Get Daily Data")
#print day.get("DATE")
'''