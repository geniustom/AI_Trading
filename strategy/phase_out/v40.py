# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台散戶"),15)
    if (f1>1300 and f1<1700) or (f1>2100 and f1<3200):
        run=0
    return run

###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(I)==0:
        return

    pp=I.get("小台未純化主力企圖")[i-1]+I.get("小台未純化主力作為")[i-1]+I.get("電期主力")[i-1]
    if i==15: 
        self.Variable.append(max(I.get("大台單量")[:i]))
        self.Variable.append(pp)
        
    if I.get("大台單量")[i-1]>=self.Variable[0]:
        self.Variable[0]=I.get("大台單量")[i-1]
        self.Variable[1]=pp
    
    if pp-self.Variable[1]<-5 : self.EnterShort(PRICE)
    if pp-self.Variable[1]>5 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s40]小台企圖作為、電期主力加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())