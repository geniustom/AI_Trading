# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
###############################################################################   
def s1(self,PRICE,i,I):      
    aa=I.get("小台未純化大單企圖")[i-1]
    amax=I.get("小台未純化大單企圖高通道")[i-1]
    amin=I.get("小台未純化大單企圖低通道")[i-1]
    
    if aa<amin : self.EnterShort(PRICE)
    if aa>amax : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[p02]小台未純化大單企圖策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())
