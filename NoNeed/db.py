# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
import scipy as sc
import matplotlib.pyplot as plt


class timer:
    def __init__(self): 
        import time
        self.t=time.clock()
    def spendtime(self):
        import time
        return (time.clock()-self.t)
        
        
class indicator:
    def __init__(self):
        self.name=""
        self.data=[]
        self.count=0
             
    
class DB:
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
    def QueryDBtoArry(self,SQL_Str):
        r, rcnt= self.QueryDB(SQL_Str)
        rr=r.GetRows(rcnt)        
        self.f = [field.Name for field in r.Fields]
        i=0
        for field_name in self.f:
            ind=indicator()
            ind.name=field_name
            ind.data=np.array(rr[i])
            i+=1
            self.d.append(ind)
    def data(self,dname):
        for i in range(len(self.f)):
            if dname==self.f[i]: return self.d[i].data
    
    def __init__(self,connstr):
        import win32com.client
        self.d=[]
        self.f=[]
        self.count=0
        self.dbconn=win32com.client.Dispatch(r"ADODB.Connection")
        self.dbconn.Open(connstr)
        


    

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
    
def seq_count (x):
    return x.shape


#conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=localhost;DATABASE=Future_His;UID=sa;PWD=geniustom')
#CONN= "Provider=SQLOLEDB.1;Persist Security Info=True;Data Source=localhost;Initial Catalog=Future_His;User ID=sa;Password=geniustom;"
CONN= "Provider=SQLNCLI.1;Persist Security Info=True;Data Source=127.0.0.1;Initial Catalog=FutureHis;User ID=sa;Password=geniustom;"
FIELD="Future_CurPrice,TDATETIME,Future_Volume,Future_TotalBuyVol, Future_TotalSellVol,FutureWant_TrustBuyVol,FutureWant_TrustSellVol,Future_Volume,FutureWant_TrustBuyCnt,FutureWant_TrustSellCnt,'+'FutureWant_TotalBuyCnt,FutureWant_TotalSellCnt,FutureWant_TF_TotalBuyCnt,FutureWant_TF_TotalSellCnt,FutureWant_TE_TotalBuyCnt,FutureWant_TE_TotalSellCnt,RealWant_Uppers,RealWant_Downs,RealWant_UpperLimits,RealWant_DownLimits,RealWant_Steadys,FutureM_Volume,FutureM_TotalBuyVol, FutureM_TotalSellVol,FutureWantM_TrustBuyVol,FutureWantM_TrustSellVol,FutureM_Volume,FutureWantM_TrustBuyCnt,FutureWantM_TrustSellCnt,'+'FutureWantM_TotalBuyCnt,FutureWantM_TotalSellCnt"
SQL = "Select " + FIELD + " from RealTimeFuture where TDATE='14/08/04'"


tt=timer()
dt=DayTrade(CONN)
dt.QueryDBtoArry(SQL)
print tt.spendtime()

plot(dt.data("Future_CurPrice"))
#row=rs.GetRows(cnt)

'''
print cnt
field_names = [field.Name for field in rs.Fields]
fields = []
for field_name in field_names:
    print field_name
    #fields.append(Field(rs, field_name))   
'''




'''
a=np.array([1,2,3,4,5])
b=np.array([3,5,6,3,1])
c=pl.add(a,b)

tt=timer()
d=seq_diff(c)
print tt.spendtime()

tt=timer()
e=seq_intg(d)
print tt.spendtime()

#plt.plot(rs.Fields.Item("TDATETIME").Value)
#plt.plot(a);


while not rs.eof:
        print rs.Fields.Item("TDATETIME").Value
        rs.MoveNext()
'''



#h = [(i[0],int) for i in cmd.description]

# You can also use 'object' for your type
# h = [(i[0],object) for i in c.description]

#a = asarray(list(s),dtype=h)


'''
Left = {}
for it in rs.fetchall():
    if it[0] in Left:
       Left[it[0]].append(it[1])
    else:
       Left[it[0]] = [it[1]]

#print seq_count(d)
'''

