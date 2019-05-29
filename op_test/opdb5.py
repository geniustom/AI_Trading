# coding=UTF-8

import numpy as np
import time
import matplotlib.pyplot as plt

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
    dbsql=u"SELECT TOP 1 Real_CurPrice FROM RealTimeOption WHERE (TDate = '"+day+"') AND (product_hammer = 'TXW0P') AND (Real_CurPrice<>0) ORDER BY TimeIndex"  #Future_CurPrice
    #print dbsql
    r, rcnt = opdbcmd.QueryDB(dbsql)
    rr=r.GetRows(rcnt)  
    if rcnt==1:
        FOpen=int(rr[0][0])
        OPInPrice=int(round(float(FOpen)/50,0)*50)
        
    print "日期",day,"現貨開盤:",FOpen," 價平CP:",OPInPrice
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
    #         0         1       2        3            4             5             6              7             8               9         10         11
    field="TimeIndex,Contract,Sprice,C_CurPrice,C_TrustBuyCnt,C_TrustSellCnt,C_TrustBuyVol,C_TrustSellVol,C_TotalBuyCnt,C_TotalSellCnt,C_Volume,Real_CurPrice"    
    dbsql=u"SELECT "+field+" FROM RealTimeOption WHERE (TDate = '"+day+"') AND (Sprice = "+str(sprice)+") AND (product_hammer = 'TXW0"+cp+"') ORDER BY TimeIndex"
    #print dbsql    
    r, rcnt = opdbcmd.QueryDB(dbsql)
    rr=r.GetRows(rcnt) 
    
    Contract=rr[1][0]
    SPrice=rr[2][0]
    Price=rr[3]
    Vol=rr[10]
    #################  主力  #################    
    MainPower=GetMainPower(np.array(rr[8]),np.array(rr[9]),np.array(rr[10]))
    #print MainPower
    #################  散戶  #################
    after_bcnt=np.array(rr[8])
    after_scnt=np.array(rr[9])
    BadPower=seq_intg(seq_diff(after_bcnt-after_scnt))
    TSEA=np.array(rr[11])
    #print BadPower
    return Contract,SPrice,MainPower,BadPower,Price,Vol,TSEA



try:
    opdbstr = self.connstr
    datecount = td.DateCount
except:
    opdb = DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="OPHis")       #127.0.0.2  192.168.1103
    

today=time.strftime('%y/%m/%d')
print today

def Run(day):
    FP,INP=GetOPPrice(opdb,day)
    TotalProfit=0

    Contract,SPrice,MainPowerC150,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"C",INP+150)
    Contract,SPrice,MainPowerC100,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"C",INP+100)
    Contract,SPrice,MainPowerC050,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"C",INP+50)
    Contract,SPrice,MainPowerC000,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"C",INP)
    Contract,SPrice,MainPowerCN05,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"C",INP-50)
    Contract,SPrice,MainPowerCN10,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"C",INP-100)
    
    Contract,SPrice,MainPowerPP10,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"P",INP+100)
    Contract,SPrice,MainPowerPP05,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"P",INP+50)
    Contract,SPrice,MainPowerP000,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"P",INP) 
    Contract,SPrice,MainPowerP050,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"P",INP-50)
    Contract,SPrice,MainPowerP100,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"P",INP-100)
    Contract,SPrice,MainPowerP150,BadPower,Price,Vol,TSEA=GetOPPower(opdb,day,"P",INP-150)

    C1=np.zeros(len(TSEA))
    C2=np.zeros(len(TSEA))
    C3=np.zeros(len(TSEA))
    C4=np.zeros(len(TSEA))
    C5=np.zeros(len(TSEA))

    P1=np.zeros(len(TSEA))
    P2=np.zeros(len(TSEA))
    P3=np.zeros(len(TSEA))
    P4=np.zeros(len(TSEA))
    P5=np.zeros(len(TSEA))
    
    for i in range(1,len(TSEA)):   
        if MainPowerC100[i]>0.1: C1[i]=10
        elif MainPowerC100[i]<-0.1: C1[i]=-10
        else: C1[i]=C1[i-1]
        if MainPowerC050[i]>0.1: C2[i]=10
        elif MainPowerC050[i]<-0.1: C2[i]=-10
        else: C2[i]=C2[i-1]
        if MainPowerC000[i]>0.1: C3[i]=10 
        elif MainPowerC000[i]<-0.1: C3[i]=-10
        else: C3[i]=C3[i-1]        
        if MainPowerCN05[i]>0.1: C4[i]=10 
        elif MainPowerCN05[i]<-0.1: C4[i]=-10
        else: C4[i]=C4[i-1]        
        if MainPowerCN10[i]>0.1: C5[i]=10 
        elif MainPowerCN10[i]<-0.1: C5[i]=-10
        else: C5[i]=C5[i-1]        
        
        if MainPowerPP10[i]>0.1: P1[i]=10
        elif MainPowerPP10[i]<-0.1: P1[i]=-10
        else: P1[i]=P1[i-1] 
        if MainPowerPP05[i]>0.1: P2[i]=10 
        elif MainPowerPP05[i]<-0.1: P2[i]=-10
        else: P2[i]=P2[i-1] 
        if MainPowerP000[i]>0.1: P3[i]=10 
        elif MainPowerP000[i]<-0.1: P3[i]=-10
        else: P3[i]=P3[i-1] 
        if MainPowerP050[i]>0.1: P4[i]=10 
        elif MainPowerP050[i]<-0.1: P4[i]=-10
        else: P4[i]=P4[i-1] 
        if MainPowerP100[i]>0.1: P5[i]=10 
        elif MainPowerP100[i]<-0.1: P5[i]=-10
        else: P5[i]=P5[i-1] 
        if TSEA[i-1]==0: TSEA[i-1]=TSEA[i]

    plt.plot(C1+INP+100);plt.plot(C2+INP+50);plt.plot(C3+INP);#plt.plot(C4+INP-50);plt.plot(C5+INP-100)
    plt.plot(TSEA)
    plt.show()
    #plt.plot(P1+INP+100);plt.plot(P2+INP+50);
    plt.plot(P3+INP);plt.plot(P4+INP-50);plt.plot(P5+INP-100)
    plt.plot(TSEA)
    plt.show()

#Run("16/03/31")
Run("16/04/08")

'''        
    plt.subplot(521)
    plt.plot(C1);    plt.plot(-11);plt.plot(11)
    plt.subplot(522)
    plt.plot(P1);    plt.plot(-11);plt.plot(11)
    plt.subplot(523)
    plt.plot(C2);    plt.plot(-11);plt.plot(11)
    plt.subplot(524)
    plt.plot(P2);    plt.plot(-11);plt.plot(11)
    plt.subplot(525)
    plt.plot(C3);    plt.plot(-11);plt.plot(11)
    plt.subplot(526)
    plt.plot(P3);    plt.plot(-11);plt.plot(11)
    plt.subplot(527)
    plt.plot(C4);    plt.plot(-11);plt.plot(11)
    plt.subplot(528)
    plt.plot(P4);    plt.plot(-11);plt.plot(11)
    plt.subplot(529)
    plt.plot(C5);    plt.plot(-11);plt.plot(11)
    plt.subplot(5,2,10)
    plt.plot(P5);    plt.plot(-11);plt.plot(11)
    plt.show()
    plt.plot(TSEA)
'''

'''
####################   以下為實際上線    ###################
try:
    profit=Run(today)
except:
    profit=Run("16/04/01")
    
print "============================"
print "所有總績效：",profit


'''
'''
####################   以下為近日回測    ###################
profit=0
profit+=Run('16/03/25')
profit+=Run('16/03/28')
profit+=Run('16/03/29')
profit+=Run('16/03/30')
profit+=Run('16/03/31')
profit+=Run('16/04/01')
profit+=Run('16/04/06')
profit+=Run('16/04/07')
profit+=Run('16/04/08')
print "============================"
print "所有總績效：",profit
#'''



'''

def WriteSignalToDB(dbc,dTable,dDate,dTime,dStrategy,dIndex,dPrice,dUnit,dWinPoint,dSprice,dContract): 
    OrderContract="%s%05d%s" % (dContract[0:3],dSprice,dContract[3:5])
    dContract=OrderContract
    DBC=Query(dbc.conn)    
    SQL="Select * from %s Where TDATE='%s' and TIMEINDEX=%d and StrategyIndex='%s' and Option_Sprice=%d and Option_Contract='%s' " %(dTable,dDate,dIndex,dStrategy,dSprice,dContract)
    #print SQL
    
    r, rcnt = DBC.QueryDB(SQL)
    if rcnt==0:
        SQL="Insert into %s(TDATE,TDATETIME,TIMEINDEX,Option_CurPrice,NowUnit,WinPoint,SignalTime,StrategyIndex,Option_Sprice,Option_Contract) Values('%s','%s',%d,%f,%d,%d,'%s','%s',%d,'%s')" %(dTable,dDate,dTime,dIndex,dPrice,dUnit,dWinPoint,dTime,dStrategy,dSprice,dContract)
        #print SQL        
        DBC.ExecDB(SQL)




# MainPower[i-1]<0 and and BadPower[i-1]>0      
def RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,CP):
    tradecnt=0
    unit=0
    Profit=0
    for i in range(len(MainPower)):
        if i<5:
            continue
        #if MainPower[i-1]>0 and BadPower[i-1]>10 and unit==0 and tradecnt==0 and i>=15 and i<100 : #and Price[i-1]>Price[10]+5:
        if MainPower[i-1]<-0.2 and unit==0 and tradecnt==0 and i>=5 and i<100 :         
            unit=-1
            tradecnt+=1
            Profit=Price[i]
            print "Sell ",str(SPrice),CP," in ",Price[i] , "at " , i
            WriteSignalToDB(opdb,"OptionSignal",day,time.strftime("%H:%M"),"s1",i,Price[i],-1,0,SPrice,Contract)
        if MainPower[i-1]>0.2 and unit==-1:
            Profit=unit*(Price[i]-Profit)-3             
            unit=0
            print "Exit ",str(SPrice),CP," in ",Price[i] , "at " , i           
            WriteSignalToDB(opdb,"OptionSignal",day,time.strftime("%H:%M"),"s1",i,Price[i],0,Profit,SPrice,Contract)
        if unit==-1 and i>290:
            Profit=unit*(Price[i]-Profit)-3            
            unit=0
            print "Exit ",str(SPrice),CP," in ",Price[i] , "at " , i
            WriteSignalToDB(opdb,"OptionSignal",day,time.strftime("%H:%M"),"s1",i,Price[i],0,Profit,SPrice,Contract)
    return Profit



def Run(day):
    FP,INP=GetOPPrice(opdb,day)
    TotalProfit=0

    Contract,SPrice,MainPower,BadPower,Price,Vol=GetOPPower(opdb,day,"C",INP+50)
    TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C")

    Contract,SPrice,MainPower,BadPower,Price,Vol=GetOPPower(opdb,day,"C",INP)
    TotalProfit+=RunOPStrategy(day,Contract,INP,MainPower,BadPower,Price,Vol,"C")
    
    Contract,SPrice,MainPower,BadPower,Price,Vol=GetOPPower(opdb,day,"C",INP-50)
    TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"C")

    
    #遇到下跌容易爆噴，不考慮
    #Contract,SPrice,MainPower,BadPower,Price,Vol=GetOPPower(opdb,day,"P",INP-50)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P")

    #遇到下跌容易爆噴，不考慮
    Contract,SPrice,MainPower,BadPower,Price,Vol=GetOPPower(opdb,day,"P",INP)
    TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P")
    
    #Contract,SPrice,MainPower,BadPower,Price,Vol=GetOPPower(opdb,day,"P",INP+50)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P")    
    
    #Contract,SPrice,MainPower,BadPower,Price,Vol=GetOPPower(opdb,day,"P",INP+100)
    #TotalProfit+=RunOPStrategy(day,Contract,SPrice,MainPower,BadPower,Price,Vol,"P")
    
    
    #plt.plot(MainPower)
    print "今日總績效:",TotalProfit
    return TotalProfit

'''



