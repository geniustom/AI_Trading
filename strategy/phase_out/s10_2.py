# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純散戶買作為")-I.get("大台純散戶賣作為"),15,start=30)
    f2=fl.getOpenVolABS(I.get("小台純主力買作為")-I.get("小台純主力賣作為"),15,start=30)
    if (f1>60 and f1<96) or (f1>168 and f1<287) or (f2>4.8 and f2<9.5) :
        run=0
    return run

###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    #if filter1(I)==0:
    #    return
    
    baseB= 30
    baseT= 60
    if i< (baseT+30) : return
    base0= I.get("大台未純化主力企圖")[baseB]
    base1= I.get("大台未純化主力企圖")[baseT]
    tt=I.get("大台未純化主力企圖")[i-1]-base1  
    
    if base0>0 and tt<-2 : self.EnterLong(PRICE)
    if base0<0 and tt>2 : self.EnterShort(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
 
      
     
############################################################################### 
import os
STittle=u"[s10_2]純大台主力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())