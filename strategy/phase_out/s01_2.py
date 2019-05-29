# coding=UTF-8
############################################################################### 
def filter2(I): #二代濾網
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("小台成交量"),15)
    f2=fl.getOpenVolABS(I.get("大台成交量"),15)
    if (f1>50000 and f1<63000) or (f2>54000 and f2<64000) :
        run=0
    return run

#=IF(OR(AND((O2>50000),(O2<63000)),AND((G2>54000),(G2<64000))),0,W2) 以1作門檻時
###############################################################################    
def s1(self,PRICE,i,I): #1568 1888
    if filter2(I)==0:
        return
    if I.get("大台未純化主力企圖動能")[i-1]<-1 and I.get("小台未純化主力企圖動能")[i-1]<-1 : self.EnterShort(PRICE)
    if I.get("大台未純化主力企圖動能")[i-1]>1 and I.get("小台未純化主力企圖動能")[i-1]>1 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

   
############################################################################### 
import os
STittle=u"[s01-2]大小台主力企圖動能策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())