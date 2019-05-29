# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        X=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15,start=30)
        AR=fl.getOpenVolABS(I.get("金期純主力買企圖")-I.get("金期純主力賣企圖"),15,start=30)

        #IF(OR(AND((X2>39),(X2<86)),AND((AR2>17),(AR2<26))),0,AV2)
        if (X>39 and X<86) or (AR>17 and AR<26):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return

    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("小台買賣差")[baseT]
    base2= I.get("大台買賣差")[baseT]

    if I.get("小台買賣差")[i-1]-base1<0 and I.get("大台買賣差")[i-1]-base2<0 : self.EnterShort(PRICE)
    if I.get("小台買賣差")[i-1]-base1>0 and I.get("大台買賣差")[i-1]-base2>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s18_1]大小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())