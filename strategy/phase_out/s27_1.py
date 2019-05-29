# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純散戶買企圖")-I.get("小台純散戶賣企圖"),15,start=30)
        f2=fl.getOpenVolABS(I.get("大台主力"),15,start=30)
        if (f1>99999 and f1<0) or (f2>69 and f2<110):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
        return
        
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("慢市小台未純化主力企圖")[baseT]
        
    if I.get("慢市小台未純化主力企圖")[i-1]-base1<-5 : self.EnterShort(PRICE)
    if I.get("慢市小台未純化主力企圖")[i-1]-base1>5  : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
 
      
     
############################################################################### 
import os
STittle=u"[s27_1]慢市小台未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())