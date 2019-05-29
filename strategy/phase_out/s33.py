# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純散戶買作為")-I.get("大台純散戶賣作為"),15)
        f2=fl.getOpenVolABS(I.get("大台主力"),15)
        if  (f1>31 and f1 <45) or (f2>0 and f2<13):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    tx=I.get("小台未純化主力企圖")[i-1]
    mf=I.get("金期未純化主力企圖")[i-1]
    me=I.get("電期未純化主力企圖")[i-1]
    
    if mf>tx and me>tx and tx<0 : self.EnterShort(PRICE)
    if mf<tx and me<tx and tx>0 : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s33]小台與金電期貨未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())