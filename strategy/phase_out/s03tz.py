# coding=UTF-8
############################################################################### 
def filter1(self,I):  
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
        f2=fl.getOpenVolABS(I.get("大台成交量"),15)
        if (f1>7.2 and f1<9.8) or (f2>50000 and f2<64000):
            self.RunToday=0
    return self.RunToday
def filter2(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
        f2=fl.getOpenVolABS(I.get("大台散戶"),15)
        if  (f1>4 and f1 <8) or (f2>1370 and f2<2500):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    #if filter2(self,I)==0:
    #    return

    a = I.get("小台未純化主力企圖")[i-1]
    b = I.get("電期主力")[i-1]
    if a<0 and b<0 : self.EnterShort(PRICE)
    if a>0 and b>0 : self.EnterLong(PRICE)
    #if self.NowUnit!=0 and ((a>0 and b<0)or (a<0 and b>0)):self.ExitAll(PRICE)
        
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s03]小台、電期主力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())