# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        X=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
        AQ=fl.getOpenVolABS(I.get("金期未純化主力作為"),15)

        #IF(OR(AND((AQ2>17),(AQ2<2600)),AND((X2>2.7),(X2<4.5))),0,AV2)
        if (AQ>17 and AQ<2600) or (X>2.7 and X<4.5):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
        return
    if I.get("小台未純化主力企圖")[i-1]<-3 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖")[i-1]>3  : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
 
      
     
############################################################################### 
import os
STittle=u"[s11]純小台主力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())