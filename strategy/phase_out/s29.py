# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台成交量"),15)
        f2=fl.getOpenVolABS(I.get("大台散戶"),15)
        if  (f1>62000 and f1 <71000) or (f2>1900 and f2<2650):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    mb=I.get("中市大台未純化主力企圖")[i-1]
    ms=I.get("中市小台未純化主力企圖")[i-1]
        
    #if mb<0 and ms<0 : self.EnterShort(PRICE)
    #if mb>0 and ms>0 : self.EnterLong(PRICE)
    if mb+ms<-2 : self.EnterShort(PRICE)
    if mb+ms>2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s29]中市大台純主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())