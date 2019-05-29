# coding=UTF-8
############################################################################### 
def filter1(self,I):  
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AI=fl.getOpenVolABS(I.get("電期純主力買作為")-I.get("電期純主力賣作為"),15,start=30)
        AR=fl.getOpenVolABS(I.get("金期純主力買企圖")-I.get("金期純主力賣企圖"),15,start=30)
        
        #IF(OR((AR2<1),AND((AI2>4.5),(AI2<7.5))),0,AV2)
        if (AR<1) or (AI>4.5 and AI<7.5) :
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(self,I)==0:
        return

    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("小台未純化主力企圖")[baseT]
    base2= I.get("大台黑手")[baseT]        
        
    if I.get("小台未純化主力企圖")[i-1]-base1<0 and I.get("大台黑手")[i-1]-base2<0 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖")[i-1]-base1>0 and I.get("大台黑手")[i-1]-base2>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)  

     
############################################################################### 
import os
STittle=u"[s05_1]小台主力、大台黑手策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())