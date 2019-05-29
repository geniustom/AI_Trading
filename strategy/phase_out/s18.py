# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        f2=fl.getOpenVolABS(I.get("大台純散戶買作為")-I.get("大台純散戶賣作為"),15)
        if (f1>14 and f1<21) or (f2>37 and f2<73):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return

    if I.get("小台買賣差")[i-1]<0 and I.get("大台買賣差")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("小台買賣差")[i-1]>0 and I.get("大台買賣差")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s18]大小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())