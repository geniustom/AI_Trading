# coding=UTF-8
############################################################################### 
def filter1(self,I):
    import lib.filter as fl
    if self.RunToday==-1:
        self.RunToday=1
        M=fl.getOpenVolABS(I.get("大台未純化主力作為"),15,start=30)
        AU=fl.getOpenVolABS(I.get("金期純散戶買作為")-I.get("金期純散戶賣作為"),15,start=30)

        
        #IF(OR(AND((M2>10),(M2<19)),AND((AU2>20),(AU2<26))),0,AV2)
        if (M>10 and M<19) or (AU>20 and AU<26):
            self.RunToday=0
    return self.RunToday
###############################################################################    
def s1(self,PRICE,i,I): #1763
    if filter1(self,I)==0:
        return

    baseT= 30
    if i< (baseT+15) : return
    base1= I.get("大台純主力買企圖")[baseT]
    base2= I.get("小台純主力買企圖")[baseT]  
    base3= I.get("大台純主力賣企圖")[baseT]
    base4= I.get("小台純主力賣企圖")[baseT]  
    
    b=(I.get("大台純主力買企圖")[i-1]-base1)+(I.get("小台純主力買企圖")[i-1]-base2)
    s=(I.get("大台純主力賣企圖")[i-1]-base3)+(I.get("小台純主力賣企圖")[i-1]-base4)
    
    if (b-s)<-2 : self.EnterShort(PRICE)
    if (b-s)>2  : self.EnterLong(PRICE)
    
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)


   
############################################################################### 
import os
STittle=u"[s31_1]大小台加總純主力企圖"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())