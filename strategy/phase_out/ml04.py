# coding=UTF-8
import lib.indicator as ind; reload(ind);  
############################################################################### 
def s1(self,PRICE,i,I):
    if i==15:ind.GetIndicatorByType(I,"大台輸家")
    if I.get("大台純輸家作為")[i-1]>10 : self.EnterShort(PRICE)
    if I.get("大台純輸家作為")[i-1]<-10 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ml04]大台純輸家作為策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())