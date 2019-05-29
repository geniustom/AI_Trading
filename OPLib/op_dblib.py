# coding=UTF-8

import numpy as np
import time
import op_indicator as indl;       reload(indl);

class timer:
    def __init__(self): 
        self.t=time.clock()
    def spendtime(self,msg=""):
        if msg=="":
            return str(time.clock()-self.t)
        else:
            return msg + " : " +str(time.clock()-self.t) + " secs"
            
class DBConn:
    def __init__(self,host,uid,pwd,cata):
        import win32com.client
        tt=timer()
        self.conn=win32com.client.Dispatch(r"ADODB.Connection")
        self.connstr= "Provider=SQLNCLI.1;Persist Security Info=True;Data Source="+host+";Initial Catalog="+cata+";User ID="+uid+";Password="+pwd+";"
        self.conn.Open(self.connstr)
        print tt.spendtime("OPDB Conn Time")
        
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
        self.sqlfield="C_CurPrice,C_TrustBuyCnt,C_TrustSellCnt,C_TrustBuyVol,C_TrustSellVol,C_TotalBuyCnt,C_TotalSellCnt,C_Volume"    #TimeIndex,Contract,Sprice,
        r, rcnt = self.dt.QueryDB("SELECT convert(varchar,TDATE,11) FROM (SELECT DISTINCT TDATE FROM RealTimeOption WHERE Future_CurPrice<>0) AS NEW ORDER BY TDATE")
        rr=r.GetRows(rcnt)   
        #print rr
        self.DateList=[]            #撈db抓到的所有tdate
        self.DateListStart=[]       #對應該tdate的起始索引位置
        self.DateListEnd=[]         #對應該tdate的結束索引位置
        self.DateTXWTag=[]          #周選擇權每天的TAG
        self.DateATMPrice=[]        #周選擇權每天的開盤價平履約價
        self.AllData=[]             #用於回測的所有資料
        for i in range(len(rr[0])):
            self.DateList.append(rr[0][i][:8])
        self.DateCount=rcnt
    
    def GetTXWTag(self,day):   #輸入日期，回傳合約TAG (因為第三周是結算周)
        OPTag=""
        opdbcmd = Query(self.dbconn)    
        dbsql=u"SELECT TOP 1 product_hammer FROM RealTimeOption WHERE (TDate = '"+day+"') AND (product_hammer = 'TXW0P') AND (Future_CurPrice<>0)"
        r, rcnt = opdbcmd.QueryDB(dbsql)
        if rcnt==0:
            dbsql=u"SELECT TOP 1 product_hammer FROM RealTimeOption WHERE (TDate = '"+day+"') AND (product_hammer = 'TXO00P') AND (Future_CurPrice<>0)"
            rr, rrcnt = opdbcmd.QueryDB(dbsql)
            if rrcnt==1:
                OPTag= "TXO00"
        else:
            OPTag="TXW0"
        return OPTag        

    #價內（ITM, In The Money）才有履約的價值；價外（OTM, Out of The Money）和價平（ATM, At The Money）
    def GetOPATMPrice(self,day,OPTag,showinfo):
        FOpen=0    
        OPATMPrice=0
        opdbcmd = Query(self.dbconn)
        dbsql=u"SELECT TOP 1 Future_CurPrice FROM RealTimeOption WHERE (TDate = '"+day+"') AND (product_hammer = '"+OPTag+"P') AND (Future_CurPrice<>0) ORDER BY TimeIndex"
        #print dbsql
        r, rcnt = opdbcmd.QueryDB(dbsql)
        if rcnt==1:
            rr=r.GetRows(rcnt)  
            FOpen=int(rr[0][0])
            OPATMPrice=int(round(float(FOpen)/50,0)*50)      
            if showinfo==1 :
                print day,"期貨開盤:",FOpen," 價平:",OPATMPrice," TAG:",OPTag
        return FOpen,OPATMPrice,OPTag
    
    def GetAllATMPrice(self):
        for i in range(self.DateCount):
            self.DateTXWTag.append(self.GetTXWTag(self.DateList[i]))
            self.DateATMPrice.append(self.GetOPATMPrice(self.DateList[i],self.DateTXWTag[i],0)[1])       

    def QueryDBtoIndicators(self,d,p,t,cp,prefix,indGroup=None):  #d=日期 t=合約tag p=履約價 ,cp=C or P , prefix=標題
        self.Qy=Query(self.dbconn)
        SQL_Str=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p)+") AND (product_hammer = '"+t+cp+"') ORDER BY TimeIndex"

        r, rcnt= self.Qy.QueryDB(SQL_Str)
        #print "Data count : " + str(rcnt)  #just for debug
        rr=r.GetRows(rcnt)        
        if indGroup is None:
            indGroup=indl.indicatorGroup()
        indGroup.names = [field.Name for field in r.Fields]
        i=0
        for field_name in indGroup.names:
            ind=indl.indicator()
            ind.name=prefix+"_"+field_name
            ind.data=np.array(rr[i])
            ind.count=len(rr[i])
            i+=1
            indGroup.ids.append(ind)
        return  indGroup
    
    def FetchDataByDate(self,d,p,t):
        indi=None
        indi=self.QueryDBtoIndicators(d,p+50 ,t,"C","CO1",indi)
        indi=self.QueryDBtoIndicators(d,p    ,t,"C","CAT",indi)
        indi=self.QueryDBtoIndicators(d,p-50 ,t,"C","CI1",indi)
        indi=self.QueryDBtoIndicators(d,p-100,t,"C","CI2",indi)
        indi=self.QueryDBtoIndicators(d,p-50 ,t,"P","PO1",indi)
        indi=self.QueryDBtoIndicators(d,p    ,t,"P","PAT",indi)
        indi=self.QueryDBtoIndicators(d,p+50 ,t,"P","PI1",indi)
        indi=self.QueryDBtoIndicators(d,p+100,t,"P","PI2",indi)
        indi.GetBaseIndicator()
        return indi        
        
    def FetchAllData(self):
        tt=timer()   
        self.GetAllATMPrice()
        print tt.spendtime("OPDB GetAllATMPrice Time")
        tt=timer() 
        if self.AllData==[]:
            for i in range(self.DateCount):  
                d=self.DateList[i]
                p=self.DateATMPrice[i]
                t=self.DateTXWTag[i]
                indi=self.FetchDataByDate(d,p,t)
                self.AllData.append(indi) #操作方式 optd.AllData[第幾交易日].ids[第幾個數列].data
        print tt.spendtime("OPDB QueryDBtoIndicators Time")    
    

def WriteSignalToDB(dbc,dTable,dDate,dTime,dStrategy,dIndex,dPrice,dUnit,dWinPoint,dSprice,dContract,dLots): 
    OrderContract="%s%05d%s" % (dContract[0:3],dSprice,dContract[3:5])
    dContract=OrderContract
    DBC=Query(dbc.conn)    
    SQL="Select * from %s Where TDATE='%s' and TIMEINDEX=%d and StrategyIndex='%s' and Option_Sprice=%d and Option_Contract='%s' and Lots=%d " %(dTable,dDate,dIndex,dStrategy,dSprice,dContract,dLots)
    #print SQL
    
    r, rcnt = DBC.QueryDB(SQL)
    if rcnt==0:
        SQL="Insert into %s(TDATE,TDATETIME,TIMEINDEX,Option_CurPrice,NowUnit,WinPoint,SignalTime,StrategyIndex,Option_Sprice,Option_Contract,Lots) Values('%s','%s',%d,%f,%d,%d,'%s','%s',%d,'%s',%d)" %(dTable,dDate,dTime,dIndex,dPrice,dUnit,dWinPoint,dTime,dStrategy,dSprice,dContract,dLots)
        #print SQL        
        DBC.ExecDB(SQL)

def seq_intg (x):
    y=np.zeros(x.shape,dtype=x.dtype)
    y[0]=x[0]
    for i in range(len(x)):  #從0開始
        if i>0: y[i]=x[i]+y[i-1]
    return y        
        
def seq_diff (x):
    #return np.hstack((0,np.diff(x)))
    #return np.ediff1d(x, to_begin=0)
    y=np.zeros(x.shape,dtype=x.dtype)
    for i in range(len(x)):  #從0開始
        if i>0: y[i]=x[i]-x[i-1]
    return y  
    
    
    
    
'''
    def FetchDateByDB(self,d,p,t):
        CO1=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p+50)+")     AND (product_hammer = '"+t+"C') ORDER BY TimeIndex"
        CAT=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p)+")        AND (product_hammer = '"+t+"C') ORDER BY TimeIndex"            
        CI1=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p-50)+")     AND (product_hammer = '"+t+"C') ORDER BY TimeIndex"
        CI2=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p-100)+")    AND (product_hammer = '"+t+"C') ORDER BY TimeIndex"
        PO1=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p-50)+")     AND (product_hammer = '"+t+"P') ORDER BY TimeIndex"
        PAT=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p)+")        AND (product_hammer = '"+t+"P') ORDER BY TimeIndex"            
        PI1=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p+50)+")     AND (product_hammer = '"+t+"P') ORDER BY TimeIndex"
        PI2=u"SELECT "+self.sqlfield+" FROM RealTimeOption WHERE (TDate = '"+d+"') AND (Sprice = "+str(p+100)+")    AND (product_hammer = '"+t+"P') ORDER BY TimeIndex"
'''