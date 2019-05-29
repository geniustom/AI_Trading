# coding=UTF-8

import op_dblib as dl;      reload(dl);
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

    def get(self,dname,list_type=0):        #取得指標
        if type(dname)==str : dname=unicode(dname,'utf-8')
        for i in range(len(self.ids)):
            if dname == self.ids[i].name:  
                self.len=len(self.ids[i].data)                
                return self.ids[i].data
                break
        # 以上找不到指標，載入自定指標
        if list_type==0:
            return np.array(self.LoadCustomIndicator(dname))
        else:
            return self.LoadCustomIndicator(dname)
        
    def add(self,dname,sou):    #加入一個新指標
        ind=indicator()
        ind.name=dname
        ind.data=np.array(sou)
        #若原指標已存在則取代
        found=0
        for i in range(len(self.ids)):
            if dname == self.ids[i].name:
                print dname,u"已存在"
                found=1
                self.ids[i]=ind
                break
        if found==0:
            self.ids.append(ind)
        self.len=len(ind.data)
        #print "指標數:",len(self.ids)
        return ind.data
        
    def ShowAllTag(self):
        print "indicator length=",len(self.ids)
        for i in range(len(self.ids)):
            print self.ids[i].name
        
    def changeNameTo(self,orgname,newname):
        if type(orgname)==str : orgname=unicode(orgname,'utf-8')
        if type(newname)==str : newname=unicode(newname,'utf-8')
            
        for i in range(len(self.ids)):
            if orgname==self.ids[i].name: 
                self.ids[i].name=newname
                #self.names[i]=newname
                break
 
    def LowPassFilter(self,ni,fi):
        ret=lb.seq_intg(lb.seq_diff_filter(self.get(ni),fi))
        return ret
        
    def getHi(self,x):
        y=np.zeros(x.shape,dtype=x.dtype)
        h=0
        for i in range(len(x)):
            y[i]=max(h,x[i])
            h=y[i]
        return y
 
    def getLo(self,x):
        y=np.zeros(x.shape,dtype=x.dtype)
        h=999999
        for i in range(len(x)):
            y[i]=min(h,x[i])
            h=y[i]
        return y
          
    def GetBaseIndicator(self):
        self.changeNameTo("CO1_C_CurPrice"        ,"外1_C價格")
        self.changeNameTo("CAT_C_CurPrice"        ,"平0_C價格")
        self.changeNameTo("CI1_C_CurPrice"        ,"內1_C價格")
        self.changeNameTo("CI2_C_CurPrice"        ,"內2_C價格")
        self.changeNameTo("PO1_C_CurPrice"        ,"外1_P價格")
        self.changeNameTo("PAT_C_CurPrice"        ,"平0_P價格")
        self.changeNameTo("PI1_C_CurPrice"        ,"內1_P價格")
        self.changeNameTo("PI2_C_CurPrice"        ,"內2_P價格")
        self.changeNameTo("CO1_C_TrustBuyCnt"     ,"外1_C委買筆")
        self.changeNameTo("CAT_C_TrustBuyCnt"     ,"平0_C委買筆")
        self.changeNameTo("CI1_C_TrustBuyCnt"     ,"內1_C委買筆")
        self.changeNameTo("CI2_C_TrustBuyCnt"     ,"內2_C委買筆")
        self.changeNameTo("PO1_C_TrustBuyCnt"     ,"外1_P委買筆")
        self.changeNameTo("PAT_C_TrustBuyCnt"     ,"平0_P委買筆")
        self.changeNameTo("PI1_C_TrustBuyCnt"     ,"內1_P委買筆")
        self.changeNameTo("PI2_C_TrustBuyCnt"     ,"內2_P委買筆")
        self.changeNameTo("CO1_C_TrustSellCnt"    ,"外1_C委賣筆")
        self.changeNameTo("CAT_C_TrustSellCnt"    ,"平0_C委賣筆")
        self.changeNameTo("CI1_C_TrustSellCnt"    ,"內1_C委賣筆")
        self.changeNameTo("CI2_C_TrustSellCnt"    ,"內2_C委賣筆")
        self.changeNameTo("PO1_C_TrustSellCnt"    ,"外1_P委賣筆")
        self.changeNameTo("PAT_C_TrustSellCnt"    ,"平0_P委賣筆")
        self.changeNameTo("PI1_C_TrustSellCnt"    ,"內1_P委賣筆")
        self.changeNameTo("PI2_C_TrustSellCnt"    ,"內2_P委賣筆")
        self.changeNameTo("CO1_C_TrustBuyVol"     ,"外1_C委買口")
        self.changeNameTo("CAT_C_TrustBuyVol"     ,"平0_C委買口")
        self.changeNameTo("CI1_C_TrustBuyVol"     ,"內1_C委買口")
        self.changeNameTo("CI2_C_TrustBuyVol"     ,"內2_C委買口")
        self.changeNameTo("PO1_C_TrustBuyVol"     ,"外1_P委買口")
        self.changeNameTo("PAT_C_TrustBuyVol"     ,"平0_P委買口")
        self.changeNameTo("PI1_C_TrustBuyVol"     ,"內1_P委買口")
        self.changeNameTo("PI2_C_TrustBuyVol"     ,"內2_P委買口")
        self.changeNameTo("CO1_C_TrustSellVol"    ,"外1_C委賣口")
        self.changeNameTo("CAT_C_TrustSellVol"    ,"平0_C委賣口")
        self.changeNameTo("CI1_C_TrustSellVol"    ,"內1_C委賣口")
        self.changeNameTo("CI2_C_TrustSellVol"    ,"內2_C委賣口")
        self.changeNameTo("PO1_C_TrustSellVol"    ,"外1_P委賣口")
        self.changeNameTo("PAT_C_TrustSellVol"    ,"平0_P委賣口")
        self.changeNameTo("PI1_C_TrustSellVol"    ,"內1_P委賣口")
        self.changeNameTo("PI2_C_TrustSellVol"    ,"內2_P委賣口")
        self.changeNameTo("CO1_C_TotalBuyCnt"     ,"外1_C買成筆")
        self.changeNameTo("CAT_C_TotalBuyCnt"     ,"平0_C買成筆")
        self.changeNameTo("CI1_C_TotalBuyCnt"     ,"內1_C買成筆")
        self.changeNameTo("CI2_C_TotalBuyCnt"     ,"內2_C買成筆")
        self.changeNameTo("PO1_C_TotalBuyCnt"     ,"外1_P買成筆")
        self.changeNameTo("PAT_C_TotalBuyCnt"     ,"平0_P買成筆")
        self.changeNameTo("PI1_C_TotalBuyCnt"     ,"內1_P買成筆")
        self.changeNameTo("PI2_C_TotalBuyCnt"     ,"內2_P買成筆")
        self.changeNameTo("CO1_C_TotalSellCnt"    ,"外1_C賣成筆")
        self.changeNameTo("CAT_C_TotalSellCnt"    ,"平0_C賣成筆")
        self.changeNameTo("CI1_C_TotalSellCnt"    ,"內1_C賣成筆")
        self.changeNameTo("CI2_C_TotalSellCnt"    ,"內2_C賣成筆")
        self.changeNameTo("PO1_C_TotalSellCnt"    ,"外1_P賣成筆")
        self.changeNameTo("PAT_C_TotalSellCnt"    ,"平0_P賣成筆")
        self.changeNameTo("PI1_C_TotalSellCnt"    ,"內1_P賣成筆")
        self.changeNameTo("PI2_C_TotalSellCnt"    ,"內2_P賣成筆")
        self.changeNameTo("CO1_C_Volume"          ,"外1_C成交量")
        self.changeNameTo("CAT_C_Volume"          ,"平0_C成交量")
        self.changeNameTo("CI1_C_Volume"          ,"內1_C成交量")
        self.changeNameTo("CI2_C_Volume"          ,"內2_C成交量")
        self.changeNameTo("PO1_C_Volume"          ,"外1_P成交量")
        self.changeNameTo("PAT_C_Volume"          ,"平0_P成交量")
        self.changeNameTo("PI1_C_Volume"          ,"內1_P成交量")
        self.changeNameTo("PI2_C_Volume"          ,"內2_P成交量")

       
        
