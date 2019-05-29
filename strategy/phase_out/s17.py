# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AF=fl.getOpenVolABS(I.get("電期未純化主力企圖"),15)
        AQ=fl.getOpenVolABS(I.get("金期未純化主力作為"),15)
        AR=fl.getOpenVolABS(I.get("金期純主力買企圖")-I.get("金期純主力賣企圖"),15)
                
        #IF(OR(AND((AR2=0),(AQ2<10.5)),(AF2>37)),0,AV2)
        if (AR==0 and AQ<10.5) or (AF>37):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return

    if I.get("小台買賣差")[i-1]<-1500 : self.EnterShort(PRICE)
    if I.get("小台買賣差")[i-1]>1500 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s17]小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())