# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        f1=fl.getOpenVolABS(I.get("大台純散戶買企圖")-I.get("大台純散戶賣企圖"),15)
        f2=fl.getOpenVolABS(I.get("小台成交量"),15)
        if  (f1>20 and f1 <30) or (f2>39000 and f2<59000):
            self.RunToday=0
    return self.RunToday
############################################################################### 
def s1(self,PRICE,i,I): #1763
#    if filter1(self,I)==0:
#        return

    if i<15:
        return
        
    offset=3 #爆大量後幾根K棒做動作
        
    if I.get("大台單量")[i-offset]>2000 and self.NowUnit==0 :
        self.priceHL=I.get("大台高點")[i-offset]-I.get("大台低點")[i-offset] 
        self.MaxLost=self.priceHL*0.382
        #self.MaxWin=self.priceHL*1.618 #不設停利的績效比較好
        
        if I.get("大台指數")[i-offset]==I.get("大台高點")[i-offset] : 
            self.EnterShort(PRICE)
        if I.get("大台指數")[i-offset]==I.get("大台低點")[i-offset] : 
            self.EnterLong(PRICE)


    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[n05]中量反手做單策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())
    
    
'''
    if i<60:
        return

    if i>75:
        self.ExitAll(PRICE)
        return
'''