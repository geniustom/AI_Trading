# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("小台主力"),15)
    f2=fl.getOpenVolABS(I.get("小台成交量"),15)
    if  (f1>11 and f1 <25) or (f2>51000 and f2<56000):
        run=0
    return run

def filterInv(I):
    import lib.filter as fl
    run=0
    
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
    f3=fl.getOpenVolABS(I.get("小台黑手"),15)
    f4=fl.getOpenVolABS(I.get("大台成交量"),15)
    if ((f1>4.6 and f1<6) or (f2>38 and f2<56) or (f3>2600 and f3<3300)) and (f4<95000 or f4>130000):
        run=1
    return run
###############################################################################    
def s1(self,PRICE,i,I): #1763
    #if filter1(I)==0:
    #    return

    if i==15: 
        self.Variable.append(0)
    
    b=I.get("大台純主力買企圖")[i-1]+I.get("小台純主力買企圖")[i-1]
    s=I.get("大台純主力賣企圖")[i-1]+I.get("小台純主力賣企圖")[i-1]

    if (b-s)<-6 and self.Variable[0]==0: self.Variable[0]=PRICE*0.993
    if (b-s)>6 and self.Variable[0]==0: self.Variable[0]=PRICE*1.007
        
    if (b-s)>6 and PRICE>self.Variable[0] : self.EnterShort(PRICE)
    if (b-s)<-6 and PRICE<self.Variable[0] : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s31]大小台加總純主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())