# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
    f2=fl.getOpenVolABS(I.get("大台散戶"),15)
    if (f1>39 and f1<75) or (f2>2000 and f2<4000):
        run=0
    return run

###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(I)==0:
        return
    if I.get("小台未純化主力企圖動能")[i-1]<0 and I.get("電期主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖動能")[i-1]>0 and I.get("電期主力")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s03]小台、電期主力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())