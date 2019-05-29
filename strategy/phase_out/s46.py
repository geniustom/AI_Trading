# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        U=fl.getOpenVolABS(I.get("小台純散戶買企圖")-I.get("小台純散戶賣企圖"),15)
        V=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
        K=fl.getOpenVolABS(I.get("大台純主力買企圖")-I.get("大台純主力賣企圖"),15)
        if (U>0 and U<5) or (V>18 and V<26) or (K>4.7 and K<8.2):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return
        
    bp=I.get("電期散戶")[i-1]+I.get("金期散戶")[i-1]
    mp=I.get("電期主力")[i-1]+I.get("金期主力")[i-1]
    if bp>0 and mp<0 : self.EnterShort(PRICE)
    if bp<0 and mp>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s46]金電期主力散戶加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())