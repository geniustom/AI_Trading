# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
    f2=fl.getOpenVolABS(I.get("小台成交量"),15)
    if (f1>12 and f1<20) or (f2>49000 and f2<61000):
        run=0
    return run

###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(I)==0:
        return
    if I.get("小台未純化主力企圖動能")[i-1]<-2 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖動能")[i-1]>2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s04]小台未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())