# coding=UTF-8

import os
import common    as cm;      reload(cm);
import lib.dblib as dl;      reload(dl);
import s40_i;reload(s40_i);



try:
    dbstr = db.connstr
    datecount = td.DateCount
except:
    db = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)


def daytrade(s):
    return cm.runDayTrade(db,td,fName=s.FName,cName=__name__,sName=s.s1,sTittle=s.STittle)


daytrade(s40_i)
