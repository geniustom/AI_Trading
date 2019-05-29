# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AK=fl.getOpenVolABS(I.get("電期純散戶買作為")-I.get("電期純散戶賣作為"),15)
        AU=fl.getOpenVolABS(I.get("金期純散戶買作為")-I.get("金期純散戶賣作為"),15)
        
        #IF(OR(AND((AK2>0),(AK2<2.1)),AND((AU2>3.8),(AU2<5.5))),0,AV2)
        if (AK>0 and AK<2.1) or (AU>3.8 and AU<5.5):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    #if filter1(self,I)==0:
    #    return
    
    m=I.get("中市大台買賣差")[i-1]
    if m<-1100 : self.EnterShort(PRICE)
    if m>1100 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

############################################################################### 
import os
STittle=u"[ss02_02]中市大台買賣差"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())