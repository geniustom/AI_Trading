# coding=UTF-8

############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 15
    if i< (baseT+15) : return
    base1= I.get("大台純贏家作為30")[baseT]

    if I.get("大台純贏家作為30")[i-1]-base1<-4 : self.EnterShort(PRICE)
    if I.get("大台純贏家作為30")[i-1]-base1>4 : self.EnterLong(PRICE)
        
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ml08]大台30純贏家作為策略-績效差待優化"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())