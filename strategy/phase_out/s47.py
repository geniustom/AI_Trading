# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        Q=fl.getOpenVolABS(I.get("小台散戶"),15)
        M=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        if (Q>2700 and Q<3300) or (M>13 and M<16)or (M>38 and M<65):
            self.RunToday=0
    return self.RunToday
###############################################################################   
def s1(self,PRICE,i,I): #1554 1505
    if filter1(self,I)==0:
        return
    tp=I.get("小台未純化主力企圖")[i-1]+I.get("小台未純化主力作為")[i-1]
    ep=I.get("電期未純化主力企圖")[i-1]+I.get("電期未純化主力作為")[i-1]
    fp=I.get("金期未純化主力企圖")[i-1]+I.get("金期未純化主力作為")[i-1]
    pp=tp+ep+fp
    
    if pp<-6 : self.EnterShort(PRICE)
    if pp>6 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

        
############################################################################### 
import os
STittle=u"[s43]小台企圖作為、金電期主力加總策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())