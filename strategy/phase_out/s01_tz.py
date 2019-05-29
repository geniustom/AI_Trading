# coding=UTF-8
############################################################################### 
def filter1(I): #一代濾網 (已失效)
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("小台散戶"),15)
    if (f1>6.9 and f1<8.7) or (f2>1600 and f2<2200) :
        run=0
    return run

def filter2(I): #二代濾網
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純主力買企圖")-I.get("大台純主力賣企圖"),15)
    f2=fl.getOpenVolABS(I.get("大台成交量"),15)
    if (f1>0 and f1<5.5) or (f2>84000 and f2<97000) :
        run=0
    return run
###############################################################################    
def s1(self,PRICE,i,I): #1568 1888
    #if filter2(I)==0:
    #    return
    if I.get("大台未純化主力企圖")[i-1]<0 and I.get("小台未純化主力企圖")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台未純化主力企圖")[i-1]>0 and I.get("小台未純化主力企圖")[i-1]>0 : self.EnterLong(PRICE)
        
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
    self.MaxWin=40
    self.MaxLost=50
   
############################################################################### 
import os
STittle=u"[s01]大小台主力企圖策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())