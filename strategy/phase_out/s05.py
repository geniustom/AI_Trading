# coding=UTF-8
############################################################################### 
def filter1(self,I):  
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台黑手"),15)
        f2=fl.getOpenVolABS(I.get("大台黑手"),15)
        if (f1>3500) or (f2>1700 and f2<1900) :
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #小主小黑無濾網1575 小主大黑無濾網1971 (42,67)1497
    if filter1(self,I)==0:
        return
    if I.get("小台未純化主力企圖")[i-1]<0 and I.get("大台黑手")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖")[i-1]>0 and I.get("大台黑手")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)  
        
        
        
############################################################################### 
import os
STittle=u"[s05]小台主力、大台黑手策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())