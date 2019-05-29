#此策略績效soso 沒有優化必要
# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("小台成交量"),15)
    if  (f1>0 and f1 <3.4) or (f2>30000 and f2<37000):
        run=0
    return run

###############################################################################    
def s1(self,PRICE,i,I): #1763
    #if filter1(I)==0:
    #    return
    
    tx=I.get("大台純主力買企圖")[i-1]-I.get("大台純主力賣企圖")[i-1]
    mf=I.get("金期純主力買企圖")[i-1]-I.get("金期純主力賣企圖")[i-1]
    me=I.get("電期純主力買企圖")[i-1]-I.get("電期純主力賣企圖")[i-1]
    
    if mf>tx and me>tx and mf<0 and me<0 : self.EnterShort(PRICE)
    if mf<tx and me<tx and mf>0 and me>0 : self.EnterLong(PRICE)

    #if mf>tx and me>tx : self.EnterShort(PRICE)
    #if mf<tx and me<tx : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s30]小台與金電期貨純主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())