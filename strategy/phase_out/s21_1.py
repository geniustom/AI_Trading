# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AM=fl.getOpenVolABS(I.get("金期主力"),15,start=30)
        AU=fl.getOpenVolABS(I.get("金期純散戶買作為")-I.get("金期純散戶賣作為"),15,start=30)
        
        #IF(OR(AND((AU2>19.5),(AU2<26)),AND((AM2>30),(AM2<55))),0,AV2)
        if (AU>19.5 and AU<26) or (AM>30 and AM<55):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return

    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("中市小台買賣差")[baseT]
    base2= I.get("中市大台買賣差")[baseT]

    if I.get("中市小台買賣差")[i-1]-base1<0 and I.get("中市大台買賣差")[i-1]-base2<0 : self.EnterShort(PRICE)
    if I.get("中市小台買賣差")[i-1]-base1>0 and I.get("中市大台買賣差")[i-1]-base2>0 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s21_1]中市大小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())