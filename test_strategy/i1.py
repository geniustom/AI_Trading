# coding=UTF-8
############################################################################### 
def filter1(I):
    import lib.filter as fl
    run=1
    f1=fl.getOpenVolABS(I.get("大台純主力買作為")-I.get("大台純主力賣作為"),15)
    f2=fl.getOpenVolABS(I.get("小台散戶"),15)
    if (f1>6.9 and f1<8.7) or (f2>1600 and f2<2200) :
        run=0
    return run

def IsLoVolatility(I,i):
    if i<30: 
        return 0,0
        
    T=I.get("指數波動")
    A=T[i-1]
    B=T[i-10]
    C=T[i-20]
    D=T[i-30]

    if abs((A+B+C+D)/4 - A) <15 :
        return A,1

###############################################################################    
def s1(self,PRICE,i,I): #1568 1888
    #if filter1(I)==0:
    #    return
    a,ret=IsLoVolatility(I,i)
    if ret==1:
        print a
    if I.get("大台未純化主力企圖")[i-1]<0 and I.get("小台未純化主力企圖")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台未純化主力企圖")[i-1]>0 and I.get("小台未純化主力企圖")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)

   
############################################################################### 
import os
STittle=u"大小台主力企圖策略"
FName=os.path.split(__file__)[1].split('.')[0]
if __name__ == '__main__':
    exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\init.py').read())