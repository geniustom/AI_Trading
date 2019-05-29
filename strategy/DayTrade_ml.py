# coding=UTF-8

import os,imp
import common    as cm;      imp.reload(cm);
import lib.dblib as dl;      imp.reload(dl);
import lib.indicator as ind; imp.reload(ind);
import ms01,ms02,ms03,ms04,ms05,ms06,ms07,ms08,ms09,ms10,ms11,ms12,ms13,ms14,ms15,ms16
#import ml01,ml02,ml03,ml04,ml05,ml06,ml07,ml08,ml09,ml10
import p01,p02,p03,p04,p05,p06


try:
    dbstr = db.connstr
    datecount = td.DateCount
except:
    db = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)

def daytrade(s):
    return cm.runDayTrade(db,td,fName=s.FName,cName=__name__,sName=s.s1,sTittle=s.STittle)

TotalProfit=0
TotalProfit+= daytrade(ms01)
TotalProfit+= daytrade(ms02)
TotalProfit+= daytrade(ms03)
TotalProfit+= daytrade(ms04)
TotalProfit+= daytrade(ms05)
TotalProfit+= daytrade(ms06)
TotalProfit+= daytrade(ms07)
TotalProfit+= daytrade(ms08)
TotalProfit+= daytrade(ms09)
TotalProfit+= daytrade(ms10)
TotalProfit+= daytrade(ms11)
TotalProfit+= daytrade(ms12)
TotalProfit+= daytrade(ms13)
TotalProfit+= daytrade(ms14)
TotalProfit+= daytrade(ms15)
TotalProfit+= daytrade(ms16)

TotalProfit+= daytrade(p01)
TotalProfit+= daytrade(p02)
TotalProfit+= daytrade(p03)
TotalProfit+= daytrade(p04)
TotalProfit+= daytrade(p05)
TotalProfit+= daytrade(p06)


print ( u"\n\n今日總績效:",TotalProfit)
