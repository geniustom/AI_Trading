# coding=UTF-8

import datalib as lib
import indicator as indl
import numpy as np
import pylab as pl
import scipy as sc



class strategy:
    def __init__(self,Indicator,StartTick=5,MaxTrader=6,MaxWin=9999,MaxLost=9999,Name=""): 
        self.Indi=Indicator
        self.StartTick=StartTick
        self.Count=Indicator.len
        self.MaxTrader=MaxTrader
        self.MaxWin=MaxWin
        self.MaxLost=MaxLost
        self.timelist=[]
        self.pricelist=Indicator.get("大台指數")
        self.timelist=Indicator.get("TIME")
        self.Name=Name

        self.NowUnit=0                              #-1 空單 0空手 1多單
        self.NowUnitList=[]                         #記錄每個時間點部位的list
        self.PreUnit=0                              #當DonActive=1時，以此判斷是否需重新下單
        self.DonActive=0                            #不啟動策略 0:啟動 1:不啟動
        self.NowTrader=0                            #目前進出次數
        #self.Couse=0                                # 3= 多多多 -3=空空空 +1=2多1空  -1=2空一多
        self.EnterPrice=0                           #紀錄主力進場價
        self.StopPoint=0                            #紀錄停損點位
        self.ProfitPoint=0
        self.ProfitList=[]

        
    def EnterLong(self,price):
        if self.PreUnit!=1: self.DonActive=0
        self.PreUnit=1
        if (self.NowUnit != 1) and (self.NowTrader<self.MaxTrader) and (self.DonActive==0): #檢查部位是否改變
            if self.NowTrader>0: self.GetProfitPoint()
            self.NowUnit=1
            self.EnterPrice=price
            self.NowTrader+=1
            if self.NowTrader == self.MaxTrader: self.NowUnit=0     #若超過最大次數時強制平倉
        
    def EnterShort(self,price):
        if self.PreUnit!=-1: self.DonActive=0
        self.PreUnit=-1
        if (self.NowUnit != -1) and (self.NowTrader<self.MaxTrader) and (self.DonActive==0): #檢查部位是否改變
            if self.NowTrader>0: self.GetProfitPoint()
            self.NowUnit=-1
            self.EnterPrice=price
            self.NowTrader+=1
            if self.NowTrader == self.MaxTrader: self.NowUnit=0     #若超過最大次數時強制平倉

    def ExitAll(self,price):
        if (self.NowUnit != 0) and (self.NowTrader<self.MaxTrader) and (self.DonActive==0): #檢查部位是否改變
            if self.NowTrader>0: self.GetProfitPoint()
            self.DonActive=1
            self.NowUnit=0               
            
    def GetProfitPoint(self):
        Profit=(self.pricelist[self.index]-self.EnterPrice)*self.NowUnit
        self.ProfitList.append(Profit)
        self.ProfitPoint+=Profit
        
    def CheckStopWin(self):
        if ((self.pricelist[self.index]-self.EnterPrice)*self.NowUnit > self.MaxWin):
            self.NowUnit=0
            self.DonActive=1        #停利或停損時，只有在原部位改變食材會有新訊號
            self.NowTrader+=1            

    def CheckStopLose(self):        
        if ((self.EnterPrice-self.pricelist[self.index])*self.NowUnit > self.MaxLost):
            self.NowUnit=0
            self.DonActive=1        #停利或停損時，只有在原部位改變食材會有新訊號
            self.NowTrader+=1     
        
    def Run(self,method):
        self.index=0
        while self.index < self.Indi.len :
            if self.index >= self.StartTick:
                self.NowUnit=self.NowUnitList[self.index-1] #預設危值上衣跟k棒的部位
                price= self.pricelist[self.index]
                method(self,price,self.index,self.Indi)
                self.CheckStopLose()
                self.CheckStopWin()
                self.NowUnitList.append(self.NowUnit)
            else:
                self.NowUnitList.append(0)
            self.index+=1

        for i in range(self.index,self.Count-1,1):
            self.NowUnitList.append(0)
        

