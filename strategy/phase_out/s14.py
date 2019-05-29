# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純主力買企圖")-I.get("大台純主力賣企圖"),15)
        f2=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        if (f1>12 and f1<18) or (f2>10 and f2<19) :
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
       return
    mb=I.get("小台純主力買企圖")[i-1]
    ms=I.get("小台純主力賣企圖")[i-1]
    bb=I.get("小台純散戶買企圖")[i-1]
    bs=I.get("小台純散戶賣企圖")[i-1]
    m=mb-ms
    b=bb-bs

    if m-b<-2 : self.EnterShort(PRICE)
    if m-b>2: self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

############################################################################### 
import os
STittle=u"[s14]小台主力散戶企圖差值策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())