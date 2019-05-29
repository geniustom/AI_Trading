# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        II=fl.getOpenVolABS(I.get("大台主力"),15,start=30)
        X=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15,start=30)
        AK=fl.getOpenVolABS(I.get("電期純散戶買作為")-I.get("電期純散戶賣作為"),15,start=30)
        AO=fl.getOpenVolABS(I.get("金期黑手"),15,start=30)

        #IF(OR((AK2>42),(AO2<160),(X2<8),(I2<13.5)),0,AV2)
        if (AK>42) or (AO<160) or (X<8) or (II<13.5) :
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
       return
       
    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("小台純主力買企圖")[baseT]
    base2= I.get("小台純主力賣企圖")[baseT]  
    base3= I.get("小台純主力買作為")[baseT]  
    base4= I.get("小台純主力賣作為")[baseT]  
       
    mb=I.get("小台純主力買企圖")[i-1]-base1
    ms=I.get("小台純主力賣企圖")[i-1]-base2
    bb=I.get("小台純主力買作為")[i-1]-base3
    bs=I.get("小台純主力賣作為")[i-1]-base4

    if mb-ms<0 and bb-bs<0 : self.EnterShort(PRICE)
    if mb-ms>0 and bb-bs>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

############################################################################### 
import os
STittle=u"[s12_1]小台主力企圖作為策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())