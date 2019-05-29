# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        P=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        AM=fl.getOpenVolABS(I.get("金期主力"),15)

        #IF(OR(AND((P2>13.5),(P2<20.5)),AND((AM2>23.5),(AM2<27.5))),0,AV2)
        if (P>13.5 and P<20.5) or (AM>23.5 and AM<27.5):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return

    if I.get("中市小台買賣差")[i-1]<0 and I.get("中市大台買賣差")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("中市小台買賣差")[i-1]>0 and I.get("中市大台買賣差")[i-1]>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        
############################################################################### 
import os
STittle=u"[s21]中市大小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())