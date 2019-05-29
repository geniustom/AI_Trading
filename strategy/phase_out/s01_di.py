# coding=UTF-8
############################################################################### 
def filter3(I): #二代濾網
    import lib.filter as fl
    run=0
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("小台散戶"),15)
    if (f1>7 and f1<7.7) or (f2>2700 and f2<3400) :
        run=1
    return run
###############################################################################    
def s1(self,PRICE,i,I): #1568 1888
    if filter3(I)==0:
        return
    if I.get("大台未純化主力企圖")[i-1]<0 and I.get("小台未純化主力企圖")[i-1]<0 : self.EnterLong(PRICE)
    if I.get("大台未純化主力企圖")[i-1]>0 and I.get("小台未純化主力企圖")[i-1]>0 : self.EnterShort(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

   
############################################################################### 
import os
STittle=u"[s01]反向大小台主力企圖策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())