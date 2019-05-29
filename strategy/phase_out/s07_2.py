# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("大台成交量"),15)
    if (f1>4.6 and f1<6.6) or (f2>53000 and f2<70000) :
        run=0
    return run

###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(I)==0:
        return
    
    mb=I.get("小台純主力買作為動能")[i-1]
    ms=I.get("小台純主力賣作為動能")[i-1]
        
    if mb-ms<0 : self.EnterShort(PRICE)
    if mb-ms>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s07]小台純主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())