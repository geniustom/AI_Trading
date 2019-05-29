# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
        f2=fl.getOpenVolABS(I.get("小台成交量"),15)
        if  (f1>0 and f1 <3.4) or (f2>45000 and f2<56000):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return

    mb=I.get("大台純主力買作為")[i-1]+I.get("小台純主力買作為")[i-1]
    ms=I.get("大台純主力賣作為")[i-1]+I.get("小台純主力賣作為")[i-1]    
    bb=I.get("大台純散戶買作為")[i-1]+I.get("小台純散戶買作為")[i-1]
    bs=I.get("大台純散戶賣作為")[i-1]+I.get("小台純散戶賣作為")[i-1]
    m=mb-ms
    b=bb-bs
    
    if m>6 and b<-6 : self.EnterLong(PRICE)
    if m<-6 and b>6 : self.EnterShort(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s37]大台加總純主力散戶作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())