# coding=UTF-8
############################################################################### 
def filter1(self,I):  
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AI=fl.getOpenVolABS(I.get("電期純主力買作為")-I.get("電期純主力賣作為"),15)
        AJ=fl.getOpenVolABS(I.get("電期純散戶買企圖")-I.get("電期純散戶賣企圖"),15)
        AR=fl.getOpenVolABS(I.get("金期純主力買企圖")-I.get("金期純主力賣企圖"),15)
        AS=fl.getOpenVolABS(I.get("金期純主力買作為")-I.get("金期純主力賣作為"),15)
        
        #IF(OR(AND((AS2=0),(AR2<6.9)),AND((AI2=0),(AJ2>7),(AJ2<12.6))),0,AV2)
        if (AS==0 and AR<6.9) or (AI==0 and AJ>7 and AJ<12.6):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return
    if I.get("小台未純化主力企圖")[i-1]<0 and I.get("電期主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖")[i-1]>0 and I.get("電期主力")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s03]小台、電期主力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())