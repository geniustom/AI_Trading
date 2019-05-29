# coding=UTF-8
############################################################################### 
def filter1(self,I):    #一代濾網 (已失效)
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15,start=30)
        f2=fl.getOpenVolABS(I.get("小台散戶"),15,start=30)
        if (f1>40 and f1<999) or (f2>2200 and f2<5400) :
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1568 1888
    if filter1(self,I)==0:
        return
    
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("大台未純化主力企圖")[baseT]
    base2= I.get("小台未純化主力企圖")[baseT]
        
    if I.get("大台未純化主力企圖")[i-1]-base1<0 and I.get("小台未純化主力企圖")[i-1]-base2<0 : self.EnterShort(PRICE)
    if I.get("大台未純化主力企圖")[i-1]-base1>0 and I.get("小台未純化主力企圖")[i-1]-base2>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

   
############################################################################### 
import os
STittle=u"[s01_1]大小台主力企圖策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())