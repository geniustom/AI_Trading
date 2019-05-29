# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純散戶買作為")-I.get("大台純散戶賣作為"),15)
        f2=fl.getOpenVolABS(I.get("大台成交量"),15)
        if (f1>19 and f1<25) or (f2>55000 and f2<74000) :
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    #if filter1(self,I)==0:
    #    return
    
    mb=I.get("小台純主力買作為2016")[i-1]
    ms=I.get("小台純主力賣作為2016")[i-1]
        
    if mb-ms<0 : self.EnterShort(PRICE)
    if mb-ms>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s07]小台純主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())