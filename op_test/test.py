# coding=UTF-8

import oplib.op_dblib as dl;      reload(dl);



try:
    opdbstr = opdb.connstr
    datecount = optd.DateCount
except:
    opdb = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="OPHis")
    optd=dl.TradeData(opdb.conn)
    
    
#print optd.GetTXWTag("16/04/1")
#optd.GetAllATMPrice()
optd.FetchAllData()
aa=optd.AllData
