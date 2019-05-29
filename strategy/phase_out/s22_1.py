# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台主力"),15,start=30)
        f2=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15,start=30)
        if (f1>65 and f1<96) or (f2>46 and f2<62):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return
    
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("中市小台買賣差")[baseT]

    
    if I.get("中市小台買賣差")[i-1]-base1<-900 : self.EnterShort(PRICE)
    if I.get("中市小台買賣差")[i-1]-base1>900 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s22_1]中市小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())