# coding=UTF-8
import imp
import lib.dblib as lb;             imp.reload(lb);
import lib.indicator as indl;       imp.reload(indl);

class strategy:
    def __init__(self,dbconn,Indicator,StrategyID,StartTick=5,MaxTrader=6,MaxWin=9999,MaxLost=9999,Name="",Table="Future_Signal_Total",ShowSignal=0,DBSignal=0):        
        self.DB=dbconn
        self.Table=Table
        self.DBSignal=DBSignal
        self.Indi=Indicator
        self.StrategyID=StrategyID
        self.StartTick=StartTick
        self.Count=Indicator.len
        self.MaxTrader=MaxTrader
        self.MaxWin=MaxWin
        self.MaxLost=MaxLost
        self.ShowSignal=ShowSignal
        self.timelist=[]
        self.pricelist=Indicator.get("大台指數")
        self.timelist=Indicator.get("TIME")
        self.Name=Name

        self.NowUnit=0                              #-1 空單 0空手 1多單
        self.NowUnitList=[]                         #記錄每個時間點部位的list
        self.PreUnit=0                              #當DonActive=1時，以此判斷是否需重新下單
        self.DonActive=0                            #不啟動策略 0:啟動 1:不啟動
        self.NowTrader=0                            #目前進出次數
        #self.Couse=0                               # 3= 多多多 -3=空空空 +1=2多1空  -1=2空一多
        self.LastEnterPrice=0                       #上一比單的進場價
        self.EnterPrice=0                           #紀錄主力進場價
        self.StopPoint=0                            #紀錄停損點位
        self.ProfitPoint=0
        self.IgroneRound=0                          #是否只下翻單(第二單)
        
        self.RunToday=1                            #今天是否下單 (若要全面關閉濾網，初值改為1，否則是-1)
        
        self.ProfitList=[]
        self.Variable=[]

    def getMaxIndex(self,D,rang):
        maxIndex=0
        maxValue=-999999
        for i in range(1,rang):
            if D[i]>maxValue:
                maxIndex=i
                maxValue=D[i]
        return maxIndex
        
    def EnterLong(self,price):
        #if self.PreUnit!=1: self.DonActive=0
        #self.PreUnit=1
        if (self.NowUnit != 1) and (self.NowTrader<self.MaxTrader) and (self.DonActive==0): #檢查部位是否改變
            if self.NowTrader>0: self.GetProfitPoint()
            self.NowUnit=1
            self.LastEnterPrice=self.EnterPrice
            self.EnterPrice=price
            self.NowTrader+=1
            if self.NowTrader == self.MaxTrader: self.NowUnit=0     #若超過最大次數時強制平倉
            if self.ShowSignal==1: print ("time:%s , price:%d , unit:%d" %(self.timelist[self.index],price,self.NowUnit))
       
    def EnterShort(self,price):
        #if self.PreUnit!=-1: self.DonActive=0
        #self.PreUnit=-1
        if (self.NowUnit != -1) and (self.NowTrader<self.MaxTrader) and (self.DonActive==0): #檢查部位是否改變
            if self.NowTrader>0: self.GetProfitPoint()
            self.NowUnit=-1
            self.LastEnterPrice=self.EnterPrice
            self.EnterPrice=price
            self.NowTrader+=1
            if self.NowTrader == self.MaxTrader: self.NowUnit=0     #若超過最大次數時強制平倉
            if self.ShowSignal==1: print ("time:%s , price:%d , unit:%d" %(self.timelist[self.index],price,self.NowUnit))
    
    def IgroneFirstLong(self,price):
        if self.IgroneRound==0:
            self.IgroneRound=-1
        elif self.IgroneRound==1:
            self.EnterShort(price)
            
    def IgroneFirstShort(self,price):
        if self.IgroneRound==0:
            self.IgroneRound=1
        elif self.IgroneRound==-1:        
            self.EnterLong(price)

    def ExitAll(self,price):
        #if (self.NowUnit != 0) and (self.NowTrader<self.MaxTrader) and (self.DonActive==0): #檢查部位是否改變
        if (self.NowUnit != 0): #檢查部位是否改變
            if self.NowTrader>0: self.GetProfitPoint()
            self.DonActive=1
            self.NowUnit=0      
            self.LastEnterPrice=self.EnterPrice
            self.EnterPrice=price
            if self.ShowSignal==1: print ("time:%s , price:%d , unit:%d" %(self.timelist[self.index],price,self.NowUnit))
                
    def GetProfitPoint(self):
        Profit=(self.pricelist[self.index]-self.EnterPrice)*self.NowUnit
        #print "%d %d" %(self.pricelist[self.index],self.EnterPrice)
        self.ProfitList.append(Profit)
        self.ProfitPoint+=Profit
        
    def CheckStopWin(self,price):
        if ((self.pricelist[self.index-1]-self.EnterPrice)*self.NowUnitList[self.index-1] > self.MaxWin):
            if self.NowTrader>0: self.GetProfitPoint() 
            self.NowUnit=0
            self.LastEnterPrice=self.EnterPrice
            self.EnterPrice=price
            self.DonActive=1        #停利或停損時，只有在原部位改變食材會有新訊號
            self.NowTrader+=1 
            #print "%s: %d -> %d stop-win" %(self.day,self.pricelist[self.index],self.EnterPrice)
            if self.ShowSignal==1: print ("time:%s , price:%d , unit:%d StopWin" %(self.timelist[self.index],self.pricelist[self.index],self.NowUnit))

    def CheckStopLose(self,price):        
        if ((self.EnterPrice-self.pricelist[self.index-1])*self.NowUnitList[self.index-1] > self.MaxLost):
            if self.NowTrader>0: self.GetProfitPoint()  
            self.NowUnit=0
            self.LastEnterPrice=self.EnterPrice
            self.EnterPrice=price
            self.DonActive=1        #停利或停損時，只有在原部位改變食材會有新訊號
            self.NowTrader+=1 
            #print "%s: %d -> %d stop-lose" %(self.day,self.pricelist[self.index],self.EnterPrice)
            if self.ShowSignal==1: print ("time:%s , price:%d , unit:%d StopLose" %(self.timelist[self.index],self.pricelist[self.index],self.NowUnit))
        
    def CheckDailyExitAll(self,t,p):
        if t =="13:40": self.ExitAll(p)
        if t =="13:41": self.ExitAll(p)
        if t =="13:42": self.ExitAll(p)
        if t =="13:43": self.ExitAll(p)
        if t =="13:44": self.ExitAll(p)
        if t =="13:45": self.ExitAll(p)
        
    def Run(self,method,day):
        self.index=0
        self.day=day
        indl.GetSpecialIndicator(self.Indi) #載入特別指標 (因為指標會改寫所以每次要重讀)  
        
        while self.index < self.Indi.len :
            if self.index >= self.StartTick:
                self.NowUnit=self.NowUnitList[self.index-1] #預設危值上衣跟k棒的部位
                price= self.pricelist[self.index]
                method(self,price,self.index,self.Indi)
                if self.MaxLost!=9999:  self.CheckStopLose(price)
                if self.MaxWin!=9999:   self.CheckStopWin(price)

                if self.NowUnit!=self.NowUnitList[self.index-1]:
                    if self.LastEnterPrice==0:
                        self.WinPoint=0
                    else:
                        self.WinPoint=(price-self.LastEnterPrice)*(self.NowUnitList[self.index-1]-self.NowUnit)
                    #有設定db產生訊號
                    if self.DBSignal==1:                    
                        lb.WriteSignalToDB(self.DB,self.Table,self.day,self.timelist[self.index],self.StrategyID,self.index,price,self.NowUnit,self.WinPoint)
                
                self.NowUnitList.append(self.NowUnit)                
            else:
                self.NowUnitList.append(0)
            self.index+=1

        for i in range(self.index,self.Count-1,1):
            self.NowUnitList.append(0)
        
            

        
        


