# coding=UTF-8
############################################################################### 
def filter1(self,I):  
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        P=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        AK=fl.getOpenVolABS(I.get("電期純散戶買作為")-I.get("電期純散戶賣作為"),15)
        
        #IF(OR(AND((P2>12),(P2<16)),AND((AK2>0),(AK2<2.5))),0,AV2)
        if (P>12 and P<16) or (AK>0 and AK<2.5):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return
    if I.get("小台未純化主力企圖")[i-1]<-2 : self.EnterShort(PRICE)
    if I.get("小台未純化主力企圖")[i-1]>2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

############################################################################### 
import os
STittle=u"[s04]小台未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())