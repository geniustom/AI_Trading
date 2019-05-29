# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 60
    if i==baseT:ind.GetIndicatorByType(I,"小台輸家45")
    if i< (baseT) : return
    base1= I.get("小台純輸家作為45")[baseT]
    
    if I.get("小台純輸家作為45")[i-1]-base1>2 : self.EnterShort(PRICE)
    if I.get("小台純輸家作為45")[i-1]-base1<-2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ms08]小台純輸家作為45策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())