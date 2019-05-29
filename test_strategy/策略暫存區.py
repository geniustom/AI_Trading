# -*- coding: utf-8 -*-


def s3(self,PRICE,i,I): #1019 1176
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<0 and I.get("小台黑手")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>0 and I.get("小台黑手")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
        
def s4(self,PRICE,i,I): #1971 1497
    if filter1(I)==0:
        return
    if I.get("小台主力")[i-1]<0 and I.get("大台黑手")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("小台主力")[i-1]>0 and I.get("大台黑手")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)  
    
    
def s5(self,PRICE,i,I): #-354 -173
    if filter1(I)==0:
        return
    if I.get("小台黑手")[i-1]<0 and I.get("大台黑手")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("小台黑手")[i-1]>0 and I.get("大台黑手")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE) 

def s2(self,PRICE,i,I): #-354 -173
    #if filter1(I)==0:
    #    return
    #losepower= -I.get("大台散戶")[i-1] - I.get("小台散戶")[i-1]
    #winpower = I.get("大台黑手")[i-1] + I.get("小台黑手")[i-1]
    p=I.get("小台黑手")[i-1]

    if p<-1000 : self.EnterShort(PRICE)
    if p>1000  :  self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE) 

 
def s0(self,PRICE,i,I): #662
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<-2 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>2 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
    

def s2(self,PRICE,i,I): #1185 1660
    if filter1(I)==0:
        return
    if I.get("小台主力")[i-1]<0 and I.get("小台散戶")[i-1]>0 : self.EnterShort(PRICE)
    if I.get("小台主力")[i-1]>0 and I.get("小台散戶")[i-1]<0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)

def s5(self,PRICE,i,I): #1061 1130
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<0 and I.get("大台散戶")[i-1]>0 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>0 and I.get("大台散戶")[i-1]<0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
    

def s3(self,PRICE,i,I): #922 1031
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<0 and I.get("小台散戶")[i-1]>0 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>0 and I.get("小台散戶")[i-1]<0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
        
def s4(self,PRICE,i,I): #1234 1618
    if filter1(I)==0:
        return
    if I.get("小台主力")[i-1]<0 and I.get("大台散戶")[i-1]>0 : self.EnterShort(PRICE)
    if I.get("小台主力")[i-1]>0 and I.get("大台散戶")[i-1]<0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)


        
def s6(self,PRICE,i,I): #395 308
    if filter1(I)==0:
        return
    if I.get("大台散戶")[i-1]>0 and I.get("小台散戶")[i-1]>0 : self.EnterShort(PRICE)
    if I.get("大台散戶")[i-1]<0 and I.get("小台散戶")[i-1]<0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
        
        
def s7(self,PRICE,i,I): #-81 -114
    if filter1(I)==0:
        return
    if I.get("金期散戶")[i-1]>0 and I.get("電期散戶")[i-1]>0 : self.EnterShort(PRICE)
    if I.get("金期散戶")[i-1]<0 and I.get("電期散戶")[i-1]<0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
        
def s8(self,PRICE,i,I): #-1001 -1189
    if filter1(I)==0:
        return
    if I.get("金期主力")[i-1]<0 and I.get("電期主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("金期主力")[i-1]>0 and I.get("電期主力")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
        
        
def s9(self,PRICE,i,I): #1892 1977
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<0 and I.get("小台主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>0 and I.get("小台主力")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
    
    
def s4(self,PRICE,i,I): #443
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<0 and I.get("電期主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>0 and I.get("電期主力")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
    
        
def s6(self,PRICE,i,I): #1555
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<0 and I.get("小台主力")[i-1]<0 and I.get("電期主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>0 and I.get("小台主力")[i-1]>0 and I.get("電期主力")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
    
def s2(self,PRICE,i,I): #-15
    if filter1(I)==0:
        return
    if I.get("大台主力")[i-1]<0 and I.get("金期主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("大台主力")[i-1]>0 and I.get("金期主力")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)
     
def s3(self,PRICE,i,I): #572
    if filter1(I)==0:
        return
    if I.get("小台主力")[i-1]<0 and I.get("金期主力")[i-1]<0 : self.EnterShort(PRICE)
    if I.get("小台主力")[i-1]>0 and I.get("金期主力")[i-1]>0 : self.EnterLong(PRICE)
    if I.get("TIME")[i-1]=="13:42": self.ExitAll(PRICE)  
