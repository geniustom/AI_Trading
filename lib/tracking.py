# coding=UTF-8
import imp
import lib.dblib as lb;             imp.reload(lb);
import lib.indicator as indl;       imp.reload(indl);
import lib.strategy_lib as sl;      imp.reload(sl);

class tracking:
    def __init__(self,dbconn,TData=None):
        self.db=dbconn
        tt=lb.timer()
        if TData==None:
            self.TData=lb.TradeData(self.db)
        else:
            self.TData=TData
        #print tt.spendtime("DB Get Datelist")

            
    def BackTrackingbyMem(self,s,strategyID,pStartTick=15,pMaxTrader=5,pName="",pMaxWin=9999,pMaxLost=9999,pCost=3,pDays=0):
        import datetime
        self.datelist=[]                #計算績效表用的日期
        self.profithist=[]              #單筆損益扣除成本
        self.profitcurve=[]             #累計損益扣除成本
        self.profithist_nocost=[]       #單筆損益不含成本
        self.profitcurve_nocost=[]      #累計損益不含成本        
        
        if self.TData.AllData==None:
            tt=lb.timer()
            self.TData.FetchAllData()
            print (tt.spendtime("DB Get All Data"))
        
        ttt=lb.timer()
        #回測天數 0代表全部
        DaysStart=0
        if pDays!=0: DaysStart=self.TData.DateCount-pDays
        #開始回測天數 
        for i in range(0,self.TData.DateCount-DaysStart):
            self.indi=self.TData.FetchDateByMem(self.TData.DateList[i+DaysStart])
            self.strategy=sl.strategy(self.db,self.indi,StrategyID=strategyID,StartTick=pStartTick,MaxTrader=pMaxTrader,Name=pName,MaxWin=pMaxWin,MaxLost=pMaxLost,DBSignal=0)
            day=self.TData.DateList[i+DaysStart]    
            
            self.strategy.Run(s,day)
            
            cost=len(self.strategy.ProfitList)*pCost
            todayprofit=self.strategy.ProfitPoint-cost
            todayprofit_nocost=self.strategy.ProfitPoint
            if i==0:
                self.profitcurve.append(todayprofit)
                self.profitcurve_nocost.append(todayprofit_nocost)
            else:
                self.profitcurve.append(todayprofit+self.profitcurve[i-1])
                self.profitcurve_nocost.append(todayprofit_nocost+self.profitcurve_nocost[i-1])
            self.profithist.append(todayprofit)
            self.profithist_nocost.append(todayprofit_nocost)
            d=datetime.datetime.strptime('20'+self.TData.DateList[i+DaysStart],'%Y/%m/%d')
            self.datelist.append(d)
            
            
            #print "Run:" +str(step1) + " Profit:"+str(step2)
            #print (u"交易日期：%s 績效：%s 耗時：%s" %(self.datelist[i],todayprofit,tt.spendtime("DB Query Time")))
        print (ttt.spendtime("Back Tracking Total Time"))  



    def DayTrade(self,day,s,strategyID,pStartTick=15,pMaxTrader=5,pName="",pMaxWin=9999,pMaxLost=9999,pCost=3,pShowSignal=0):
        if pShowSignal==1:
            print ("\n%s--%s" %(day,pName))
        self.indi=self.TData.FetchDateByDB(day)
        self.strategy=sl.strategy(self.db,self.indi,StrategyID=strategyID,StartTick=pStartTick,MaxTrader=pMaxTrader,Name=pName,MaxWin=pMaxWin,MaxLost=pMaxLost,ShowSignal=pShowSignal,DBSignal=1)
        self.strategy.Run(s,day)
        
        profit=self.strategy.ProfitPoint
        cost=len(self.strategy.ProfitList)*pCost
        netporfit=self.strategy.ProfitPoint-cost
        print ("%d - %d = %d" %(profit,cost,netporfit))
        return netporfit
