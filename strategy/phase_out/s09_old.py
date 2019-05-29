# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台黑手"),15)
        f2=fl.getOpenVolABS(I.get("小台散戶"),15)
        if  (f1>2300 and f1 <3000) or (f2>1600 and f2<2200):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    mb=I.get("大台純主力買作為")[i-1]
    ms=I.get("大台純主力賣作為")[i-1]
        
    if mb-ms<-3 : self.EnterShort(PRICE)
    if mb-ms>3 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s09]大台純主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())