# coding=UTF-8
import lib.indicator as ind; reload(ind);  
############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 30
    if i==30:ind.GetIndicatorByType(I,"小台輸家30")
    if i< (baseT+15) : return
    base1= I.get("小台純輸家作為30")[baseT]
    
    if I.get("小台純輸家作為30")[i-1]-base1>3 : self.EnterShort(PRICE)
    if I.get("小台純輸家作為30")[i-1]-base1<-3 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ml10]小台純輸家作為30策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())