# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        R=fl.getOpenVolABS(I.get("小台成交量"),15,start=30)
        M=fl.getOpenVolABS(I.get("大台未純化主力作為"),15,start=30)

        #IF(OR(AND((R2>220000),(R2<280000)),(M2<18)),0,AV2)
        if (R>220000 and R<280000) or (M<18):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return      

    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("中市大台黑手")[baseT]
    base2= I.get("中市小台黑手")[baseT]

    bd=I.get("中市大台黑手")[i-1]-base1
    md=I.get("中市小台黑手")[i-1]-base2
        
    if bd<0 and md<0 : self.EnterShort(PRICE)
    if bd>0 and md>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s20_1]中市大小台黑手策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())