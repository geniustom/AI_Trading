# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=0

    II=fl.getOpenVolABS(I.get("大台散戶"),15)
    J=fl.getOpenVolABS(I.get("大台黑手"),15)
    K=fl.getOpenVolABS(I.get("大台純主力買企圖")-I.get("大台純主力賣企圖"),15)
    R=fl.getOpenVolABS(I.get("小台黑手"),15)
    M=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)

    if ((K>0 and K<6) or (J>4700 and J<7200) or (R>2600 and R<3000) or (M>40 and M<52)) and (II<3100 or II>4800):
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
 
    pp=I.get("小台未純化主力企圖")[i-1]+I.get("電期主力")[i-1]+I.get("金期主力")[i-1]
    
    if pp<-3 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if pp>3 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
        
    if pp>3 and PRICE>self.Variable[0] and self.NowUnit==0 : self.EnterShort(PRICE)
    if pp<-3 and PRICE<self.Variable[0] and self.NowUnit==0 : self.EnterLong(PRICE) 
    
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s44_i]小台、金電期主力加總逆勢策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())