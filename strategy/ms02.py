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
        L=fl.getOpenVolABS(I.get("大台未純化大單企圖"),15)
        AM=fl.getOpenVolABS(I.get("金期主力"),15)

        if (L<10.2) or (AM>50) :
            self.RunToday=0
    return self.RunToday
############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 30
    if filter1(self,I)==0: return
    if i< (baseT) : return
    if i==baseT:ind.GetIndicatorByType(I,"小台贏家15")
    base1= I.get("小台純贏家作為15")[baseT]
    
    if I.get("小台純贏家作為15")[i-1]-base1<-1 : self.EnterShort(PRICE)
    if I.get("小台純贏家作為15")[i-1]-base1>1 : self.EnterLong(PRICE)
        
    #if (self.NowUnit<0) and PRICE-I.get("大台低點")[i-1]>35: self.ExitAll(PRICE)
    #if (self.NowUnit>0) and I.get("大台高點")[i-1]-PRICE>35: self.ExitAll(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ms02]小台純贏家作為15策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())