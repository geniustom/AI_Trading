# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
    f3=fl.getOpenVolABS(I.get("小台純主力買作為")-I.get("小台純主力賣作為"),15)
    if  (f1>3.5 and f1 <6.1) or (f2<9.3 and f3==0):
        run=0
    return run

###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(I)==0:
        return
    
    mb=I.get("小台純主力買企圖動能")[i-1]
    ms=I.get("小台純主力賣企圖動能")[i-1]
        
    if mb-ms<-2 : self.EnterShort(PRICE)
    if mb-ms>2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s08]小台純主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())