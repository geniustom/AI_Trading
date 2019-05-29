# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
        f2=fl.getOpenVolABS(I.get("小台成交量"),15)
        if (f1>39 and f1<52) or (f2>50000 and f2<59000):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
        return
    if I.get("中市小台未純化主力企圖")[i-1]<-5 : self.EnterShort(PRICE)
    if I.get("中市小台未純化主力企圖")[i-1]>5  : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
 
      
     
############################################################################### 
import os
STittle=u"[s23]中市小台未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())