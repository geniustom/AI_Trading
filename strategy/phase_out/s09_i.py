# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台黑手"),15)
    f2=fl.getOpenVolABS(I.get("小台散戶"),15)
    if  (f1>2300 and f1 <3000) or (f2>1600 and f2<2200):
        run=0
    return run

def filterInv(I):
    import lib.filter as fl
    run=0
    
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
    f3=fl.getOpenVolABS(I.get("小台黑手"),15)
    f4=fl.getOpenVolABS(I.get("大台成交量"),15)
    if ((f1>4.6 and f1<6) or (f2>38 and f2<56) or (f3>2600 and f3<3300)) and (f4<95000 or f4>130000):
        run=1
    return run
###############################################################################    
def s1(self,PRICE,i,I): #1763
    #if filter1(I)==0:
    #    return

    if i==15: 
        self.Variable.append(0)
    
    mb=I.get("大台純主力買作為N")[i-1]
    ms=I.get("大台純主力賣作為N")[i-1]
    m=mb-ms
    
    if m<-3 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if m>3 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
        
    if m>3 and PRICE>self.Variable[0] : self.EnterShort(PRICE)
    if m<-3 and PRICE<self.Variable[0] : self.EnterLong(PRICE)

    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
   
############################################################################### 
import os
STittle=u"[s09]大台純主力作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())