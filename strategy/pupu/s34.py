# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        AF=fl.getOpenVolABS(I.get("電期未純化主力企圖"),15)
        AG=fl.getOpenVolABS(I.get("電期未純化主力作為"),15)
        AT=fl.getOpenVolABS(I.get("金期純散戶買企圖")-I.get("金期純散戶賣企圖"),15)

        #IF(OR((AF2<9),(AT2<9),AND((AG2>5),(AG2<6.5))),0,AV2)
        if (AF<9) or (AT<9) or (AG>5 and AG<6.5):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return
    
    mf=I.get("金期未純化主力企圖")[i-1]
    me=I.get("電期未純化主力企圖")[i-1]
    
    if mf+me<-3 : self.EnterShort(PRICE)
    if mf+me>3: self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s34]金電期貨未純化主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())