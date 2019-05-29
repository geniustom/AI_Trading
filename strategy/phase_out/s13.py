# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純散戶買作為")-I.get("大台純散戶賣作為"),15)
        f2=fl.getOpenVolABS(I.get("小台主力"),15)
        if  (f1>36 and f1 <49) or (f2>16 and f2<23):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
       return
    sm=I.get("小台純主力買企圖")[i-1]-I.get("小台純主力賣企圖")[i-1]
    if sm<0 and I.get("小台黑手")[i-1]<0 : self.EnterShort(PRICE)
    if sm>0 and I.get("小台黑手")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

     
############################################################################### 
import os
STittle=u"[s13]小台黑手策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())