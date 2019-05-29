# coding=UTF-8

import datalib as lib
import numpy as np

class indicator:
    def __init__(self):
        self.name=""
        self.data=np.array([])
        self.count=0

class indicatorGroup:
    def __init__(self):
        self.ids=[]
        #self.names=np.array([])
        self.len=0
        
    def get(self,dname):        #取得指標
        if type(dname)==str : dname=unicode(dname,'utf-8')
        for i in range(len(self.ids)):
            if dname == self.ids[i].name:  
                self.len=len(self.ids[i].data)                
                return np.array( self.ids[i].data )
                break
        return np.array(self.LoadCustomIndicator(dname))
        
    def add(self,dname,sou):    #加入一個新指標
        ind=indicator()
        ind.name=dname
        ind.data=np.array(sou)
        self.ids.append(ind)
        #self.names.append(dname)
        self.len=len(ind.data)
        return ind.data
        
    def changeNameTo(self,orgname,newname):
        if type(orgname)==str : orgname=unicode(orgname,'utf-8')
        if type(newname)==str : newname=unicode(newname,'utf-8')
            
        for i in range(len(self.ids)):
            if orgname==self.ids[i].name: 
                self.ids[i].name=newname
                #self.names[i]=newname
                break
            
    def GetBaseIndicator(self):
        self.changeNameTo("Future_CurPrice"          ,"大台指數")
        self.changeNameTo("Future_Volume"            ,"大台成交量")
        self.changeNameTo("FutureWant_TrustBuyVol"   ,"大台委買口")
        self.changeNameTo("FutureWant_TrustSellVol"  ,"大台委賣口")
        self.changeNameTo("Future_TotalBuyVol"       ,"大台總委賣口")
        self.changeNameTo("Future_TotalSellVol"      ,"大台總委賣口")
        self.changeNameTo("FutureWant_TrustBuyCnt"   ,"大台委買筆")
        self.changeNameTo("FutureWant_TrustSellCnt"  ,"大台委賣筆")
        self.changeNameTo("FutureWant_TotalBuyCnt"   ,"大台買成筆")
        self.changeNameTo("FutureWant_TotalSellCnt"  ,"大台賣成筆")
        
        self.changeNameTo("FutureM_CurPrice"          ,"小台指數")
        self.changeNameTo("FutureM_Volume"            ,"小台成交量")
        self.changeNameTo("FutureWantM_TrustBuyVol"   ,"小台委買口")
        self.changeNameTo("FutureWantM_TrustSellVol"  ,"小台委賣口")
        self.changeNameTo("FutureM_TotalBuyVol"       ,"小台總委賣口")
        self.changeNameTo("FutureM_TotalSellVol"      ,"小台總委賣口")
        self.changeNameTo("FutureWantM_TrustBuyCnt"   ,"小台委買筆")
        self.changeNameTo("FutureWantM_TrustSellCnt"  ,"小台委賣筆")
        self.changeNameTo("FutureWantM_TotalBuyCnt"   ,"小台買成筆")
        self.changeNameTo("FutureWantM_TotalSellCnt"  ,"小台賣成筆")    
        
        self.changeNameTo("RealWant_Uppers"          ,"上漲家數")
        self.changeNameTo("RealWant_Downs"           ,"下跌家數")
        self.changeNameTo("RealWant_Steadys"         ,"平盤家數")
        
        timelist=[]
        ti=self.get("TDATETIME")
        for i in range(len(ti)):
            timelist.append(ti[i][9:14])
        self.add('TIME',timelist) 
        
    def LoadCustomIndicator(self,N):   
        if type(N)==str : N=unicode(N,"utf-8")
        #################### 大台 ####################
        if N==u"大台成交筆" :
            return self.add(N,self.get("大台買成筆")+self.get("大台賣成筆")) 
        if N==u"大台散戶" :
            return self.add(N,lib.seq_base(self.get("大台買成筆")-self.get("大台賣成筆")))
        if N==u"大台買賣差" :
            return self.add(N,lib.seq_base(self.get("大台委買口")-self.get("大台委賣口")))
        if N==u"大台買賣差" :
            return self.add(N,lib.seq_base((self.get("大台委買筆")-self.get("大台買成筆"))-(self.get("大台委賣筆")-self.get("大台賣成筆"))))    
        #################### 小台 ####################
        if N==u"小台成交筆" :    
            return self.add(N,self.get("小台買成筆")+self.get("小台賣成筆"))   
        if N==u"小台散戶" :
            return self.add(N,lib.seq_intg(lib.seq_diff(self.get("小台買成筆")-self.get("小台賣成筆")))) 
        if N==u"小台買賣差" :
            return self.add(N,lib.seq_base(self.get("小台委買口")-self.get("小台委賣口")))
        if N==u"小台黑手" :
            return self.add(N,lib.seq_base((self.get("小台委買筆")-self.get("小台買成筆"))-(self.get("小台委賣筆")-self.get("小台賣成筆"))))
        
        return []
        
        




def GetMainPower(self,ind):
    if len(ind.ids)==0: ind=lib.indicatorGroup()
    if len(ind.get("主力動向"))==0:
        return 0        
    
