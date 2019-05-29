# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        L=fl.getOpenVolABS(I.get("大台未純化主力企圖"),15)
        X=fl.getOpenVolABS(I.get("小台純主力買企圖")-I.get("小台純主力賣企圖"),15)
        AF=fl.getOpenVolABS(I.get("電期未純化主力企圖"),15)

        
        #IF(OR(AND((X2>11.1),(X2<15.5)),(AF2<9.5),AND((L2>22.5),(L2<32))),0,AV2)
        if (X>11.1 and X<15.5) or (AF<9.5) or (L>22.5 and L<32):
            self.RunToday=0
    return self.RunToday
###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(self,I)==0:
        return
    
    if I.get("慢市小台買賣差")[i-1]<-1000 : self.EnterShort(PRICE)
    if I.get("慢市小台買賣差")[i-1]>1000 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s16]慢市小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())