# coding=UTF-8
############################################################################### 
def filter2(self,I):    #一代濾網 (已失效)
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        M=fl.getOpenVolABS(I.get("大台未純化主力作為"),15)
        AR=fl.getOpenVolABS(I.get("金期純主力買企圖")-I.get("金期純主力賣企圖"),15)
        AS=fl.getOpenVolABS(I.get("金期純主力買作為")-I.get("金期純主力賣作為"),15)
        if (AS==0 and AR<6.9) or (M>6.8 and M<7.6) :
            self.RunToday=0
    return self.RunToday

def filter1(self,I):    #2代濾網  IF(OR(AND((AM2>10.5),(AM2<16.5)),AND((AU2>6),(AU2<8))),0,AV2)
    import lib.filter as fl
    #if self.RunToday==1:self.RunToday=-1
    if self.RunToday==-1:
        self.RunToday=1
        AM=fl.getOpenVolABS(I.get("金期主力"),15)
        AU=fl.getOpenVolABS(I.get("金期純散戶買作為")-I.get("金期純散戶賣作為"),15)

        if (AM>10.5 and AM<16.5) or (AU>6 and AU<8) :
            self.RunToday=0
    return self.RunToday

###############################################################################    
def s1(self,PRICE,i,I): #1568 1888
    if filter1(self,I)==0:
        return
    if I.get("大台未純化主力企圖")[i-1]<0 and I.get("小台未純化主力企圖")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台未純化主力企圖")[i-1]>0 and I.get("小台未純化主力企圖")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
   
############################################################################### 
import os
STittle=u"[s01]大小台主力企圖策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())