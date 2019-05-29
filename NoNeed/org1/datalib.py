# coding=UTF-8

import numpy as np
import indicator as indl

class timer:
    def __init__(self): 
        import time
        self.t=time.clock()
    def spendtime(self,msg):
        import time
        return msg + " : " +str(time.clock()-self.t) + " secs"
        
                
class DB:
    def __init__(self,connstr):
        import win32com.client
        self.d=indl.indicatorGroup()
        self.count=0
        self.dbconn=win32com.client.Dispatch(r"ADODB.Connection")
        self.dbconn.Open(connstr)
    def QueryDB(self,SQL_Str):
        import win32com.client
        cm = win32com.client.Dispatch(r"ADODB.Command")
        cm.ActiveConnection = self.dbconn
        cm.CommandType = 1#adCmdText     #http://msdn2.microsoft.com/en-us/library/ms962122.aspx
        cm.ActiveConnection.CursorLocation = 3 #static 可以使用 RecordCount 屬性
        cm.CommandText = SQL_Str
        cm.Parameters.Refresh()
        cm.Prepared = True
        (rs1, result) = cm.Execute() 
        return rs1, rs1.recordcount        
    def QueryDBtoIndicators(self,SQL_Str):
        r, rcnt= self.QueryDB(SQL_Str)
        rr=r.GetRows(rcnt)        
        self.d.names = [field.Name for field in r.Fields]
        i=0
        for field_name in self.d.names:
            ind=indl.indicator()
            ind.name=field_name
            ind.data=np.array(rr[i])
            i+=1
            self.d.ids.append(ind)
        return  self.d


class AutoTrade:
    def __init__(self,host,uid,pwd):
        self.connstr= "Provider=SQLNCLI.1;Persist Security Info=True;Data Source="+host+";Initial Catalog=FutureHis;User ID="+uid+";Password="+pwd+";"
        self.sqlfield="Future_CurPrice,TDATETIME,Future_Volume,Future_TotalBuyVol, Future_TotalSellVol,FutureWant_TrustBuyVol,FutureWant_TrustSellVol,Future_Volume,FutureWant_TrustBuyCnt,FutureWant_TrustSellCnt,FutureWant_TotalBuyCnt,FutureWant_TotalSellCnt,FutureWant_TF_TotalBuyCnt,FutureWant_TF_TotalSellCnt,FutureWant_TE_TotalBuyCnt,FutureWant_TE_TotalSellCnt,RealWant_Uppers,RealWant_Downs,RealWant_UpperLimits,RealWant_DownLimits,RealWant_Steadys,FutureM_Volume,FutureM_TotalBuyVol, FutureM_TotalSellVol,FutureWantM_TrustBuyVol,FutureWantM_TrustSellVol,FutureM_Volume,FutureWantM_TrustBuyCnt,FutureWantM_TrustSellCnt,FutureWantM_TotalBuyCnt,FutureWantM_TotalSellCnt"
        self.DB=DB(self.connstr)
        r, rcnt = self.DB.QueryDB("SELECT TDATE FROM (SELECT DISTINCT TDATE FROM RealTimeFuture) as NEW ORDER BY TDATE")
        rr=r.GetRows(rcnt)   
        self.DateList=[]
        for i in range(len(rr[0])):
            self.DateList.append(rr[0][i][:8])
        self.DateCount=rcnt
        
    def DayTrade(self,day):
        self.indi=indl.indicatorGroup()
        SQL = "Select " + self.sqlfield + " from RealTimeFuture where TDATE='" + day + "'"
        self.indi=self.DB.QueryDBtoIndicators(SQL)
        self.indi.GetBaseIndicator()
        return self.indi
            

        
def seq_diff (x):
    #return np.hstack((0,np.diff(x)))
    #return np.ediff1d(x, to_begin=0)
    y=np.zeros(x.shape,dtype=x.dtype)
    for i in range(len(x)):  #從0開始
        if i>0: y[i]=x[i]-x[i-1]
    return y

def seq_intg (x):
    y=np.zeros(x.shape,dtype=x.dtype)
    for i in range(len(x)):  #從0開始
        if i>0: y[i]=x[i]+y[i-1]
    return y
    
def seq_base (x):   #去除初始常數後的積分
    return seq_intg(seq_diff(x))
    
def seq_count (x):
    return x.shape
        