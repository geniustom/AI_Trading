# coding=UTF-8
############################################################################### 
def filter1(self,I):  
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
        f2=fl.getOpenVolABS(I.get("小台黑手"),15)
        f3=fl.getOpenVolABS(I.get("大台主力"),15)
        f4=fl.getOpenVolABS(I.get("小台散戶"),15)
        f5=fl.getOpenVolABS(I.get("大台黑手"),15)
        if ((f1>9 and f1<12) or (f2>3400 and f2<3900) or (f3>16.5 and f3<19) or (f4>1200 and f4<1400)) and (f5>3000 or f5<2400):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return
    
    if i==15: 
        self.Variable.append(0)
        
    aa= I.get("小台未純化主力企圖")[i-1]
    bb= I.get("電期主力")[i-1]
    
    if aa<0 and bb<0 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if aa>0 and bb>0 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
     
    if aa>0 and bb>0 and PRICE>self.Variable[0] : self.EnterShort(PRICE)
    if aa<0 and bb<0 and PRICE<self.Variable[0] : self.EnterLong(PRICE) 

    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s03]小台、電期主力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())