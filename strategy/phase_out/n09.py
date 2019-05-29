# coding=UTF-8
###############################################################################   
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        P=fl.getOpenVolABS(I.get("小台主力"),15)
        G=fl.getOpenVolABS(I.get("大台成交量"),15)
        if (P>9.5 and P<21) or (G>47000 and G<64000):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return
        
    ep=I.get("電期未純化主力作為")[i-1]
    fp=I.get("金期未純化主力作為")[i-1]
    tp=I.get("小台未純化主力作為")[i-1]
    dep=ep-fp

    if tp<-1 and ep>1 : self.EnterLong(PRICE)
    if tp>1 and ep<-1 : self.EnterShort(PRICE)

    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s43]小台企圖作為、金電期主力加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())