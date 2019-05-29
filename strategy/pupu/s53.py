# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        P=fl.getOpenVolABS(I.get("小台主力"),15)
        G=fl.getOpenVolABS(I.get("大台成交量"),15)
        if (P>9.5 and P<21) or (G>47000 and G<64000):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    #if filter1(self,I)==0:
    #    return
    if i<45 : return
        
    #self.MaxTrader=3
    #tx=I.get("小台未純化主力企圖")[i-1]
    #mf=I.get("金期未純化主力企圖")[i-1]
    #me=I.get("電期未純化主力企圖")[i-1]
     
    #PNM=(I.get("小台未純化主力買作為價")[i-1]+I.get("小台未純化主力賣作為價")[i-1])/2
    PMb=I.get("小台主力買作為價")[i-1]
    PMs=I.get("小台主力賣作為價")[i-1]

    #bb=I.get(u"小台未純化主力企圖")[i-1]
    #cc=I.get(u"小台未純化主力作為")[i-1]
    
    #if cc<0 and bb-cc<-1 : self.EnterShort(PRICE)
    #if cc>0 and bb-cc>1 : self.EnterLong(PRICE)   

    #if (mf+me)<-2 and (mf+me)/2>tx and tx<-2 : self.EnterShort(PRICE)
    #if (mf+me)>2 and (mf+me)/2<tx and tx>2 : self.EnterLong(PRICE)  
    if PRICE<PMs and abs(PRICE-PMs)<30 : self.EnterShort(PRICE)
    if PRICE>PMb and abs(PRICE-PMb)<30 : self.EnterLong(PRICE)
    if self.NowUnit==-1 and PRICE>PMb : self.ExitAll(PRICE)
    if self.NowUnit==1  and PRICE<PMs : self.ExitAll(PRICE)
    

    #if self.NowUnit==-1 and PRICE>PNM+20 : self.ExitAll(PRICE)
    #if self.NowUnit==1  and PRICE<PNM-20 : self.ExitAll(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)  
############################################################################### 
import os
STittle=u"[s51]小台主力作為價策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())