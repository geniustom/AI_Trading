# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 45
    if i==baseT:ind.GetIndicatorByType(I,"小台贏家30")
    if i< (baseT) : return
    aa=I.get("小台純贏家作為30")[i-1]
    amax=I.get("小台純贏家作為30高通道")[i-1]
    amin=I.get("小台純贏家作為30低通道")[i-1]
    
    if aa<amin : self.EnterShort(PRICE)
    if aa>amax : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[mc03]小台純贏家作為30通道策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())