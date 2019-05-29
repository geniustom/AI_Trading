# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台主力"),15)
        f2=fl.getOpenVolABS(I.get("大台散戶"),15)
        if  (f1>19 and f1<23) or (f2>1900 and f2<2700):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    tx=I.get("大台未純化主力企圖")[i-1]+I.get("小台未純化主力企圖")[i-1]
    
    if tx<-2 : self.EnterShort(PRICE)
    if tx>2  : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s32]大小台加總未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())