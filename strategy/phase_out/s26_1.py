# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純主力買企圖")-I.get("大台純主力賣企圖"),15,start=30)
        f2=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15,start=30)
        if (f1>38 and f1<58) or (f2>45 and f2<63):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return
    
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("慢市小台未純化主力作為")[baseT]

    if I.get("慢市小台未純化主力作為")[i-1]-base1<-3 : self.EnterShort(PRICE)
    if I.get("慢市小台未純化主力作為")[i-1]-base1>3  : self.EnterLong(PRICE)    
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s26_1]中市小台未純化主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())