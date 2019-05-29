# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("小台純主力買作為")-I.get("小台純主力賣作為"),15,start=30)
        f2=fl.getOpenVolABS(I.get("小台純散戶買企圖")-I.get("小台純散戶賣企圖"),15,start=30)
        if  (f1>-1 and f1 <0.1) or (f2>3.5 and f2<9.5):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return

    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("大台純主力買企圖")[baseT]+I.get("小台純主力買企圖")[baseT]
    base2= I.get("大台純主力賣企圖")[baseT]+I.get("小台純主力賣企圖")[baseT]
    base3= I.get("大台純散戶買企圖")[baseT]+I.get("小台純散戶買企圖")[baseT]
    base4= I.get("大台純散戶賣企圖")[baseT]+I.get("小台純散戶賣企圖")[baseT]

    mb=I.get("大台純主力買企圖")[i-1]+I.get("小台純主力買企圖")[i-1]-base1
    ms=I.get("大台純主力賣企圖")[i-1]+I.get("小台純主力賣企圖")[i-1]-base2   
    bb=I.get("大台純散戶買企圖")[i-1]+I.get("小台純散戶買企圖")[i-1]-base3
    bs=I.get("大台純散戶賣企圖")[i-1]+I.get("小台純散戶賣企圖")[i-1]-base4
    m=mb-ms
    b=bb-bs
    
    thr=2
    if m>thr and b<-thr : self.EnterLong(PRICE)
    if m<-thr and b>thr : self.EnterShort(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s36_1]大台加總純主力散戶企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())