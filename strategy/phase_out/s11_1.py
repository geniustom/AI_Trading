# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        Q=fl.getOpenVolABS(I.get("大台純散戶買作為")-I.get("大台純散戶賣作為"),15,start=30)
        AR=fl.getOpenVolABS(I.get("金期純主力買企圖")-I.get("金期純主力賣企圖"),15,start=30)
        AO=fl.getOpenVolABS(I.get("金期黑手"),15,start=30)

        #IF(OR((Q2<33),(AR2<1),(AO2<180)),0,AV2)
        if (Q<33) or (AR<1) or (AO<180) :
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
        return
        
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("小台未純化主力企圖")[baseT]

    if I.get("小台未純化主力企圖")[i-1]-base1<-3 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖")[i-1]-base1>3  : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
 
      
     
############################################################################### 
import os
STittle=u"[s11_1]純小台主力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())