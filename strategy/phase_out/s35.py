# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台散戶"),15)
        f2=fl.getOpenVolABS(I.get("小台成交量"),15)
        if  (f1>1300 and f1 <1600) or (f2>40000 and f2<56000):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    b=I.get("大台純主力買作為")[i-1]+I.get("小台純主力買作為")[i-1]
    s=I.get("大台純主力賣作為")[i-1]+I.get("小台純主力賣作為")[i-1]
    
    if (b-s)<-6 : self.EnterShort(PRICE)
    if (b-s)>6  : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s35]大小台加總純主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())