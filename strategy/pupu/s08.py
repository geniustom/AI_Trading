# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        F=fl.getMonthDay(I.get("DATE")[0])
        AB=fl.getOpenVolABS(I.get("電期成交量"),15)

        #IF(OR(AND((F2>8),(F2<13)),AND((AB2>1800),(AB2<2400))),0,AV2)
        if  (F>8 and F <13) or (AB>1800 and AB<2400):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    mb=I.get("小台純主力買企圖")[i-1]
    ms=I.get("小台純主力賣企圖")[i-1]
        
    if mb-ms<-2 : self.EnterShort(PRICE)
    if mb-ms>2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s08]小台純主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())