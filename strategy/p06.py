# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
###############################################################################   
def s1(self,PRICE,i,I):
    baseT= 45
    if i==baseT:ind.GetIndicatorByType(I,"大台散戶")
    if i< (baseT) : return
    aa=I.get("大台散戶")[i-1]
    amax=I.get("大台散戶高通道")[i-1]
    amin=I.get("大台散戶低通道")[i-1]

    if aa<amin : self.EnterLong(PRICE)
    if aa>amax : self.EnterShort(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[p06]大台散戶通道策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())
