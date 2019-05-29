# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=0

    G=fl.getOpenVolABS(I.get("大台成交量"),15)
    J=fl.getOpenVolABS(I.get("大台黑手"),15)
    L=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    P=fl.getOpenVolABS(I.get("小台主力"),15)

    if ((G>37000 and G<58000) or (J>4700 and J<7100) or (L>4.3 and L<5.3)) and (P<21 or P>35):
        run=1
    return run

###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(I)==0:
        return
    
    if i==15: 
        self.Variable.append(0)
        
    pp=I.get("小台未純化主力企圖")[i-1]+I.get("電期主力")[i-1]+I.get("金期主力")[i-1]
    
    if pp<-3 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if pp>3 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
        
    if pp>3 and PRICE>self.Variable[0] : self.EnterShort(PRICE)
    if pp<-3 and PRICE<self.Variable[0] : self.EnterLong(PRICE)  
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s44_i]小台、金電期主力加總逆勢策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())