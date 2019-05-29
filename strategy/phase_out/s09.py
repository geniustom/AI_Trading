# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        N=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        P=fl.getOpenVolABS(I.get("小台成交量"),15)
        if  (N>11.5 and N <16) or (P>27000 and P<37000):
            self.RunToday=0
    return self.RunToday

###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    mb=I.get("大台純主力買作為N")[i-1]
    ms=I.get("大台純主力賣作為N")[i-1]
        
    if mb-ms<-3 : self.EnterShort(PRICE)
    if mb-ms>3 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s09]大台純主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())