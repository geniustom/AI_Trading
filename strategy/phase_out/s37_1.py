# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        P=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15,start=30)
        AO=fl.getOpenVolABS(I.get("金期黑手"),15,start=30)

        #IF(OR((AO2<250),AND((P2>90),(P2<110))),0,AV2)
        if  (P>90 and P<110) or (AO<250):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return

    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("大台純主力買作為")[baseT]+I.get("小台純主力買作為")[baseT]
    base2= I.get("大台純主力賣作為")[baseT]+I.get("小台純主力賣作為")[baseT]
    base3= I.get("大台純散戶買作為")[baseT]+I.get("小台純散戶買作為")[baseT]
    base4= I.get("大台純散戶賣作為")[baseT]+I.get("小台純散戶賣作為")[baseT]

    mb=I.get("大台純主力買作為")[i-1]+I.get("小台純主力買作為")[i-1]-base1
    ms=I.get("大台純主力賣作為")[i-1]+I.get("小台純主力賣作為")[i-1]-base2    
    bb=I.get("大台純散戶買作為")[i-1]+I.get("小台純散戶買作為")[i-1]-base3
    bs=I.get("大台純散戶賣作為")[i-1]+I.get("小台純散戶賣作為")[i-1]-base4
    m=mb-ms
    b=bb-bs
    
    tr=1
    if m>tr and b<-tr : self.EnterLong(PRICE)
    if m<-tr and b>tr : self.EnterShort(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s37_1]大台加總純主力散戶作為"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())