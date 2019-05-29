# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純主力買企圖")-I.get("大台純主力賣企圖"),15)
        f2=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
        if  (f1>13 and f1 <18) or (f2>2 and f2<3.3):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
        return
    if I.get("慢市小台未純化主力作為")[i-1]<-3 : self.EnterShort(PRICE)
    if I.get("慢市小台未純化主力作為")[i-1]>3  : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
 
      
     
############################################################################### 
import os
STittle=u"[s26]中市小台未純化主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())