# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
###############################################################################   
def filter1(self,I):    #2代濾網  IF(OR(AND((AM2>10.5),(AM2<16.5)),AND((AU2>6),(AU2<8))),0,AV2)
    import lib.filter as fl
    #if self.RunToday==1:self.RunToday=-1
    if self.RunToday==-1:
        self.RunToday=1
        H=fl.getOpenVolABS(I.get("大台成交量"),15)
        AO=fl.getOpenVolABS(I.get("金期黑手"),15)
        
        if (AO>395) and (H>53000) :
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I):
    baseT= 15
    if filter1(self,I)==0: return
    if i==baseT:
        ind.GetIndicatorByType(I,"小台未純化大單作為")
        ind.GetIndicatorByType(I,"小台未純化大單企圖")
    if i< (baseT) : return
    aa=I.get("小台未純化大單企圖")[i-1]
    amax=I.get("小台未純化大單企圖高通道")[i-1]
    amin=I.get("小台未純化大單企圖低通道")[i-1]
    
    ma=I.get("小台未純化大單作為")[i-1]
    mmax=I.get("小台未純化大單作為高通道")[i-1]
    mmin=I.get("小台未純化大單作為低通道")[i-1]
    
    if aa<amin and ma<mmin : self.EnterShort(PRICE)
    if aa>amax and ma>mmax : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[p03]小台未純化大單企圖作為通道策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())
