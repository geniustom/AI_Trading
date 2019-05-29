# coding=UTF-8
############################################################################### 

def filter1(I):
    import lib.filter as fl
    run=0

    L=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    U=fl.getOpenVolABS(I.get("小台純散戶買企圖")-I.get("小台純散戶賣企圖"),15)

    if ((L>4.6 and L<5.5) or (L>9 and L<11) or (L>2.3 and L<3.3) or (U>23 and U<31)):
        run=1
    return run
    
def init(self,i,I):
    if i==15: 
        self.Variable.append(0)
        self.RunToday=filter1(I) 
        
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    init(self,i,I)
    if self.RunToday==0: return
        
    w=I.get("小台純主力買企圖")[i-1]-I.get("小台純主力賣企圖")[i-1]
    d=I.get("小台純主力買作為")[i-1]-I.get("小台純主力賣作為")[i-1]
    pp=w+d+I.get("電期主力")[i-1]+I.get("金期主力")[i-1]
        
    if pp<-3 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if pp>3 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
        
    if pp>3 and PRICE>self.Variable[0] and self.NowUnit==0: self.EnterShort(PRICE)
    if pp<-3 and PRICE<self.Variable[0] and self.NowUnit==0: self.EnterLong(PRICE)        
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s42_i]小台企圖作為、金電期主力加總逆勢策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())