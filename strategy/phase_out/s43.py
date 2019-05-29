# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        if (f1>38 and f1<66) or (f1>13.5 and f1<19.5):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return
    pp=I.get("小台未純化主力企圖")[i-1]+I.get("小台未純化主力作為")[i-1]+I.get("電期主力")[i-1]+I.get("金期主力")[i-1]
    if pp<-4 : self.EnterShort(PRICE)
    if pp>4 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s43]小台企圖作為、金電期主力加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())