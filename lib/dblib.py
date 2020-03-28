# coding=UTF-8
import numpy as np
import imp
import lib.indicator as indl;       imp.reload(indl);

class timer:
    def __init__(self): 
        import time
        self.t=time.clock()
    def spendtime(self,msg=""):
        import time
        if msg=="":
            return str(time.clock()-self.t)
        else:
            return msg + " : " +str(time.clock()-self.t) + " secs"
        
def seq_diff (x):
    #return np.hstack((0,np.diff(x)))
    #return np.ediff1d(x, to_begin=0)
    y=np.zeros(x.shape,dtype=x.dtype)
    for i in range(len(x)):  #從0開始
        if i>0: y[i]=x[i]-x[i-1]
    return y

def seq_diff_pricefilter (x,p,f): #將x串列中,p的變化量大於f的部分濾除,用於過濾快市的數據
    y=np.zeros(x.shape,dtype=x.dtype)
    for i in range(len(x)):  #從0開始
        if i>0 : 
            y[i]=x[i]-x[i-1]
            if abs(p[i]-p[i-1])>f : y[i]=0
    return y
    
def seq_diff_filter (x,f): #將x串列中變化量大於cut的部分濾除
    y=np.zeros(x.shape,dtype=x.dtype)
    for i in range(len(x)):  #從0開始
        if i>0 : y[i]=(x[i]-x[i-1])
        if abs(y[i])>f: y[i]=0
    return y

def seq_intg (x):
    y=np.zeros(x.shape,dtype=x.dtype)
    y[0]=x[0]
    for i in range(len(x)):  #從0開始
        if i>0: y[i]=x[i]+y[i-1]
    return y
    
def seq_base (x):   #去除初始常數後的積分
    return seq_intg(seq_diff(x))
    
def seq_count (x):
    return x.shape
    
def getEnergy(x,ratio=0.5):
    y=np.zeros(x.shape,dtype=x.dtype)
    y[0]=x[0]
    for i in range(1,len(x)):  #從0開始
        if y[i-1]>0 : 
            y[i]=(x[i]*ratio)+y[i-1] if x[i]>0 else (x[i]+y[i-1])
        elif  y[i-1]<0:
            y[i]=(x[i]*ratio)+y[i-1] if x[i]<0 else (x[i]+y[i-1])
        else:
            y[i]=x[i]+y[i-1]
    return y

    
def WriteSignalToDB(dbconn,dTable,dDate,dTime,dStrategy,dIndex,dPrice,dUnit,dWinPoint):
    import datetime as dt
    DBC=Query(dbconn)
    SQL="Select * from %s Where TDATE='%s' and TIMEINDEX=%d and StrategyIndex='%s'" %(dTable,dDate,dIndex,dStrategy)
    #print SQL
    r, rcnt = DBC.QueryDB(SQL)
    if rcnt==0:
        SQL="Insert into %s(TDATE,TDATETIME,TIMEINDEX,Future_CurPrice,NowUnit,WinPoint,SignalTime,StrategyIndex) Values('%s','%s',%d,%d,%d,%d,'%s','%s')" %(dTable,dDate,dTime,dIndex,dPrice,dUnit,dWinPoint,dTime,dStrategy )
        #print SQL        
        DBC.ExecDB(SQL)
    #SQL = "Select * from " + dTable + "Where TDATE='" + dDate + "' ORDER BY TDATE,TIMEINDEX"

    

class DBConn:
    def __init__(self,host,uid,pwd,cata):
        import win32com.client
        tt=timer()
        self.conn=win32com.client.Dispatch(r"ADODB.Connection")
        self.connstr= "Provider=SQLNCLI.1;Persist Security Info=True;Data Source="+host+";Initial Catalog="+cata+";User ID="+uid+";Password="+pwd+";"
        self.conn.Open(self.connstr)
        print (tt.spendtime("DB Conn Time"))
        
        
class Query:
    def __init__(self,conn):
        import win32com.client
        self.cm = win32com.client.Dispatch(r"ADODB.Command")
        self.cm.CommandType = 1                     #adCmdText     #http://msdn2.microsoft.com/en-us/library/ms962122.aspx
        self.cm.ActiveConnection = conn
        self.cm.ActiveConnection.CursorLocation = 3 #static 可以使用 RecordCount 屬性
    def QueryDB(self,SQL_Str):
        self.cm.CommandText = SQL_Str
        self.cm.Parameters.Refresh()
        self.cm.Prepared = True
        (rs1, result) = self.cm.Execute() 
        return rs1, rs1.recordcount   
    def ExecDB(self,SQL_Str):
        self.cm.CommandText = SQL_Str
        self.cm.Parameters.Refresh()
        self.cm.Prepared = True
        self.cm.Execute()
        
class TradeData:
    def __init__(self,conn):
        self.dbconn=conn
        self.dt=Query(conn)
        #self.sqlfield="Future_CurPrice,TDATETIME,Future_Volume,Future_TotalBuyVol, Future_TotalSellVol,FutureWant_TrustBuyVol,FutureWant_TrustSellVol,Future_Volume,FutureWant_TrustBuyCnt,FutureWant_TrustSellCnt,FutureWant_TotalBuyCnt,FutureWant_TotalSellCnt,RealWant_Uppers,RealWant_Downs,RealWant_UpperLimits,RealWant_DownLimits,RealWant_Steadys,FutureM_Volume,FutureM_TotalBuyVol, FutureM_TotalSellVol,FutureWantM_TrustBuyVol,FutureWantM_TrustSellVol,FutureM_Volume,FutureWantM_TrustBuyCnt,FutureWantM_TrustSellCnt,FutureWantM_TotalBuyCnt,FutureWantM_TotalSellCnt,Future_TF_Volume,FutureWant_TF_TrustBuyVol,FutureWant_TF_TrustSellVol,Future_TF_Volume,FutureWant_TF_TrustBuyCnt,FutureWant_TF_TrustSellCnt,FutureWant_TF_TotalBuyCnt,FutureWant_TF_TotalSellCnt,Future_TE_Volume,FutureWant_TE_TrustBuyVol,FutureWant_TE_TrustSellVol,Future_TE_Volume,FutureWant_TE_TrustBuyCnt,FutureWant_TE_TrustSellCnt,FutureWant_TE_TotalBuyCnt,FutureWant_TE_TotalSellCnt"
        #self.sqlfield="*"
       
        self.sqlfield ="TDATETIME,Future_High,Future_Low,Real_CurPrice,"
        self.sqlfield+="RealWant_Uppers,RealWant_Downs,RealWant_UpperLimits,RealWant_DownLimits,RealWant_Steadys,"
        self.sqlfield+="Future_CurPrice   ,Future_Volume   ,FutureWant_TrustBuyVol   ,FutureWant_TrustSellVol   ,FutureWant_TrustBuyCnt   ,FutureWant_TrustSellCnt   ,FutureWant_TotalBuyCnt   ,FutureWant_TotalSellCnt   ,Future_TotalBuyVol  ,Future_TotalSellVol,"     
        self.sqlfield+="FutureM_CurPrice  ,FutureM_Volume  ,FutureWantM_TrustBuyVol  ,FutureWantM_TrustSellVol  ,FutureWantM_TrustBuyCnt  ,FutureWantM_TrustSellCnt  ,FutureWantM_TotalBuyCnt  ,FutureWantM_TotalSellCnt  ,FutureM_TotalBuyVol ,FutureM_TotalSellVol,"     
        self.sqlfield+="Future_TF_CurPrice,Future_TF_Volume,FutureWant_TF_TrustBuyVol,FutureWant_TF_TrustSellVol,FutureWant_TF_TrustBuyCnt,FutureWant_TF_TrustSellCnt,FutureWant_TF_TotalBuyCnt,FutureWant_TF_TotalSellCnt,"
        self.sqlfield+="Future_TE_CurPrice,Future_TE_Volume,FutureWant_TE_TrustBuyVol,FutureWant_TE_TrustSellVol,FutureWant_TE_TrustBuyCnt,FutureWant_TE_TrustSellCnt,FutureWant_TE_TotalBuyCnt,FutureWant_TE_TotalSellCnt"        

        r, rcnt = self.dt.QueryDB("SELECT TDATE FROM (SELECT DISTINCT TDATE FROM RealTimeFuture WHERE TDATE>'15/01/01') as NEW ORDER BY TDATE")
        rr=r.GetRows(rcnt)   
        #print rr
        self.DateList=[]            #撈db抓到的所有tdate
        self.DateListStart=[]       #對應該tdate的起始索引位置
        self.DateListEnd=[]         #對應該tdate的結束索引位置
        self.AllData=None
        for i in range(len(rr[0])):
            self.DateList.append(rr[0][i][:8])
        self.DateCount=rcnt
        
    def QueryDBtoIndicators(self,SQL_Str,indGroup=None):
        self.Qy=Query(self.dbconn)
        print(SQL_Str)
        r, rcnt= self.Qy.QueryDB(SQL_Str)
        print ("Data count : " + str(rcnt))  #just for debug
        rr=r.GetRows(rcnt)        
        if indGroup is None:
            indGroup=indl.indicatorGroup()
        indGroup.names = [field.Name for field in r.Fields]
        i=0
        for field_name in indGroup.names:
            ind=indl.indicator()
            ind.name=field_name
            ind.data=np.array(rr[i])
            i+=1
            indGroup.ids.append(ind)
        return  indGroup
    
    def FetchDateByDB(self,day):      # 即時跑策略時用
        self.DaySQL = "Select " + self.sqlfield + " from RealTimeFuture where TDATE='" + day + "' ORDER BY TIMEINDEX"
        indi=self.QueryDBtoIndicators(self.DaySQL)
        indi.GetBaseIndicator()
        return indi 

    def FetchDateByMem(self,day):     # 離線回測時用
        #沒資料時自動load資料
        if self.AllData==None:
            tt=timer()
            self.FetchAllData()
            print (tt.spendtime("DB Get All Data"))
        
        DayIndex=self.DateList.index(day)
        RecStart=self.DateListStart[DayIndex]
        RecEnd=self.DateListEnd[DayIndex]
        RecLen=RecEnd-RecStart
        indi=indl.indicatorGroup()
        for i in range(len(self.AllData.ids)):
            ids=indl.indicator()
            ids.count=RecLen
            ids.name=self.AllData.ids[i].name
            ids.data=self.AllData.ids[i].data[RecStart:RecEnd] #np.array(
            indi.ids.append(ids)
        #print self.AllData.ids[1][RecStart:RecEnd]
        #print indi.get("DATE",list_type=1)
        return indi

    def FetchAllData(self):
        # 420604 筆以上會出問題
        self.AllDataSQL = "Select " + self.sqlfield + " from RealTimeFuture WHERE TDATE>'15/01/01' ORDER BY TDATE,TIMEINDEX"
        indi=self.QueryDBtoIndicators(self.AllDataSQL)
        indi.GetBaseIndicator()    
        SearchIndex=0
        indiDayList=indi.get("DATE",list_type=1)

        for i in range(len(self.DateList)):          
            for j in range(SearchIndex,indi.len):
                if self.DateList[i]==indiDayList[j]:
                    self.DateListStart.append(SearchIndex)
                    break
                SearchIndex+=1
                
        for i in range(len(self.DateList)): 
            try:
                self.DateListEnd.append(self.DateListStart[i+1]-1)      #
            except:
                self.DateListEnd.append(indi.len)                            #最後
            
        self.AllData=indi        
        
        #indilist =indl.indicatorGroup()
        #indilist[i]
        
        
        
    