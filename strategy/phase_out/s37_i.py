# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=0
    
    f1=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
    f2=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
    f3=fl.getOpenVolABS(I.get("小台純散戶買企圖")-I.get("小台純散戶賣企圖"),15)
    #f4=fl.getOpenVolABS(I.get("大台成交量"),15)
    if (f1>0 and f1<10) or (f2>13 and f2<15) or (f3>2.6 and f3<5):
        run=1
    return run

###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(I)==0:
        return
        
    if i==15: 
        self.Variable.append(0)

    mb=I.get("大台純主力買作為")[i-1]+I.get("小台純主力買作為")[i-1]
    ms=I.get("大台純主力賣作為")[i-1]+I.get("小台純主力賣作為")[i-1]    
    bb=I.get("大台純散戶買作為")[i-1]+I.get("小台純散戶買作為")[i-1]
    bs=I.get("大台純散戶賣作為")[i-1]+I.get("小台純散戶賣作為")[i-1]
    m=mb-ms
    b=bb-bs
    tr=2

    if m<-tr and b>tr and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if m>tr and b<-tr and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
     
    if m>tr and b<-tr and PRICE>self.Variable[0] and self.NowUnit==0: self.EnterShort(PRICE)
    if m<-tr and b>tr and PRICE<self.Variable[0] and self.NowUnit==0: self.EnterLong(PRICE)     
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s37_i]大台加總純主力散戶作為逆勢策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())