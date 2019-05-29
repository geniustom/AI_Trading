# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1  
        P=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15,start=30)
        AB=fl.getOpenVolABS(I.get("電期成交量"),15,start=30)

        #IF(OR(AND((P2>82),(P2<143)),AND((AB2>21000),(AB2<26000))),0,AV2)
        if (P>82 and P<143) or (AB>21000 and AB<26000) :
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
    base3= I.get("小台純散戶買企圖")[baseT]  
    base4= I.get("小台純散戶賣企圖")[baseT]        
       
    mb=I.get("小台純主力買企圖")[i-1]-base1
    ms=I.get("小台純主力賣企圖")[i-1]-base2
    bb=I.get("小台純散戶買企圖")[i-1]-base3
    bs=I.get("小台純散戶賣企圖")[i-1]-base4
    b=mb-bb
    s=ms-bs

    if b<0 and s>0 : self.EnterShort(PRICE)
    if b>0 and s<0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

############################################################################### 
import os
STittle=u"[s15_1]小台主力散戶企圖買賣力策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())