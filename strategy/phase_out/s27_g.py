# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    G=fl.getOpenVolABS(I.get("大台成交量"),15)
    V=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
    
    if (V>0 and V<11) or (G>54000 and G<70000):
        run=0
    return run
###############################################################################   
def s1(self,PRICE,i,I): #1532 1764 (無濾網,有濾網)
    if filter1(I)==0:
        return
        
    if i==15: 
        self.Variable.append(0)
        
    pp=I.get("慢市小台未純化主力企圖")[i-1]
        
    if pp<-2 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if pp>2 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
        
    if pp>2 and PRICE>self.Variable[0] : self.EnterLong(PRICE)
    if pp<-2 and PRICE<self.Variable[0] : self.EnterShort(PRICE)
        
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
 
      
     
############################################################################### 
import os
STittle=u"[s27]慢市小台未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())