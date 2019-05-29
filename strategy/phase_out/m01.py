# coding=UTF-8
############################################################################### 

###############################################################################    
def s1(self,PRICE,i,I): #1763
    #self.MaxTrader=1
    
    tx=I.get("小台未純化主力企圖")[i-1]
    mf=I.get("金期未純化主力企圖")[i-1]
    me=I.get("電期未純化主力企圖")[i-1]
    
    if i in (15,45,75,105,135):
        btx=I.get("小台未純化主力企圖")[0]
        bmf=I.get("金期未純化主力企圖")[0]
        bme=I.get("電期未純化主力企圖")[0]
    
    if (mf+me)<-2 and (mf+me)/2>tx and tx<-2 : self.EnterShort(PRICE)
    if (mf+me)>2 and (mf+me)/2<tx and tx>2 : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)

############################################################################### 
import os
STittle=u"[m01]金電加總與小台未純化主力企圖同步性"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())