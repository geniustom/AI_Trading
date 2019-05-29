# coding=UTF-8
import os,imp
import numpy as np
import common    as cm;      imp.reload(cm);
import lib.dblib as dl;      imp.reload(dl);
import lib.analytics as an;  imp.reload(an);
import matplotlib.pyplot as plt
#import time

def OutputProfit(sname):
    fname='D:/GIT/FutureStrategy/strategy/'+sname+'.py'
    if os.path.exists(fname):
        runfile(fname)
        print (sname)
        net,mdd,kelly=an.CalMDD(PC,0)
        pn.append(sname)
        pt.append([net , kelly , mdd])
        pc.append(np.array(PC))
    plt.show()

######################################################################
#                   若資料庫內容重抓，會造成無法回測，此時重開機即可
#                   若重開無校可試試執行 "顯示指標數值" 後再試一次
######################################################################

pc=[]   #績效
pt=[]   #NET & KELLY & MDD
pn=[]   #策略名
s_count=100




try:
    dbstr = db.connstr
    datecount = td.DateCount
except:
    db = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)


       
for i in range(1,s_count+1):
    sn="ms%02d" % i
    OutputProfit(sn)        
 
for i in range(1,s_count+1):
    sn="mc%02d" % i
    OutputProfit(sn)
    
for i in range(1,s_count+1):
    sn="p%02d" % i
    OutputProfit(sn)
    


T1=pn
T2=np.transpose(pt)
T3=np.array(np.transpose(pc))
TotalDate=td.DateList[datecount-800:datecount]

