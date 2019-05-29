# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=0

    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("小台主力"),15)
    f3=fl.getOpenVolABS(I.get("小台成交量"),15)
    f4=fl.getOpenVolABS(I.get("大台黑手"),15)
    if (f1>15 and f1<30) or (f2>20 and f2<30) or (f3>29000 and f3<36000) or (f4>4400 and f4<5900):
        run=1
    return run

###############################################################################  
def s1(self,PRICE,i,I): #2330 1482->1888
    if filter1(I)==0:
        return

    if i==15: 
        self.Variable.append(0)
        
    mtx=I.get("中市小台買賣差")[i-1]
    
    if mtx<-900 and self.Variable[0]==0: self.Variable[0]=PRICE*0.994
    if mtx>900 and self.Variable[0]==0: self.Variable[0]=PRICE*1.006
        
    if mtx>900 and PRICE>self.Variable[0] : self.EnterShort(PRICE)
    if mtx<-900 and PRICE<self.Variable[0] : self.EnterLong(PRICE)
        
    self.CheckDailyExitAll(I.get("TIME")[i],PRICE)
        

        
############################################################################### 
import os
STittle=u"[s22_i]中市小台買賣差策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())