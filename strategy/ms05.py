# coding=UTF-8
import imp
import lib.indicator as ind; imp.reload(ind);  
###############################################################################   
def filter1(self,I):    #2代濾網  IF(OR(AND((AM2>10.5),(AM2<16.5)),AND((AU2>6),(AU2<8))),0,AV2)
    import lib.filter as fl
    #if self.RunToday==1:self.RunToday=-1
    if self.RunToday==-1:
        self.RunToday=1
        F=fl.getMonthDay(I.get("TDATETIME")[0][0:8])
        J=fl.getOpenVolABS(I.get("大台散戶"),15)
        

        if (J>3000 and J<4200) or (F>9 and F<16) :
            self.RunToday=0
    return self.RunToday
############################################################################### 
def s1(self,PRICE,i,I):
    baseT= 15
    if filter1(self,I)==0: return
    if i< (baseT) : return
    if i==baseT:ind.GetIndicatorByType(I,"小台輸家00")
    base1= I.get("小台純輸家作為00")[baseT]
    
    if I.get("小台純輸家作為00")[i-1]-base1>2 : self.EnterShort(PRICE)
    if I.get("小台純輸家作為00")[i-1]-base1<-2 : self.EnterLong(PRICE)
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
     
############################################################################### 
import os
STittle=u"[ms05]小台純輸家作為00策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())
    
    
