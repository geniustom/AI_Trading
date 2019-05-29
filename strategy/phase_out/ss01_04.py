# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AA=fl.getOpenVolABS(I.get("小台純散戶買作為")-I.get("小台純散戶賣作為"),15)
        AQ=fl.getOpenVolABS(I.get("金期未純化主力作為"),15)
        AR=fl.getOpenVolABS(I.get("金期純主力買企圖")-I.get("金期純主力賣企圖"),15)

        #IF(OR((AQ2>19),(AR2>25),AND((AA2>39),(AA2<51))),0,AV2)
        if  (AQ>19) or (AR>25) or (AA>39 and AA<51):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    #if filter1(self,I)==0:
    #    return
    
    tx=I.get("小台未純化主力企圖")[i-1]
    mf=I.get("金期未純化主力企圖")[i-1]
    me=I.get("電期未純化主力企圖")[i-1]
    
    if tx<0 and mf<0 and me<0 : self.EnterShort(PRICE)
    if tx>0 and mf>0 and me>0 : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

############################################################################### 
import os
STittle=u"[ss01_04]綜合未純化主力企圖同步性"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())