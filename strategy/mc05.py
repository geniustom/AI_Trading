# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 15
    if i==baseT:ind.GetIndicatorByType(I,"小台輸家00")
    if i< (baseT) : return
    aa=I.get("小台純輸家作為00")[i-1]
    amax=I.get("小台純輸家作為00高通道")[i-1]
    amin=I.get("小台純輸家作為00低通道")[i-1]
    
    if aa<amin : self.EnterLong(PRICE)
    if aa>amax : self.EnterShort(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[mc05]小台純輸家作為00通道策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())