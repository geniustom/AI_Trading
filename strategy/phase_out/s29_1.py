# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AD=fl.getOpenVolABS(I.get("電期散戶"),15,start=30)
        AO=fl.getOpenVolABS(I.get("金期黑手"),15,start=30)

        #IF(OR((AO2<190),AND((AO2>800),(AO2<1250)),AND((AD2>110),(AD2<170))),0,AV2)
        if  (AO<190) or (AO>800 and AO <1250) or (AD>110 and AD<170):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("中市大台未純化主力企圖")[baseT]    
    base2= I.get("中市小台未純化主力企圖")[baseT]     
    
    mb=I.get("中市大台未純化主力企圖")[i-1]-base1
    ms=I.get("中市小台未純化主力企圖")[i-1]-base2
        
    #if mb<0 and ms<0 : self.EnterShort(PRICE)
    #if mb>0 and ms>0 : self.EnterLong(PRICE)
    if mb+ms<-3 : self.EnterShort(PRICE)
    if mb+ms>3 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s29_1]中市大台純主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())