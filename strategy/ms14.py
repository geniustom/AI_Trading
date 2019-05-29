# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 30
    if i==baseT:ind.GetIndicatorByType(I,"大台輸家15")
    if i< (baseT) : return
    base1= I.get("大台純輸家作為15")[baseT]
    
    if I.get("大台純輸家作為15")[i-1]-base1>10 : self.EnterShort(PRICE)
    if I.get("大台純輸家作為15")[i-1]-base1<-10 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ms14]大台純輸家作為15策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())