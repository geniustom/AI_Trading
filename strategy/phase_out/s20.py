# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
        f2=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
        if (f1>18.5 and f1<30) or (f2<6):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return      

    bd=I.get("中市大台黑手")[i-1]
    md=I.get("中市小台黑手")[i-1]
        
    if bd<0 and md<0 : self.EnterShort(PRICE)
    if bd>0 and md>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s20]中市大小台黑手策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())