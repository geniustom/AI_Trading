# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        M=fl.getOpenVolABS(I.get("大台未純化主力作為"),15)
        X=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
        AM=fl.getOpenVolABS(I.get("金期主力"),15)

        #IF(OR((M2>22),(AM2<9.5),AND((X2>11.1),(X2<16))),0,AV2)
        if (M>22) or (AM<9.5) or (X>11.1 and X<16):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return

    w=I.get("小台純主力買企圖")[i-1]-I.get("小台純主力賣企圖")[i-1]
    d=I.get("小台純主力買作為")[i-1]-I.get("小台純主力賣作為")[i-1]
    pp=w+d+I.get("電期主力")[i-1]+I.get("金期主力")[i-1]
    if pp<-3 : self.EnterShort(PRICE)
    if pp>3 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s42]小台企圖作為、金電期主力加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())