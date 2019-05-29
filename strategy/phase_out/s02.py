# coding=UTF-8
############################################################################### 
def filter1(self,I):    #一代濾網 (已失效)
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純散戶買作為")-I.get("大台純散戶賣作為"),15)
        f2=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
        if (f1>15 and f1<21) or (f2>11 and f2<20):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
        return
    if I.get("大台未純化主力企圖")[i-1]<0 and I.get("大台黑手")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台未純化主力企圖")[i-1]>0 and I.get("大台黑手")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

     
############################################################################### 
import os
STittle=u"[s02]大台黑手策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())