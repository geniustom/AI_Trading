# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純主力買作為")-I.get("小台純主力賣作為"),15,start=30)
        f2=fl.getOpenVolABS(I.get("小台散戶"),15,start=30)
        if (f1>0.7 and f1<4.2) or  (f2>2300 and f2 <5600):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("金期未純化主力企圖")[baseT]
    base2= I.get("電期未純化主力企圖")[baseT]        
    
    mf=I.get("金期未純化主力企圖")[i-1]-base1
    me=I.get("電期未純化主力企圖")[i-1]-base2
    
    if mf+me<-3 : self.EnterShort(PRICE)
    if mf+me>3: self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s34_1]金電期貨未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())