# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=0
    
    f1=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
    f2=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f3=fl.getOpenVolABS(I.get("小台成交量"),15)
    f4=fl.getOpenVolABS(I.get("大台成交量"),15)
    if (f1>0 and f1<11) or (f2>4.5 and f2<5.3) or (f3>29000 and f3<36000) or (f4>54000 and f4<60000):
        run=1
    return run

###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(I)==0:
        return

    if i==15: 
        self.Variable.append(0)
        
    pp=I.get("小台未純化主力企圖")[i-1]+I.get("小台未純化主力作為")[i-1]+I.get("電期主力")[i-1]
    if pp<-5 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if pp>5 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
        
    if pp>5 and PRICE>self.Variable[0] and self.NowUnit==0: self.EnterShort(PRICE)
    if pp<-5 and PRICE<self.Variable[0] and self.NowUnit==0: self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s40_i]小台企圖作為、電期主力加總逆勢策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())