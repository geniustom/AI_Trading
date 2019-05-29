# coding=UTF-8
import lib.indicator as ind; reload(ind);
############################################################################### 
def s1(self,PRICE,i,I):
    if i==15:ind.GetIndicatorByType(I,"電期贏家")
    if I.get("電期純贏家作為")[i-1]<-2 : self.EnterShort(PRICE)
    if I.get("電期純贏家作為")[i-1]>2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ml05]電期純贏家作為策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())