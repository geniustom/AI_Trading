# -*- coding: utf-8 -*-
import imp
import numpy as np
import strategy.common    as cm;             imp.reload(cm);
import lib.dblib as dl;             imp.reload(dl);
import lib.indicator as ind;        imp.reload(ind);

try:
    dbstr = db.connstr
    datecount = td.DateCount
except:
    db = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)


BackTestDays=800  #need >40
PC=np.array(cm.runDayTrade(db,td,fName=FName,cName="Track all",sName=s1,sTittle=STittle,Days=BackTestDays))

'''
TrainTag=np.zeros(PC.shape,dtype=PC.dtype)
for i in range(0,len(PC)):
    if PC[i]>0: TrainTag[i]=1
    else: TrainTag[i]=0
'''