# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純主力買作為")-I.get("小台純主力賣作為"),15)
        f2=fl.getOpenVolABS(I.get("大台主力"),15)
        if (f1>0.35 and f1<0.9) or (f2>35 and f2<47):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return

    w=I.get("小台純主力買企圖")[i-1]-I.get("小台純主力賣企圖")[i-1]
    d=I.get("小台純主力買作為")[i-1]-I.get("小台純主力賣作為")[i-1]
    pp=w+d+I.get("電期主力")[i-1]
    if pp<-5 : self.EnterShort(PRICE)
    if pp>5 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s41]小台企圖作為、電期主力加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())