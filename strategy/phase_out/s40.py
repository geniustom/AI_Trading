# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        U=fl.getOpenVolABS(I.get("小台黑手"),15)
        AF=fl.getOpenVolABS(I.get("電期未純化主力企圖"),15)
        
        #IF(OR(AND((U2>3500),(U2<4000)),AND((AF2>8),(AF2<11))),0,AV2)
        if (U>3500 and U<4000) or (AF>8 and AF<11):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return
    pp=I.get("小台未純化主力企圖")[i-1]+I.get("小台未純化主力作為")[i-1]+I.get("電期主力")[i-1]
    if pp<-5 : self.EnterShort(PRICE)
    if pp>5 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s40]小台企圖作為、電期主力加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())