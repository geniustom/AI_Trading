# coding=UTF-8

import numpy as np
import time
import matplotlib.pyplot as plt
global OPTAG

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
        
def GetOPPrice(dbc,day):
    FOpen=0    
    OPInPrice=0
    opdbcmd = Query(dbc.conn)
    dbsql=u"SELECT TOP 1 Future_CurPrice FROM RealTimeOption WHERE (TDate = '"+day+"') AND (product_hammer = '"+OPTAG+"P') AND (Future_CurPrice<>0) ORDER BY TimeIndex"
    #print dbsql
    r, rcnt = opdbcmd.QueryDB(dbsql)
    if rcnt==1:
        rr=r.GetRows(rcnt)  
        FOpen=int(rr[0][0])
        OPInPrice=int(round(float(FOpen)/50,0)*50)
        
    print "日期",day,"期貨開盤:",FOpen," 價平CP:",OPInPrice," TAG:",OPTAG
    return FOpen,OPInPrice
        
def GetMainPower(n1,n2,n3):    #n1,n2,n3 = 買成筆,賣成筆,成交量
    bpower=np.zeros(len(n1))
    spower=np.zeros(len(n1))
    allpower=np.zeros(len(n1))
    
    for i in range(0,len(n1)):
        bpower[i]= (float(n3[i])/float(n1[i])) if n1[i]!=0 else 0
        spower[i]= (float(n3[i])/float(n2[i])) if n2[i]!=0 else 0
        allpower[i]=(bpower[i]-spower[i])
        
    return allpower


def GetOPPower(dbc,day,cp,sprice):
    opdbcmd = Query(dbc.conn)
    #         0         1       2        3            4             5             6              7             8               9         10                11
    field="TimeIndex,Contract,Sprice,C_CurPrice,C_TrustBuyCnt,C_TrustSellCnt,C_TrustBuyVol,C_TrustSellVol,C_TotalBuyCnt,C_TotalSellCnt,C_Volume,CONVERT(char(5), TDateTime, 108)"    
    dbsql=u"SELECT "+field+" FROM RealTimeOption WHERE (TDate = '"+day+"') AND (Sprice = "+str(sprice)+") AND (product_hammer = '"+OPTAG+cp+"') ORDER BY TimeIndex"
    #print dbsql    
    r, rcnt = opdbcmd.QueryDB(dbsql)
    rr=r.GetRows(rcnt) 
    
    Contract=rr[1][0]
    SPrice=rr[2][0]
    Price=rr[3]
    Vol=rr[10]
    TimeStr=rr[11]
    #################  主力  #################    
    MainPower=GetMainPower(np.array(rr[8]),np.array(rr[9]),np.array(rr[10]))
    #print MainPower
    #################  散戶  #################
    after_bcnt=np.array(rr[8])
    after_scnt=np.array(rr[9])
    BadPower=seq_intg(seq_diff(after_bcnt-after_scnt))
    #print BadPower
    return Contract,SPrice,MainPower,BadPower,Price,Vol,TimeStr


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




# MainPower[i-1]<0 and and BadPower[i-1]>0      
def RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,CP,lots,T):
    tradecnt=0
    unit=0
    Profit=0
    for i in range(len(MainPower)):
        if i<5:
            continue
        #if MainPower[i-1]>0 and BadPower[i-1]>10 and unit==0 and tradecnt==0 and i>=15 and i<100 : #and Price[i-1]>Price[10]+5:
        if MainPower[i-1]<-0.3 and unit==0 and tradecnt==0 and i>=5 and i<100 and Price[i-1]>Price[10]+5:         
            unit=-1
            tradecnt+=1
            Profit=Price[i]
            print "Sell",str(SPrice),CP,"@",Price[i] , "x", lots ," at " , T[i]
            WriteSignalToDB(opdb,"OptionSignal",day,T[i],"s1",i,Price[i],-1,0,SPrice,Contract,lots)
        elif MainPower[i-1]>0.3 and unit==-1:
            Profit=(unit*(Price[i]-Profit)-3)*lots             
            unit=0
            print "Stop",str(SPrice),CP,"@",Price[i] , "x", lots ," at " , T[i]         
            WriteSignalToDB(opdb,"OptionSignal",day,T[i],"s1",i,Price[i],0,Profit,SPrice,Contract,lots)
        elif unit==-1 and Price[i-1]>Profit+50:
            Profit=(unit*(Price[i]-Profit)-3)*lots             
            unit=0
            print "Stop",str(SPrice),CP,"@",Price[i] , "x", lots ," at " , T[i]         
            WriteSignalToDB(opdb,"OptionSignal",day,T[i],"s1",i,Price[i],0,Profit,SPrice,Contract,lots)           
        elif unit==-1 and i>290:
            Profit=(unit*(Price[i]-Profit)-3)*lots            
            unit=0
            print "Exit",str(SPrice),CP,"@",Price[i] , "x", lots ," at " , T[i]
            WriteSignalToDB(opdb,"OptionSignal",day,T[i],"s1",i,Price[i],0,Profit,SPrice,Contract,lots)    
    if unit==0:  
        return Profit 
    else: 
        return 0


''' 
心得
1. 操作價內並設2成停損的效果較好
2. 價平適合逆勢操作
3. 價外適合做買方，不適合做賣方

'''


def Run(day):
    GetTag(opdb,day)
    FP,INP=GetOPPrice(opdb,day)
    TotalProfit=0

    
    #Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"C",INP+100)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C",1,T)
    
    #Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"C",INP+50)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C",1,T)

    Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"C",INP)
    TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C",1,T)
    
    Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"C",INP-50)
    TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C",1,T)

    #Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"C",INP-100)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C",1,T)

    #Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"C",INP-150)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C",1,T)
    
    #遇到下跌容易爆噴，不考慮
    #Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"P",INP-50)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P",1,T)

    #遇到下跌容易爆噴，不考慮
    Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"P",INP)
    TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P",1,T)
    
    Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"P",INP+50)
    TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P",1,T)
    
    #Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"P",INP+100)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P",1,T)
    
    #Contract,SPrice,MainPower,BadPower,Price,Vol,T=GetOPPower(opdb,day,"P",INP+150)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P",1,T)
    
    #plt.plot(MainPower)
    print "今日總績效:",TotalProfit
    return TotalProfit


# 很慘的組合2016/04/15 = SC價平、內1、內2 + SC、內1、內2

def GetTag(dbc,day):   #輸入日期，回傳合約TAG (因為第三周是結算周)
    global OPTAG
    opdbcmd = Query(dbc.conn)    
    dbsql=u"SELECT TOP 1 product_hammer FROM RealTimeOption WHERE (TDate = '"+day+"') AND (product_hammer = 'TXW0P') AND (Future_CurPrice<>0)"
    r, rcnt = opdbcmd.QueryDB(dbsql)
    if rcnt==0:
        dbsql=u"SELECT TOP 1 product_hammer FROM RealTimeOption WHERE (TDate = '"+day+"') AND (product_hammer = 'TXO00P') AND (Future_CurPrice<>0)"
        rr, rrcnt = opdbcmd.QueryDB(dbsql)
        if rrcnt==1:
            OPTAG= "TXO00"
    else:
        OPTAG="TXW0"


try:
    opdbstr = self.connstr
    datecount = td.DateCount
except:
    opdb = DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="OPHis")       #127.0.0.1  192.168.1.103
    
OPTAG=""
today=time.strftime('%y/%m/%d')
print today

#'''
####################   以下為實際上線    ###################
try:
    profit=Run(today)
except:
    profit=Run("16/04/15")
    
print "============================"
print "所有總績效：",profit


#'''
####################   以下為近日回測    ###################
def GetDate(dbc):
    global DateList
    global rr
    opdbcmd = Query(dbc.conn)
    r, rcnt = opdbcmd.QueryDB("SELECT TDATE FROM (SELECT DISTINCT TDATE FROM RealTimeOption WHERE TDATE>'13/01/01') as NEW ORDER BY TDATE")
    rr=r.GetRows(rcnt)   
    DateList=[]            #撈db抓到的所有tdate
    for i in range(len(rr[0])):
        DateList.append(rr[0][i].Format("%y/%m/%d"))
        
DateList=[]
profit=[]
GetDate(opdb)
for i in range(24,len(DateList)):
    profit.append(Run(DateList[i]))
    
print "============================"
print "每日績效：",profit,"所有總績效：",sum(profit)
profitcurve=[]
profitcurve.append(profit[0])
for i in range(1,len(profit)):
    profitcurve.append(profit[i]+profitcurve[i-1])
plt.plot(profitcurve)
#'''














'''
def GetMainPower(n1,n2,n3,n4):    #n1,n2,n3,n4 = 委買口,委賣口,委買筆,委賣筆
    bpower=np.zeros(len(n1))
    spower=np.zeros(len(n1))
    allpower=np.zeros(len(n1))
    ret=np.zeros(len(n1))
    
    for i in range(10,len(n1)):
        bpower[i]= (float(n1[i])/float(n3[i])) if n3[i]!=0 else 0
        spower[i]= (float(n2[i])/float(n4[i])) if n4[i]!=0 else 0
        allpower[i]=(bpower[i]-spower[i])
        if i>0:
            ret[i]=ret[i-1]+(allpower[i]-allpower[i-1])
        
    return ret

def GetMainPower(n1,n2,n3,n4):    #n1,n2,n3,n4 = 委買口,委賣口,委買筆,委賣筆
    bpower=np.zeros(len(n1))
    spower=np.zeros(len(n1))
    ret=np.zeros(len(n1))
    
    for i in range(0,len(n1)-1):
        bpower[i]= (float(n1[i])/float(n3[i])) if n3[i]!=0 else 0
        spower[i]= (float(n2[i])/float(n4[i])) if n4[i]!=0 else 0
        ret[i]=bpower[i]-spower[i]
        
    return seq_intg(seq_diff(ret))
    

'''

'''
def RunOPStrategy(Contract,SPrice,MainPower,BadPower,Price,CP):
    tradecnt=0
    unit=0
    for i in range(len(MainPower)):
        if MainPower[i]<-1 and unit==0 and tradecnt==0 and i>15 and i<200:
            unit=-1
            tradecnt=1
            print "Sell ",str(SPrice),CP," in ",Price[i] , "at " , i
        if MainPower[i]>1 and unit==-1:
            unit=0
            print "Exit ",str(SPrice),CP," in ",Price[i] , "at " , i           
            
        if unit==-1 and i>290:
            unit=0
            print "Exit ",str(SPrice),CP," in ",Price[i] , "at " , i   
'''

'''  輸出日期資料
r, rcnt = opdbcmd.QueryDB("SELECT TDATE FROM (SELECT DISTINCT TDATE FROM RealTimeOption) as NEW ORDER BY TDATE")
rr=r.GetRows(rcnt)   
print rcnt
'''

'''       
class TradeData:
    def __init__(self,conn):
        self.dbconn=conn
        self.dt=Query(conn)
        r, rcnt = self.dt.QueryDB("SELECT TDATE FROM (SELECT DISTINCT TDATE FROM hammer) as NEW ORDER BY TDATE")
        rr=r.GetRows(rcnt)   
        #print rr
        self.DateList=[]            #撈db抓到的所有tdate
        self.DateListStart=[]       #對應該tdate的起始索引位置
        self.DateListEnd=[]         #對應該tdate的結束索引位置
        self.AllData=None
        for i in range(len(rr[0])):
            self.DateList.append(rr[0][i][:8])
        self.DateCount=rcnt        
        
    def FetchDateByDB(self,day):      # 即時跑策略時用
        self.DaySQL = "Select * from hammer where TDATE='" + day + "' ORDER BY TIMEINDEX"
        indi=self.QueryDBtoIndicators(self.DaySQL)
        indi.GetBaseIndicator()
        return indi         
''' 

