# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
###############################################################################   
def filter1(self,I):    #2代濾網  IF(OR(AND((AM2>10.5),(AM2<16.5)),AND((AU2>6),(AU2<8))),0,AV2)
    import lib.filter as fl
    #if self.RunToday==1:self.RunToday=-1
    if self.RunToday==-1:
        self.RunToday=1
        ind.GetIndicatorByType(I,"大台未純化大單企圖")
        ind.GetIndicatorByType(I,"大台未純化大單作為")
        II=fl.getOpenVolABS(I.get("大台未純化大單企圖"),15)
        M=fl.getOpenVolABS(I.get("大台未純化大單作為"),15)

        if (M>8.8 and M<11) or (II<10) :
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I):
    baseT= 45
    if filter1(self,I)==0: return
    if i< (baseT) : return
    if i==baseT:ind.GetIndicatorByType(I,"小台未純化大單作為")
    aa=I.get("小台未純化大單作為")[i-1]
    amax=I.get("小台未純化大單作為高通道")[i-1]
    amin=I.get("小台未純化大單作為低通道")[i-1]
    
    if aa<amin : self.EnterShort(PRICE)
    if aa>amax : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[p02]小台未純化大單作為通道45策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())

