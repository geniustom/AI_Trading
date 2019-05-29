# coding=UTF-8

import datalib as dl
import indicator as il
import strategy as sl

import numpy as np
import pylab as pl
import scipy as sc
import matplotlib.pyplot as plt




def strategy1(self,PRICE,i,I):
    if I.get("大台散戶")[i]>0: self.EnterShort(PRICE)
    if I.get("大台散戶")[i]<0: self.EnterLong(PRICE)
    if I.get("TIME")[i]=="13:43": self.ExitAll(PRICE)

'''
host="localhost"
uid="sa"
pwd="geniustom"
dbconn=dl.DB("Provider=SQLNCLI.1;Persist Security Info=True;Data Source="+host+";Initial Catalog=FutureHis;User ID="+uid+";Password="+pwd+";")
Qy=dl.Query(dbconn.dbconn)
r, rcnt = Qy.QueryDB("SELECT TDATE FROM (SELECT DISTINCT TDATE FROM RealTimeFuture) as NEW ORDER BY TDATE")
'''



tt=dl.timer()
AT=dl.AutoTrade("localhost","sa","geniustom")
print tt.spendtime("DB Conn Time")
i=1
#for i in range(0,AT.DateCount):
tt=dl.timer()
AT.DayTrade(AT.DateList[i])
s1=sl.strategy(AT.indi,StartTick=15,MaxTrader=10,Name="散戶主力策略")
s1.Run(strategy1)
print u"交易日期：%s 績效：%s 耗時：%s"%(AT.DateList[i],s1.ProfitList,tt.spendtime("DB Query Time"))

i=2
tt=dl.timer()
indi=AT.DayTrade(AT.DateList[i])
s1=sl.strategy(indi,StartTick=15,MaxTrader=10,Name="散戶主力策略")
s1.Run(strategy1)
print u"交易日期：%s 績效：%s 耗時：%s"%(AT.DateList[i],s1.ProfitList,tt.spendtime("DB Query Time"))

i=3
tt=dl.timer()
indi=AT.DayTrade(AT.DateList[i])
s1=sl.strategy(indi,StartTick=15,MaxTrader=10,Name="散戶主力策略")
s1.Run(strategy1)
print u"交易日期：%s 績效：%s 耗時：%s"%(AT.DateList[i],s1.ProfitList,tt.spendtime("DB Query Time"))









'''
subplot(2, 1, 1)
plt.plot(indi.get("大台散戶"),"r")
plt.plot(indi.get("小台散戶"),"g")
plt.plot(indi.get("大台黑手"),"b")
plt.plot(indi.get("小台黑手"),"y")
subplot(2, 1, 2)
plt.plot(indi.get("大台指數"),"B")
#row=rs.GetRows(cnt) 

#conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=localhost;DATABASE=Future_His;UID=sa;PWD=geniustom')
#CONN= "Provider=SQLOLEDB.1;Persist Security Info=True;Data Source=localhost;Initial Catalog=Future_His;User ID=sa;Password=geniustom;"
CONN= "Provider=SQLNCLI.1;Persist Security Info=True;Data Source=localhost;Initial Catalog=FutureHis;User ID=sa;Password=geniustom;"
FIELD="Future_CurPrice,TDATETIME,Future_Volume,Future_TotalBuyVol, Future_TotalSellVol,FutureWant_TrustBuyVol,FutureWant_TrustSellVol,Future_Volume,FutureWant_TrustBuyCnt,FutureWant_TrustSellCnt,FutureWant_TotalBuyCnt,FutureWant_TotalSellCnt,FutureWant_TF_TotalBuyCnt,FutureWant_TF_TotalSellCnt,FutureWant_TE_TotalBuyCnt,FutureWant_TE_TotalSellCnt,RealWant_Uppers,RealWant_Downs,RealWant_UpperLimits,RealWant_DownLimits,RealWant_Steadys,FutureM_Volume,FutureM_TotalBuyVol, FutureM_TotalSellVol,FutureWantM_TrustBuyVol,FutureWantM_TrustSellVol,FutureM_Volume,FutureWantM_TrustBuyCnt,FutureWantM_TrustSellCnt,FutureWantM_TotalBuyCnt,FutureWantM_TotalSellCnt"
DATE="14/08/04"
SQL = "Select " + FIELD + " from RealTimeFuture where TDATE='" + DATE + "'"


tt=dl.timer()
dt=dl.DB(CONN)
indi=il.indicatorGroup()
print tt.spendtime("DB Conn Time")
tt=dl.timer()
indi=dt.QueryDBtoIndicators(SQL)
indi.GetBaseIndicator()
s1=sl.strategy(indi,StartTick=15,MaxTrader=20,Name="散戶主力策略")
s1.Run(strategy1)
print tt.spendtime("DB Query Time")


plt.subplot(2, 1, 1)
plt.plot(s1.NowUnitList)
#plt.plot(indi.get("大台散戶"))
plt.subplot(2, 1, 2)
plt.plot(indi.get("大台指數"),"B")

print s1.ProfitList
print s1.ProfitPoint



print cnt
field_names = [field.Name for field in rs.Fields]
fields = []
for field_name in field_names:
    print field_name
    #fields.append(Field(rs, field_name))   





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




#h = [(i[0],int) for i in cmd.description]

# You can also use 'object' for your type
# h = [(i[0],object) for i in c.description]

#a = asarray(list(s),dtype=h)



Left = {}
for it in rs.fetchall():
    if it[0] in Left:
       Left[it[0]].append(it[1])
    else:
       Left[it[0]] = [it[1]]

#print seq_count(d)
'''

