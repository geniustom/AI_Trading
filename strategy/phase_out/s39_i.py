# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=0
    
    f1=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
    f2=fl.getOpenVolABS(I.get("小台黑手"),15)
    f3=fl.getOpenVolABS(I.get("小台成交量"),15)
    #f4=fl.getOpenVolABS(I.get("大台成交量"),15)
    if (f1>38 and f1<45) or (f2>5600 and f2<7600) or (f3>50000 and f3<57500):
        run=1
    return run

###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(I)==0:
        return
        
    if i==15: 
        self.Variable.append(0)
        
    pp=I.get("小台未純化主力作為")[i-1]+I.get("電期主力")[i-1]
    if pp<-4 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if pp>4 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
     
    if pp>4 and PRICE>self.Variable[0] and self.NowUnit==0: self.EnterShort(PRICE)
    if pp<-4 and PRICE<self.Variable[0] and self.NowUnit==0: self.EnterLong(PRICE)     
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s39_i]小台、電期主力加總逆勢策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())