# coding=UTF-8

import sys,time,imp
sys.path.append("..") 

import lib.filter as fl;     imp.reload(fl);
import lib.dblib as dl;      imp.reload(dl);
import lib.tracking as tl;   imp.reload(tl);
import lib.analytics as an;  imp.reload(an);
import matplotlib.pyplot as plt

global BackTestDays
STittle=""
PC=[]
today=time.strftime('%y/%m/%d',time.localtime(time.time()))
#today="16/08/04"
print (today)

############################################################################### 
def BackTrack(bt,fName,sName,Days=800): 
    global BackTestDays
    BackTestDays=Days
    bt.BackTrackingbyMem(sName,fName,pStartTick=15,pName=STittle,pDays=BackTestDays,pMaxLost=60,pMaxTrader=2,pCost=4)
    plt.plot(bt.datelist,bt.profitcurve_nocost,"r")
    plt.hold
    plt.plot(bt.datelist,bt.profitcurve,"b")
    tmp=bt.profithist
    an.CalMDD(tmp,1)
    return tmp

def Trade(bt,fName,sName,day):
    #print STittle,fName,sName,day
    profit=bt.DayTrade(day,sName,fName,pName=STittle,pMaxLost=60,pMaxTrader=2,pCost=4,pShowSignal=1)
    return profit
    
###############################################################################    
def runDayTrade(db,td,fName,cName,sName,sTittle,Days=800):
    global PC,STittle,today
    #print db,td,fName, cName,sName,sTittle,today
    
    STittle=sTittle
    print (STittle)
    BackTest=tl.tracking(db.conn,td)
    if cName == 'Track all':     # 若Cname=__main__ 就跑回測，否則跑單日
        PC=BackTrack(BackTest,fName,sName,Days)
    else:
        PC=Trade(BackTest,fName,sName,today)
    
    return PC
    
