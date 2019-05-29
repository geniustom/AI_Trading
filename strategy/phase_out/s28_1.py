# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15,start=30)
        f2=fl.getOpenVolABS(I.get("小台純散戶買企圖")-I.get("小台純散戶賣企圖"),15,start=30)
        if  (f1>0 and f1 <8.5) or (f2>4 and f2<17):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("中市大台純主力買作為")[baseT]    
    base2= I.get("中市大台純主力賣作為")[baseT] 
    
    mb=I.get("中市大台純主力買作為")[i-1]-base1
    ms=I.get("中市大台純主力賣作為")[i-1]-base2
        
    if mb-ms<-2 : self.EnterShort(PRICE)
    if mb-ms>2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s28_1]中市大台純主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())