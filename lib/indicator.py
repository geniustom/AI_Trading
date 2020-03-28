# coding=UTF-8

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
        #if type(dname)==str : dname=unicode(dname,'utf-8')
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
                print( dname,u"已存在")
                found=1
                self.ids[i]=ind
                break
        if found==0:
            self.ids.append(ind)
        self.len=len(ind.data)
        #print( "指標數:",len(self.ids))
        return ind.data
        
    def ShowAllTag(self):
        print( "indicator length=",len(self.ids))
        for i in range(len(self.ids)):
            print( self.ids[i].name)
        
    def changeNameTo(self,orgname,newname):
        #if type(orgname)==str : orgname=unicode(orgname,'utf-8') #python2
        #if type(newname)==str : newname=unicode(newname,'utf-8') #python2
            
        for i in range(len(self.ids)):
            if orgname==self.ids[i].name: 
                self.ids[i].name=newname
                #self.names[i]=newname
                break
 
    def LowPassFilter(self,ni,fi):
        import lib.dblib as lb
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

    #比單純的企圖再多一項動能處理，也就是若目前累加為正，則讓往後正值的累加減半，若往後是負值，則正常加總，如此可避免被反向摜殺    
    #INPUT:  委買口 , 委賣口 , 委買筆 , 委賣筆 , 主力單臨界值 , 散戶單臨界值
    #OUTPUT: 未純化主力企圖 , 純主力買企圖 , 純主力賣企圖 , 純散戶買企圖 , 純散戶賣企圖
    def GetWantPower(self,n1,n2,n3,n4,t1,t2,energy=0):  
        import lib.dblib as lb
        a1=lb.seq_diff(self.get(n1))
        a2=lb.seq_diff(self.get(n2))
        a3=lb.seq_diff(self.get(n3))
        a4=lb.seq_diff(self.get(n4))
        
        ret1=np.zeros(len(a1))
        ret2=np.zeros(len(a1))
        ret3=np.zeros(len(a1))
        ret4=np.zeros(len(a1))
        ret5=np.zeros(len(a1))
        
        for i in range(1,len(a1)):
            bb = (a1[i]/a3[i]) if (abs(a3[i])>10) else 0
            ss = (a2[i]/a4[i]) if (abs(a4[i])>10) else 0 
            pp=bb-ss
            ret1[i]=pp                              #未純化的主力企圖
            ret2[i]= (bb-t1) if(bb>t1) else 0       #純化主力企圖買成分
            ret3[i]= (ss-t1) if(ss>t1) else 0       #純化主力企圖賣成分
            ret4[i]= (bb)    if(bb<t2) else 0       #純化散戶企圖買成分 
            ret5[i]= (ss)    if(ss<t2) else 0       #純化散戶企圖賣成分 
            
        if energy==0:
            return lb.seq_intg(ret1),lb.seq_intg(ret2),lb.seq_intg(ret3),lb.seq_intg(ret4),lb.seq_intg(ret5)
        else:
            return lb.getEnergy(ret1),lb.getEnergy(ret2),lb.getEnergy(ret3),lb.getEnergy(ret4),lb.getEnergy(ret5)

    #INPUT:  起始, 結束, 買成筆 , 賣成筆 , 成交口
    #OUTPUT: 未純化企圖  
    def GetNotPureWantPower(self,start,stop,n1,n2,n3,n4): 
        import lib.dblib as lb 
        if start==None: start=0
        if stop==None: stop=len(self.get(n1))
        a1=lb.seq_diff(self.get(n1)[start:stop])
        a2=lb.seq_diff(self.get(n2)[start:stop])
        a3=lb.seq_diff(self.get(n3)[start:stop])
        a4=lb.seq_diff(self.get(n4)[start:stop])
        lens=abs(start-stop)
        ret=np.zeros(lens)
        
        for i in range(1,len(a1)):
            bb = (a1[i]/a3[i]) if (abs(a3[i])>10) else 0
            ss = (a2[i]/a4[i]) if (abs(a4[i])>10) else 0       
            pp=bb-ss
            ret[i]=pp
            
        return lb.seq_intg(ret)

            
    #INPUT:  起始, 結束, 買成筆 , 賣成筆 , 成交口
    #OUTPUT: 未純化作為        
    def GetNotPureDoPower(self,start,stop,n1,n2,v1):
        import lib.dblib as lb
        dib=lb.seq_diff(self.get(n1)[start:stop])
        dis=lb.seq_diff(self.get(n2)[start:stop])
        div=lb.seq_diff(self.get(v1)[start:stop])
        lens=abs(start-stop)
        retb=np.zeros(lens)
        rets=np.zeros(lens)
        for i in range(1,len(dib)):
            bb = (div[i] / dib[i] ) if dib[i]!=0 else 0
            ss = (div[i] / dis[i] ) if dis[i]!=0 else 0
            retb[i]=bb                              #未純化主力買作為
            rets[i]=ss                              #未純化主力賣作為
            
        return lb.seq_intg(retb),lb.seq_intg(rets)  #未純化主力作為
            
    #INPUT:  起始,結束,買成筆 , 賣成筆 , 成交口 , 均口臨界值(H,L) 
    #OUTPUT: 純化作為
    def GetPureDoPower(self,start,stop,n1,n2,v1,th,tl):
        import lib.dblib as lb
        dib=lb.seq_diff(self.get(n1)[start:stop])
        dis=lb.seq_diff(self.get(n2)[start:stop])
        div=lb.seq_diff(self.get(v1)[start:stop])
        lens=abs(start-stop)
        retb=np.zeros(lens)
        rets=np.zeros(lens)
        for i in range(0,lens):
            bb = (div[i] / dib[i] ) if dib[i]!=0 else 0
            ss = (div[i] / dis[i] ) if dis[i]!=0 else 0
            
            retb[i]= (bb-tl) if(bb>tl) and (bb<th) else 0       #純化買作為
            rets[i]= (ss-tl) if(ss>tl) and (ss<th) else 0       #純化賣作為

        return lb.seq_intg(retb)-lb.seq_intg(rets)

    def GetHighLowChannel(self,rName,rTime,defMax=0,defMin=0):
        rData=self.get(rName)
        CMax=np.zeros(len(rData)) ; CMax=np.zeros(len(rData))
        CMin=np.zeros(len(rData)) ; CMin=np.zeros(len(rData))
        CMax[1]=rData[1]
        CMin[1]=rData[1]
        rangMax=0
        rangMin=0
        for i in range(2,len(rData)):
            if i<rTime :
                CMax[i]=max(CMax[i-1],rData[i]) if defMax==0 else defMax
                CMin[i]=min(CMin[i-1],rData[i]) if defMin==0 else defMin
                rangMax=CMax[i]
                rangMin=CMin[i]
            elif i%rTime==0:
                rangMax=max(rData[i-rTime:i])
                rangMin=min(rData[i-rTime:i])
            CMax[i]=rangMax
            CMin[i]=rangMin
            
        return CMax,CMin

    #皮尔逊相关系数  
    def pearsonSimilar(inA,inB):  
        return np.corrcoef(inA,inB,rowvar=0)[0][1]  
    #余弦相似度  
    def cosSimilar(inA,inB): 
        from numpy import linalg as la 
        inA=np.mat(inA)  
        inB=np.mat(inB)  
        num=float(inA*inB.T)  
        denom=la.norm(inA)*la.norm(inB)  
        return (num/denom)  


    def GetCorr(self,data,start,stop):
        coef=np.corrcoef(data,self.get(u"指數波動")[start:stop])[0][1]
        return coef

    #INPUT: 統計長度 , 買成筆 , 賣成筆 , 成交口 , 均口搜尋範圍(上限,下限,最小間距,相關性)
    #OUTPUT: 最優上下限
    def GetWinLoseDoCoef(self,start,stop,n1,n2,v1,rmax,rmin,rstep,rdiff,cor):
        winner=[0,0]
        loser=[0,0]
        corr_loser=0
        corr_winner=0
        for ii in range(rmax,rmin,-rstep):
            for jj in range(rmin,ii,rstep):
                rh=float(ii)/10
                rl=float(jj)/10
                if abs(rh-rl)<rdiff: break
                power=self.GetPureDoPower(start,stop,n1,n2,v1,rh,rl)
                #corr=np.corrcoef(TXI[start:stop],power)[0][1]
                corr=self.GetCorr(power,start,stop)
                if corr>corr_winner and corr>cor: 
                    winner=[rh,rl]
                    corr_winner=corr
                if corr<corr_loser and corr<-cor: 
                    loser=[rh,rl]
                    corr_loser=corr            
            
        #print( winner,loser,corr_winner,corr_loser)
        return winner,loser,[corr_winner,corr_loser]
            # ML01 相關性0.7 間距0.6最佳    

    def GetBaseIndicator(self):
        self.changeNameTo("Real_CurPrice"            ,"現貨指數")
        self.changeNameTo("Future_CurPrice"          ,"大台指數")
        self.changeNameTo("Future_Volume"            ,"大台成交量")
        self.changeNameTo("Future_TotalBuyVol"       ,"大台五檔買")
        self.changeNameTo("Future_TotalSellVol"      ,"大台五檔賣")
        self.changeNameTo("FutureWant_TrustBuyVol"   ,"大台委買口")
        self.changeNameTo("FutureWant_TrustSellVol"  ,"大台委賣口")
        self.changeNameTo("FutureWant_TrustBuyCnt"   ,"大台委買筆")
        self.changeNameTo("FutureWant_TrustSellCnt"  ,"大台委賣筆")
        self.changeNameTo("FutureWant_TotalBuyCnt"   ,"大台買成筆")
        self.changeNameTo("FutureWant_TotalSellCnt"  ,"大台賣成筆")
        
        self.changeNameTo("FutureM_CurPrice"          ,"小台指數")
        self.changeNameTo("FutureM_Volume"            ,"小台成交量")
        self.changeNameTo("FutureM_TotalBuyVol"       ,"小台五檔買")
        self.changeNameTo("FutureM_TotalSellVol"      ,"小台五檔賣")
        self.changeNameTo("FutureWantM_TrustBuyVol"   ,"小台委買口")
        self.changeNameTo("FutureWantM_TrustSellVol"  ,"小台委賣口")
        self.changeNameTo("FutureWantM_TrustBuyCnt"   ,"小台委買筆")
        self.changeNameTo("FutureWantM_TrustSellCnt"  ,"小台委賣筆")
        self.changeNameTo("FutureWantM_TotalBuyCnt"   ,"小台買成筆")
        self.changeNameTo("FutureWantM_TotalSellCnt"  ,"小台賣成筆")    
        
        self.changeNameTo("Future_TF_CurPrice"          ,"金期指數")
        self.changeNameTo("Future_TF_Volume"            ,"金期成交量")
        self.changeNameTo("FutureWant_TF_TrustBuyVol"   ,"金期委買口")
        self.changeNameTo("FutureWant_TF_TrustSellVol"  ,"金期委賣口")
        self.changeNameTo("FutureWant_TF_TrustBuyCnt"   ,"金期委買筆")
        self.changeNameTo("FutureWant_TF_TrustSellCnt"  ,"金期委賣筆")
        self.changeNameTo("FutureWant_TF_TotalBuyCnt"   ,"金期買成筆")
        self.changeNameTo("FutureWant_TF_TotalSellCnt"  ,"金期賣成筆")        
        
        self.changeNameTo("Future_TE_CurPrice"          ,"電期指數")
        self.changeNameTo("Future_TE_Volume"            ,"電期成交量")
        self.changeNameTo("FutureWant_TE_TrustBuyVol"   ,"電期委買口")
        self.changeNameTo("FutureWant_TE_TrustSellVol"  ,"電期委賣口")
        self.changeNameTo("FutureWant_TE_TrustBuyCnt"   ,"電期委買筆")
        self.changeNameTo("FutureWant_TE_TrustSellCnt"  ,"電期委賣筆")
        self.changeNameTo("FutureWant_TE_TotalBuyCnt"   ,"電期買成筆")
        self.changeNameTo("FutureWant_TE_TotalSellCnt"  ,"電期賣成筆")         

        self.changeNameTo("RealWant_Uppers"          ,"上漲家數")
        self.changeNameTo("RealWant_Downs"           ,"下跌家數")
        self.changeNameTo("RealWant_UpperLimits"     ,"漲停家數")
        self.changeNameTo("RealWant_DownLimits"      ,"跌停家數")
        self.changeNameTo("RealWant_Steadys"         ,"平盤家數")
        
        timelist=[]
        daylist=[]
        ti=self.get("TDATETIME")
        for i in range(len(ti)):
            timelist.append(ti[i][9:14])
            daylist.append(ti[i][0:8])
        self.add('DATE',daylist) 
        self.add('TIME',timelist) 
        
        
    def LoadCustomIndicator(self,N):
        import lib.dblib as lb
        #if type(N)==str :  N=unicode(N,"utf-8")
        #################### 指數 ####################
        if N==u"現期價差" : 
            return self.add(N,self.get("大台指數")-self.get("現貨指數"))
        if N==u"指數波動" : 
            return self.add(N,lb.seq_base(self.get("大台指數")))
        ##################### 量  ####################
        if N==u"大台單量" : 
            return self.add(N,lb.seq_diff(self.get(u"大台成交量")))
        #################### 大台 ####################
        if N==u"大台成交筆" :
            return self.add(N,self.get("大台買成筆")+self.get("大台賣成筆")) 
        if N==u"大台散戶" :
            return self.add(N,lb.seq_base(self.get("大台買成筆")-self.get("大台賣成筆")))
        if N==u"大台買賣差" :
            return self.add(N,lb.seq_base(self.get("大台委買口")-self.get("大台委賣口")))
        if N==u"大台黑手" :
            return self.add(N,lb.seq_base((self.get("大台委買筆")-self.get("大台買成筆"))-(self.get("大台委賣筆")-self.get("大台賣成筆"))))    
        if N==u"大台主力" : 
             return self.add(N,self.GetNotPureWantPower(None,None,"大台委買口","大台委賣口","大台委買筆","大台委賣筆"))
        if N==u"大台五檔買累計" :
            return self.add(N,lb.seq_intg((self.get("大台五檔買"))))
        if N==u"大台五檔賣累計" :
            return self.add(N,lb.seq_intg((self.get("大台五檔賣"))))  
        if N==u"大台虛掛單" :
            return self.add(N,lb.seq_base((self.get("大台委買口")-self.get("大台五檔買累計"))-(self.get("大台委賣口")-self.get("大台五檔賣累計"))))      
        if N==u"大台實掛單" :
            return self.add(N,lb.seq_base((self.get("大台五檔買累計")-self.get("大台五檔賣累計"))))      

        #################### 小台 ####################
        if N==u"小台成交筆" :    
            return self.add(N,self.get("小台買成筆")+self.get("小台賣成筆"))   
        if N==u"小台散戶" :
            return self.add(N,lb.seq_intg(lb.seq_diff(self.get("小台買成筆")-self.get("小台賣成筆")))) 
        if N==u"小台買賣差" :
            return self.add(N,lb.seq_base(self.get("小台委買口")-self.get("小台委賣口")))
        if N==u"小台黑手" :
            return self.add(N,lb.seq_base((self.get("小台委買筆")-self.get("小台買成筆"))-(self.get("小台委賣筆")-self.get("小台賣成筆"))))
        if N==u"小台主力" :  
             return self.add(N,self.GetNotPureWantPower(None,None,"小台委買口","小台委賣口","小台委買筆","小台委賣筆"))
        if N==u"小台五檔買累計" :
            return self.add(N,lb.seq_intg((self.get("小台五檔買"))))
        if N==u"小台五檔賣累計" :
            return self.add(N,lb.seq_intg((self.get("小台五檔賣"))))     
        if N==u"小台虛掛單" :
            return self.add(N,lb.seq_base((self.get("小台委買口")-self.get("小台五檔買累計"))-(self.get("小台委賣口")-self.get("小台五檔賣累計"))))      
        if N==u"小台實掛單" :
            return self.add(N,lb.seq_base((self.get("小台五檔買累計")-self.get("小台五檔賣累計"))))      
        #################### 金期 ####################
        if N==u"金期主力" :  
             return self.add(N,self.GetNotPureWantPower(None,None,"金期委買口","金期委賣口","金期委買筆","金期委賣筆"))   
        if N==u"金期散戶" :
            return self.add(N,lb.seq_base(self.get("金期買成筆")-self.get("金期賣成筆")))
        if N==u"金期買賣差" :
            return self.add(N,lb.seq_base(self.get("金期委買口")-self.get("金期委賣口")))
        if N==u"金期黑手" :
            return self.add(N,lb.seq_base((self.get("金期委買筆")-self.get("金期買成筆"))-(self.get("金期委賣筆")-self.get("金期賣成筆"))))
        #################### 電期 ####################
        if N==u"電期主力" :  
             return self.add(N,self.GetNotPureWantPower(None,None,"電期委買口","電期委賣口","電期委買筆","電期委賣筆")) 
        if N==u"電期散戶" :
            return self.add(N,lb.seq_base(self.get("電期買成筆")-self.get("電期賣成筆")))
        if N==u"電期買賣差" :
            return self.add(N,lb.seq_base(self.get("電期委買口")-self.get("電期委賣口")))
        if N==u"電期黑手" :
            return self.add(N,lb.seq_base((self.get("電期委買筆")-self.get("電期買成筆"))-(self.get("電期委賣筆")-self.get("電期賣成筆"))))
        ##################  低頻成分  ##################
        if N==u"慢市上漲家數變動" :
            return self.add(N,self.LowPassFilter("上漲家數",5))
        if N==u"慢市下跌家數變動" :
            return self.add(N,self.LowPassFilter("下跌家數",5))  
        if N==u"慢市小台買賣差" :
            return self.add(N,self.LowPassFilter("小台買賣差",500))      
        if N==u"慢市大台買賣差" :
            return self.add(N,self.LowPassFilter("大台買賣差",500))   
        if N==u"慢市電期買賣差" :
            return self.add(N,self.LowPassFilter("電期買賣差",10))   
        if N==u"慢市金期買賣差" :
            return self.add(N,self.LowPassFilter("金期買賣差",10))   
        if N==u"慢市大台散戶" :
            return self.add(N,self.LowPassFilter("大台散戶",100))   
        if N==u"慢市小台散戶" :
            return self.add(N,self.LowPassFilter("小台散戶",100))   
        if N==u"慢市大台黑手" :
            return self.add(N,self.LowPassFilter("大台黑手",100))   
        if N==u"慢市小台黑手" :
            return self.add(N,self.LowPassFilter("小台黑手",100))   
        ###############################################
        if N==u"大台高點" :
            return self.add(N,self.getHi(self.get("大台指數")))
        if N==u"大台低點" :
            return self.add(N,self.getLo(self.get("大台指數")))
        if N==u"大台振福" :
            return self.add(N,self.get("大台高點")-self.get("大台低點"))
        ###############################################
        #if N==u""            
            
        #GetSpecialIndicator(self) #載入特別指標 (因為指標會改寫所以每次要重讀)
        return []
        
        


def GetIndicatorByType(indi,name):
    if name=="小台贏家00":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.6,0.7)  #最佳 0.6,0.7
        indi.add(u"小台純贏家作為00",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1]))
        x,y=indi.GetHighLowChannel(u"小台純贏家作為00",30,1,-1)
        indi.add(u"小台純贏家作為00高通道",x)
        indi.add(u"小台純贏家作為00低通道",y)
    elif name=="小台贏家15":
        winner,loser,corr=indi.GetWinLoseDoCoef(15,30,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.6,0.8)  #最佳 0.6,0.8
        indi.add(u"小台純贏家作為15",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1]))  
        x,y=indi.GetHighLowChannel(u"小台純贏家作為15",30,1,-1)
        indi.add(u"小台純贏家作為15高通道",x)
        indi.add(u"小台純贏家作為15低通道",y)
    elif name=="小台贏家30":
        winner,loser,corr=indi.GetWinLoseDoCoef(30,45,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.5,0.9)  #最佳 
        indi.add(u"小台純贏家作為30",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1])) 
        x,y=indi.GetHighLowChannel(u"小台純贏家作為30",30,1,-1)
        indi.add(u"小台純贏家作為30高通道",x)
        indi.add(u"小台純贏家作為30低通道",y)
    elif name=="小台贏家45":
        winner,loser,corr=indi.GetWinLoseDoCoef(45,60,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.5,0.9)  #最佳 
        indi.add(u"小台純贏家作為45",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1]))
    elif name=="小台輸家00":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.4,0.7)  #最佳 0.6,0.7
        indi.add(u"小台純輸家作為00",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",loser[0],loser[1]))
        x,y=indi.GetHighLowChannel(u"小台純輸家作為00",30,1,-1)
        indi.add(u"小台純輸家作為00高通道",x)
        indi.add(u"小台純輸家作為00低通道",y)
    elif name=="小台輸家15":
        winner,loser,corr=indi.GetWinLoseDoCoef(15,30,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.6,0.8)  #最佳 0.6,0.8
        indi.add(u"小台純輸家作為15",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",loser[0],loser[1]))  
    elif name=="小台輸家30":
        winner,loser,corr=indi.GetWinLoseDoCoef(30,45,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.5,0.9)  #最佳 
        indi.add(u"小台純輸家作為30",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",loser[0],loser[1]))       
    elif name=="小台輸家45":
        winner,loser,corr=indi.GetWinLoseDoCoef(45,60,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.5,0.9)  #最佳 
        indi.add(u"小台純輸家作為45",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",loser[0],loser[1]))
    elif name=="大台贏家00":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"大台買成筆","大台賣成筆","大台成交量",45,5,2,0.6,0.8)  #最佳 0.6,0.7
        indi.add(u"大台純贏家作為00",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",winner[0],winner[1]))
    elif name=="大台贏家15":
        winner,loser,corr=indi.GetWinLoseDoCoef(15,30,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.2,0.9)  #最佳 0.6,0.8
        indi.add(u"大台純贏家作為15",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",winner[0],winner[1]))  
    elif name=="大台贏家30":
        winner,loser,corr=indi.GetWinLoseDoCoef(30,45,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.2,0.9)  #最佳 
        indi.add(u"大台純贏家作為30",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",winner[0],winner[1]))       
    elif name=="大台贏家45":
        winner,loser,corr=indi.GetWinLoseDoCoef(45,60,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.2,0.9)  #最佳 
        indi.add(u"大台純贏家作為45",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",winner[0],winner[1]))
    elif name=="大台輸家00":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.2,0.8)  #最佳 0.2,0.8
        indi.add(u"大台純輸家作為00",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",loser[0],loser[1]))
    elif name=="大台輸家15":
        winner,loser,corr=indi.GetWinLoseDoCoef(15,30,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.3,0.8)  #最佳 0.6,0.8
        indi.add(u"大台純輸家作為15",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",loser[0],loser[1]))  
    elif name=="大台輸家30":
        winner,loser,corr=indi.GetWinLoseDoCoef(30,45,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.3,0.8)  #最佳 
        indi.add(u"大台純輸家作為30",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",loser[0],loser[1]))       
    elif name=="大台輸家45":
        winner,loser,corr=indi.GetWinLoseDoCoef(45,60,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.2,0.8)  #最佳 
        indi.add(u"大台純輸家作為45",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",loser[0],loser[1]))
    elif name=="大台未純化大單企圖":
        v=indi.GetNotPureWantPower(0,indi.len,"大台委買口","大台委賣口","大台委買筆","大台委賣筆")
        indi.add(u"大台未純化大單企圖",v) 
        x,y=indi.GetHighLowChannel(u"大台未純化大單企圖",30,1,-1)
        indi.add(u"大台未純化大單企圖高通道",x)
        indi.add(u"大台未純化大單企圖低通道",y)
    elif name=="大台未純化大單作為":
        e,f=indi.GetNotPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量")
        indi.add(u"大台未純化大單作為",(e-f)) 
        x,y=indi.GetHighLowChannel(u"大台未純化大單作為",30,1,-1)
        indi.add(u"大台未純化大單作為高通道",x)
        indi.add(u"大台未純化大單作為低通道",y)
    elif name=="小台未純化大單企圖":
        v=indi.GetNotPureWantPower(0,indi.len,"小台委買口","小台委賣口","小台委買筆","小台委賣筆")
        indi.add(u"小台未純化大單企圖",v) 
        x,y=indi.GetHighLowChannel(u"小台未純化大單企圖",30,1,-1)
        indi.add(u"小台未純化大單企圖高通道",x)
        indi.add(u"小台未純化大單企圖低通道",y)
    elif name=="小台未純化大單作為":
        e,f=indi.GetNotPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量")
        indi.add(u"小台未純化大單作為",(e-f)) 
        x,y=indi.GetHighLowChannel(u"小台未純化大單作為",30,1,-1)
        indi.add(u"小台未純化大單作為高通道",x)
        indi.add(u"小台未純化大單作為低通道",y) 
    elif name=="金期未純化大單作為":
        e,f=indi.GetNotPureDoPower(0,indi.len,"金期買成筆","金期賣成筆","金期成交量")
        indi.add(u"金期未純化大單作為",(e-f)) 
        x,y=indi.GetHighLowChannel(u"金期未純化大單作為",30,1,-1)
        indi.add(u"金期未純化大單作為高通道",x)
        indi.add(u"金期未純化大單作為低通道",y)
    elif name=="電期未純化大單作為":
        e,f=indi.GetNotPureDoPower(0,indi.len,"電期買成筆","電期賣成筆","電期成交量")
        indi.add(u"電期未純化大單作為",(e-f)) 
        x,y=indi.GetHighLowChannel(u"電期未純化大單作為",30,1,-1)
        indi.add(u"電期未純化大單作為高通道",x)
        indi.add(u"電期未純化大單作為低通道",y)
    elif name=="大台散戶":
        x,y=indi.GetHighLowChannel(u"大台散戶",30,1000,-1000)
        indi.add(u"大台散戶高通道",x)
        indi.add(u"大台散戶低通道",y)
    elif name=="大台黑手":
        x,y=indi.GetHighLowChannel(u"大台黑手",30,500,-500)
        indi.add(u"大台黑手高通道",x)
        indi.add(u"大台黑手低通道",y)
    elif name=="小台黑手":
        x,y=indi.GetHighLowChannel(u"小台黑手",30,500,-500)
        indi.add(u"小台黑手高通道",x)
        indi.add(u"小台黑手低通道",y)

def GetSpecialIndicator(indi):
    return
    #e,f,g,h,i,j=indi.GetDoPowerEx("小台買成筆","小台賣成筆","小台成交量",indi.mtx_winner_ub,indi.mtx_winner_lb,indi.mtx_loser_ub,indi.mtx_loser_ub)







'''
    if name=="大台贏家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.2,0.9)  #最佳 0.2,0.9
        indi.add(u"大台純贏家作為",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",winner[0],winner[1]))
        
    if name=="大台輸家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"大台買成筆","大台賣成筆","大台成交量",30,0,1,0.5,0.8)  #最佳 0.5,0.8
        indi.add(u"大台純輸家作為",indi.GetPureDoPower(0,indi.len,"大台買成筆","大台賣成筆","大台成交量",loser[0],loser[1]))
        
    if name=="小台贏家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.6,0.7)  #最佳 0.6,0.7
        indi.add(u"小台純贏家作為",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1]))
        
    if name=="小台輸家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.4,0.7)  #最佳 0.4,0.7
        indi.add(u"小台純輸家作為",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",loser[0],loser[1]))

    if name=="電期贏家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"電期買成筆","電期賣成筆","電期成交量",30,0,1,0.5,0.7)  #電期最佳 0.5,0.7
        indi.add(u"電期純贏家作為",indi.GetPureDoPower(0,indi.len,"電期買成筆","電期賣成筆","電期成交量",winner[0],winner[1]))
        
    if name=="電期輸家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"電期買成筆","電期賣成筆","電期成交量",30,0,1,0.6,0.7)  #電期最佳 0.6,0.7
        indi.add(u"電期純輸家作為",indi.GetPureDoPower(0,indi.len,"電期買成筆","電期賣成筆","電期成交量",loser[0],loser[1]))
        
    if name=="金期贏家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"金期買成筆","金期賣成筆","金期成交量",30,0,1,0.8,0.6)  #金期最佳
        indi.add(u"金期純贏家作為",indi.GetPureDoPower(0,indi.len,"金期買成筆","金期賣成筆","金期成交量",winner[0],winner[1]))
        
    if name=="金期輸家":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,15,"金期買成筆","金期賣成筆","金期成交量",30,0,1,0.6,0.8)  #金期最佳
        indi.add(u"金期純輸家作為",indi.GetPureDoPower(0,indi.len,"金期買成筆","金期賣成筆","金期成交量",loser[0],loser[1]))

    if name=="小台贏家30":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,30,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.3,0.9)  #最佳 0.3,0.9
        indi.add(u"小台純贏家作為30",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1]))
        
    if name=="小台輸家30":
        winner,loser,corr=indi.GetWinLoseDoCoef(0,30,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0,0.8)  #最佳 0,0.8
        indi.add(u"小台純輸家作為30",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",loser[0],loser[1]))

    if name=="小台贏家60":
        winner,loser,corr=indi.GetWinLoseDoCoef(45,60,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.5,0.85)  #最佳 0.5,0.85
        indi.add(u"小台純贏家作為60",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1]))
        
    if name=="小台輸家60":
        winner,loser,corr=indi.GetWinLoseDoCoef(30,60,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.5,0.8)  #最佳 0,0.8
        indi.add(u"小台純輸家作為60",indi.GetPureDoPower(0,indi.len,"小台買成筆","小台賣成筆","小台成交量",loser[0],loser[1]))
'''     

   
'''
    if indi.len>=15:
        winner,loser,corr=GetWinLoseDoPower(indi,0,15,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.6,0.7)
        #print( winner , loser , corr)
        e,f,g,h,i,j=indi.GetDoPowerEx("小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1],loser[0],loser[1])
        indi.add(u"小台未純化大單買作為",e) 
        indi.add(u"小台未純化大單賣作為",f) 
        indi.add(u"小台未純化大單作為",(e-f))
        indi.add(u"小台純贏家買作為",g) 
        indi.add(u"小台純贏家賣作為",h)
        indi.add(u"小台純贏家作為",(g-h)) 
        indi.add(u"小台純輸家買作為",i) 
        indi.add(u"小台純輸家賣作為",j)
        indi.add(u"小台純輸家作為",(i-j))          

        
    if indi.len>=15:
        winner,loser,corr=GetWinLoseDoPower(indi,0,15,"電期買成筆","電期賣成筆","電期成交量",30,0)
        #print( winner , loser , corr)
        e,f,g,h,i,j=indi.GetDoPowerEx("電期買成筆","電期賣成筆","電期成交量",winner[0],winner[1],loser[0],loser[1])
        indi.add(u"電期未純化大單買作為",e) 
        indi.add(u"電期未純化大單賣作為",f) 
        indi.add(u"電期未純化大單作為",(e-f))
        indi.add(u"電期純贏家買作為",g) 
        indi.add(u"電期純贏家賣作為",h)
        indi.add(u"電期純贏家作為",(g-h)) 
        indi.add(u"電期純輸家買作為",i) 
        indi.add(u"電期純輸家賣作為",j)
        indi.add(u"電期純輸家作為",(i-j)) 

    if indi.len>=15:
        winner,loser,corr=GetWinLoseDoPower(indi,0,15,"金期買成筆","金期賣成筆","金期成交量",30,0)
        #print( winner , loser , corr)
        e,f,g,h,i,j=indi.GetDoPowerEx("金期買成筆","金期賣成筆","金期成交量",winner[0],winner[1],loser[0],loser[1])
        indi.add(u"金期未純化大單買作為",e) 
        indi.add(u"金期未純化大單賣作為",f) 
        indi.add(u"金期未純化大單作為",(e-f))
        indi.add(u"金期純贏家買作為",g) 
        indi.add(u"金期純贏家賣作為",h)
        indi.add(u"金期純贏家作為",(g-h)) 
        indi.add(u"金期純輸家買作為",i) 
        indi.add(u"金期純輸家賣作為",j)
        indi.add(u"金期純輸家作為",(i-j)) 
        



    if indi.len>=30:
        winner,loser,corr=GetWinLoseDoPower(indi,0,30,"大台買成筆","大台賣成筆","大台成交量",30,0)
        #print( winner , loser , corr)
        e,f,g,h,i,j=indi.GetDoPowerEx("大台買成筆","大台賣成筆","大台成交量",winner[0],winner[1],loser[0],loser[1])
        indi.add(u"大台未純化大單買作為30",e) 
        indi.add(u"大台未純化大單賣作為30",f) 
        indi.add(u"大台未純化大單作為30",(e-f))
        indi.add(u"大台純贏家買作為30",g) 
        indi.add(u"大台純贏家賣作為30",h)
        indi.add(u"大台純贏家作為30",(g-h)) 
        indi.add(u"大台純輸家買作為30",i) 
        indi.add(u"大台純輸家賣作為30",j)
        indi.add(u"大台純輸家作為30",(i-j)) 

    if indi.len>=30:
        winner,loser,corr=GetWinLoseDoPower(indi,0,30,"小台買成筆","小台賣成筆","小台成交量",30,0,1,0.7,0.9)
        #print( winner , loser , )
        e,f,g,h,i,j=indi.GetDoPowerEx("小台買成筆","小台賣成筆","小台成交量",winner[0],winner[1],loser[0],loser[1])
        indi.add(u"小台未純化大單買作為30",e) 
        indi.add(u"小台未純化大單賣作為30",f) 
        indi.add(u"小台未純化大單作為30",(e-f))
        indi.add(u"小台純贏家買作為30",g) 
        indi.add(u"小台純贏家賣作為30",h)
        indi.add(u"小台純贏家作為30",(g-h)) 
        indi.add(u"小台純輸家買作為30",i) 
        indi.add(u"小台純輸家賣作為30",j)
        indi.add(u"小台純輸家作為30",(i-j)) 
#'''











'''
#INPUT: 統計長度 , 買成筆 , 賣成筆 , 成交口 , 軍口搜尋範圍(上限,下限)
#OUTPUT: 最優上下限
def GetWinLoseDoPower(indi,start,stop,n1,n2,v1,rmax,rmin):
    step=1
    TXI=indi.get(u"指數波動")
    winner=[]
    loser=[]
    corr_loser=1
    corr_winner=-1
    for ii in range(rmax,rmin,-step):
        for jj in range(rmin,ii,step):
            rh=float(ii)/10
            rl=float(jj)/10
            corr=np.corrcoef(TXI[start:stop],indi.GetPureDoPower(start,stop,n1,n2,v1,rh,rl))[0][1]
            if corr>corr_winner: 
                winner=[rh,rl]
                corr_winner=corr
            if corr<corr_loser: 
                loser=[rh,rl]
                corr_loser=corr
               
    if abs(winner[0]-winner[1])<0.7 or abs(corr_winner)<0.9:
        winner=[0,0]
        corr_winner=0
    if abs(loser[0]-loser[1])<0.7 or abs(corr_loser)<0.9:
        loser=[0,0]
        corr_loser=0
        
    return winner , loser , [corr_winner,corr_loser]
'''

















        


#'''

'''
    #比單純的作為再多一項動能處理，也就是若目前累加為正，則讓往後正值的累加減半，若往後是負值，則正常加總，如此可避免被反向摜殺
    #INPUT:  買成筆 , 賣成筆 , 成交口 , 主力單臨界值 , 散戶單臨界值
    #OUTPUT: 未純化主力作為 , 純主力買作為 , 純主力賣作為 , 純散戶買作為 , 純散戶賣作為    
    def GetDoPower(self,n1,n2,v1,t1,t2,energy=0):
        dib=lb.seq_diff(self.get(n1))
        dis=lb.seq_diff(self.get(n2))
        div=lb.seq_diff(self.get(v1))

        ret1=np.zeros(len(dib))
        ret2=np.zeros(len(dib))
        ret3=np.zeros(len(dib))
        ret4=np.zeros(len(dib))
        ret5=np.zeros(len(dib))
        ret6=np.zeros(len(dib))

        for i in range(1,len(dib)):
            bb = (div[i] / dib[i] ) if dib[i]!=0 else 0
            ss = (div[i] / dis[i] ) if dis[i]!=0 else 0
            ret1[i]=bb                              #未純化主力買作為
            ret2[i]=ss                              #未純化主力賣作為
            ret3[i]= (bb-t1) if(bb>t1) else 0       #純主力買作為
            ret4[i]= (ss-t1) if(ss>t1) else 0       #純主力賣作為
            ret5[i]= (bb)    if(bb<t2) else 0       #純散戶買作為 
            ret6[i]= (ss)    if(ss<t2) else 0       #純散戶賣作為
        
        if energy==0:
            return lb.seq_intg(ret1),lb.seq_intg(ret2),lb.seq_intg(ret3),lb.seq_intg(ret4),lb.seq_intg(ret5),lb.seq_intg(ret6)
        else:
            return lb.getEnergy(ret1),lb.getEnergy(ret2),lb.getEnergy(ret3),lb.getEnergy(ret4),lb.getEnergy(ret5),lb.getEnergy(ret6)

    #INPUT:  買成筆 , 賣成筆 , 成交口 , 主力單臨界值(H,L) , 散戶單臨界值(H,L)
    #OUTPUT: 未純化主力作為 , 純主力買作為 , 純主力賣作為 , 純散戶買作為 , 純散戶賣作為    
    def GetDoPowerEx(self,n1,n2,v1,t1h,t1l,t2h,t2l):
        dib=lb.seq_diff(self.get(n1))
        dis=lb.seq_diff(self.get(n2))
        div=lb.seq_diff(self.get(v1))

        ret1=np.zeros(len(dib))
        ret2=np.zeros(len(dib))
        ret3=np.zeros(len(dib))
        ret4=np.zeros(len(dib))
        ret5=np.zeros(len(dib))
        ret6=np.zeros(len(dib))

        for i in range(1,len(dib)):
            bb = (div[i] / dib[i] ) if dib[i]!=0 else 0
            ss = (div[i] / dis[i] ) if dis[i]!=0 else 0
            ret1[i]=bb                              #未純化主力買作為
            ret2[i]=ss                              #未純化主力賣作為
            ret3[i]= (bb-t1l) if(bb>t1l) and (bb<t1h) else 0       #純主力買作為
            ret4[i]= (ss-t1l) if(ss>t1l) and (ss<t1h) else 0       #純主力賣作為
            ret5[i]= (bb-t2l) if(bb>t2l) and (bb<t2h) else 0       #純散戶買作為 
            ret6[i]= (ss-t2l) if(ss>t2l) and (ss<t2h) else 0       #純散戶賣作為

        return lb.seq_intg(ret1),lb.seq_intg(ret2),lb.seq_intg(ret3),lb.seq_intg(ret4),lb.seq_intg(ret5),lb.seq_intg(ret6)

    #根據買賣力x量x價的加權平均得出真正主力或散戶成本，用以作為策略的進出依據
    def GetPowerCost(self,Mb,Ms,P,V):
        dMb=lb.seq_diff(self.get(Mb))
        dMs=lb.seq_diff(self.get(Ms))
        dV=lb.seq_diff(V)
        PMb=np.zeros(len(P)) ; SumMb=np.zeros(len(P))
        PMs=np.zeros(len(P)) ; SumMs=np.zeros(len(P))
        PMb[0]=P[0]
        PMs[0]=P[0]
        for i in range(1,len(P)):
            Power=dMb[i]*dV[i]
            SumMb[i]=Power+SumMb[i-1]
            if SumMb[i]==0:
                PMb[i]=PMb[i-1]
            else:
                PMb[i]=((PMb[i-1]*SumMb[i-1])+(Power*P[i]))/SumMb[i]
            Power=dMs[i]*dV[i]
            SumMs[i]=Power+SumMs[i-1]
            if SumMs[i]==0:
                PMs[i]=PMs[i-1]
            else:
                PMs[i]=((PMs[i-1]*SumMs[i-1])+(Power*P[i]))/SumMs[i]
        return PMb,PMs
#'''

'''
#INPUT: 統計長度 , 買成筆 , 賣成筆 , 成交口 , 軍口搜尋範圍(上限,下限)
#OUTPUT: 最優上下限
def GetWinLoseDoPower(indi,start,stop,n1,n2,v1,rmax,rmin):
    step=1
    TXI=indi.get(u"指數波動")
    winner=[]
    loser=[]
    corr_loser=1
    corr_winner=-1
    for ii in range(rmax,rmin,-step):
        for jj in range(rmin,ii,step):
            rh=float(ii)/10
            rl=float(jj)/10
            corr=np.corrcoef(TXI[start:stop],indi.GetPureDoPower(start,stop,n1,n2,v1,rh,rl))[0][1]
            if corr>corr_winner: 
                winner=[rh,rl]
                corr_winner=corr
            if corr<corr_loser: 
                loser=[rh,rl]
                corr_loser=corr
               
    if abs(winner[0]-winner[1])<0.7 or abs(corr_winner)<0.9:
        winner=[0,0]
        corr_winner=0
    if abs(loser[0]-loser[1])<0.7 or abs(corr_loser)<0.9:
        loser=[0,0]
        corr_loser=0
        
    return winner , loser , [corr_winner,corr_loser]    
#'''


'''
def GetOLDIndicator(indi):
    #import os
    #exec(open(os.path.split(os.path.realpath(__file__))[0]+'\\indi\\init.py').read())
    
    ########################################################################################################        
    # 2.2 , 1.9 最佳參數
    # 純大台主力企圖 -698 純大台散戶企圖 -510
    a,b,c,d,e=indi.GetWantPower("大台委買口","大台委賣口","大台委買筆","大台委賣筆",2.2,1.9,energy=0)
    indi.add(u"大台未純化主力企圖",a) 
    indi.add(u"大台純主力買企圖",b) 
    indi.add(u"大台純主力賣企圖",c) 
    indi.add(u"大台純散戶買企圖",d) 
    indi.add(u"大台純散戶賣企圖",e) 

    
#    a,b,c,d,e=indi.GetWantPower("大台委買口","大台委賣口","大台委買筆","大台委賣筆",2.2,1.9,energy=1)
#    indi.add(u"大台未純化主力企圖動能",a) 
#    indi.add(u"大台純主力買企圖動能",b) 
#    indi.add(u"大台純主力賣企圖動能",c) 
#    indi.add(u"大台純散戶買企圖動能",d) 
#    indi.add(u"大台純散戶賣企圖動能",e) 

    ########################################################################################################    
    # 1.9 , 1.9 最佳參數
    # 純大台主力作為 +399 純大台散戶作為 +771
    e,f,g,h,i,j=indi.GetDoPower("大台買成筆","大台賣成筆","大台成交量",1.9,1.9,energy=0)
    indi.add(u"大台未純化主力買作為",e) 
    indi.add(u"大台未純化主力賣作為",f) 
    indi.add(u"大台未純化主力作為",(e-f)) 
    indi.add(u"大台純主力買作為",g) 
    indi.add(u"大台純主力賣作為",h) 
    indi.add(u"大台純散戶買作為",i) 
    indi.add(u"大台純散戶賣作為",j) 
    
    e,f,g,h,i,j=indi.GetDoPower("大台買成筆","大台賣成筆","大台成交量",1.1,1.9,energy=0)
    indi.add(u"大台未純化主力買作為N",e) 
    indi.add(u"大台未純化主力賣作為N",f) 
    indi.add(u"大台未純化主力作為N",(e-f))
    indi.add(u"大台純主力買作為N",g) 
    indi.add(u"大台純主力賣作為N",h) 
    indi.add(u"大台純散戶買作為N",i) 
    indi.add(u"大台純散戶賣作為N",j) 
    
    e,f,g,h,i,j=indi.GetDoPower("大台買成筆","大台賣成筆","大台成交量",2.5,1.9,energy=0)
    indi.add(u"大台未純化主力買作為2016",e) 
    indi.add(u"大台未純化主力賣作為2016",f) 
    indi.add(u"大台未純化主力作為2016",(e-f))
    indi.add(u"大台純主力買作為2016",g) 
    indi.add(u"大台純主力賣作為2016",h) 
    indi.add(u"大台純散戶買作為2016",i) 
    indi.add(u"大台純散戶賣作為2016",j) 
    
#   f,g,h,i,j=indi.GetDoPower("大台買成筆","大台賣成筆","大台成交量",1.9,1.9,energy=1)
#   indi.add(u"大台未純化主力作為動能",f) 
#   indi.add(u"大台純主力買作為動能",g) 
#   indi.add(u"大台純主力賣作為動能",h) 
#   indi.add(u"大台純散戶買作為動能",i) 
#   indi.add(u"大台純散戶賣作為動能",j)  
    ########################################################################################################
    # 1.9 , 1.2 最佳參數
    # 純小台主力企圖 +1122 純小台散戶企圖 -112
    v,w,x,y,z=indi.GetWantPower("小台委買口","小台委賣口","小台委買筆","小台委賣筆",1.9,1.2,energy=0)
    indi.add(u"小台未純化主力企圖",v) 
    indi.add(u"小台純主力買企圖",w) 
    indi.add(u"小台純主力賣企圖",x) 
    indi.add(u"小台純散戶買企圖",y) 
    indi.add(u"小台純散戶賣企圖",z) 


    v,w,x,y,z=indi.GetWantPower("小台委買口","小台委賣口","小台委買筆","小台委賣筆",1.9,1.2,energy=0)
    indi.add(u"小台未純化主力企圖2016",v) 
    indi.add(u"小台純主力買企圖2016",w) 
    indi.add(u"小台純主力賣企圖2016",x) 
    indi.add(u"小台純散戶買企圖2016",y) 
    indi.add(u"小台純散戶賣企圖2016",z) 

#   v,w,x,y,z=indi.GetWantPower("小台委買口","小台委賣口","小台委買筆","小台委賣筆",1.9,1.2,energy=1)
#   indi.add(u"小台未純化主力企圖動能",v) 
#   indi.add(u"小台純主力買企圖動能",w) 
#   indi.add(u"小台純主力賣企圖動能",x) 
#   indi.add(u"小台純散戶買企圖動能",y) 
#   indi.add(u"小台純散戶賣企圖動能",z)   
    ########################################################################################################
    # 1.9 , 1.4 2015最佳參數
    # 純小台主力作為 +1754 純小台散戶作為 +804
    
    e,f,g,h,i,j=indi.GetDoPower("小台買成筆","小台賣成筆","小台成交量",1.9,1.4,energy=0)
    indi.add(u"小台未純化主力買作為",e) 
    indi.add(u"小台未純化主力賣作為",f) 
    indi.add(u"小台未純化主力作為",(e-f))
    indi.add(u"小台純主力買作為",g) 
    indi.add(u"小台純主力賣作為",h) 
    indi.add(u"小台純散戶買作為",i) 
    indi.add(u"小台純散戶賣作為",j) 
    

    #e,f,g,h,i,j=indi.GetDoPowerEx("小台買成筆","小台賣成筆","小台成交量",1.5,1.4,1.5,0)
    #indi.add(u"小台未純化主力買作為",e) 
    #indi.add(u"小台未純化主力賣作為",f) 
    #indi.add(u"小台未純化主力作為",(e-f))
    #indi.add(u"小台純主力買作為",g) 
    #indi.add(u"小台純主力賣作為",h)
    #indi.add(u"小台純主力作為",(g-h)) 
    #indi.add(u"小台純散戶買作為",i) 
    #indi.add(u"小台純散戶賣作為",j)
    #indi.add(u"小台純散戶作為",(i-j)) 


    e,f,g,h,i,j=indi.GetDoPower("小台買成筆","小台賣成筆","小台成交量",1.3,1.2,energy=0)
    indi.add(u"小台未純化主力買作為2016",e) 
    indi.add(u"小台未純化主力賣作為2016",f) 
    indi.add(u"小台未純化主力作為2016",(e-f))
    indi.add(u"小台純主力買作為2016",g) 
    indi.add(u"小台純主力賣作為2016",h) 
    indi.add(u"小台純散戶買作為2016",i) 
    indi.add(u"小台純散戶賣作為2016",j) 

#   f,g,h,i,j=indi.GetDoPower("小台買成筆","小台賣成筆","小台成交量",1.9,1.4,energy=1)
#   indi.add(u"小台未純化主力作為動能",f) 
#   indi.add(u"小台純主力買作為動能",g) 
#   indi.add(u"小台純主力賣作為動能",h) 
#   indi.add(u"小台純散戶買作為動能",i) 
#   indi.add(u"小台純散戶賣作為動能",j)
    ########################################################################################################
    a,b=indi.GetPowerCost(u"小台純主力買作為",u"小台純主力賣作為",indi.get("小台指數"),indi.get("小台成交量"))
    indi.add(u"小台主力買作為價",a)
    indi.add(u"小台主力賣作為價",b) 
    a,b=indi.GetPowerCost(u"小台純散戶買作為",u"小台純散戶賣作為",indi.get("小台指數"),indi.get("小台成交量"))
    indi.add(u"小台散戶買作為價",a)
    indi.add(u"小台散戶賣作為價",b)

    a,b=indi.GetPowerCost(u"大台純主力買作為",u"大台純主力賣作為",indi.get("大台指數"),indi.get("大台成交量"))
    indi.add(u"大台主力買作為價",a)
    indi.add(u"大台主力賣作為價",b) 
    a,b=indi.GetPowerCost(u"大台純散戶買作為",u"大台純散戶賣作為",indi.get("大台指數"),indi.get("大台成交量"))
    indi.add(u"大台散戶買作為價",a)
    indi.add(u"大台散戶賣作為價",b)    

    a,b=indi.GetPowerCost(u"大台未純化主力買作為",u"大台未純化主力賣作為",indi.get("大台指數"),indi.get("大台成交量"))
    indi.add(u"大台未純化主力買作為價",a)
    indi.add(u"大台未純化主力賣作為價",b)      
    a,b=indi.GetPowerCost(u"小台未純化主力買作為",u"小台未純化主力賣作為",indi.get("小台指數"),indi.get("小台成交量"))
    indi.add(u"小台未純化主力買作為價",a)
    indi.add(u"小台未純化主力賣作為價",b)        
    ########################################################################################################    
    indi.add(u"慢市小台未純化主力企圖",indi.LowPassFilter("小台未純化主力企圖",5)) #已使用
    indi.add(u"慢市小台未純化主力作為",indi.LowPassFilter("小台未純化主力作為",5)) #已使用

    #indi.add(u"慢市小台純主力買企圖",indi.LowPassFilter("小台純主力買企圖",5))  #待用
    #indi.add(u"慢市小台純主力賣企圖",indi.LowPassFilter("小台純主力賣企圖",5))  #待用
    #indi.add(u"慢市小台純主力買作為",indi.LowPassFilter("小台純主力買作為",5))  #待用
    #indi.add(u"慢市小台純主力賣作為",indi.LowPassFilter("小台純主力賣作為",5))  #待用 

    indi.add(u"中市大台黑手",indi.LowPassFilter("大台黑手",800)) 
    indi.add(u"中市小台黑手",indi.LowPassFilter("小台黑手",800)) 

    indi.add(u"中市大台買賣差",indi.LowPassFilter("大台買賣差",1000)) 
    indi.add(u"中市小台買賣差",indi.LowPassFilter("小台買賣差",1000))      
    
    indi.add(u"中市大台未純化主力企圖",indi.LowPassFilter("大台未純化主力企圖",10)) #已使用
    indi.add(u"中市小台未純化主力企圖",indi.LowPassFilter("小台未純化主力企圖",10)) #已使用
    indi.add(u"中市大台未純化主力作為",indi.LowPassFilter("大台未純化主力作為",10)) #待用
    indi.add(u"中市小台未純化主力作為",indi.LowPassFilter("小台未純化主力作為",10)) #待用   
    
    indi.add(u"中市大台純主力買企圖",indi.LowPassFilter("大台純主力買企圖",10))  #已使用
    indi.add(u"中市大台純主力賣企圖",indi.LowPassFilter("大台純主力賣企圖",10))  #已使用
    indi.add(u"中市大台純主力買作為",indi.LowPassFilter("大台純主力買作為",10))  #待用
    indi.add(u"中市大台純主力賣作為",indi.LowPassFilter("大台純主力賣作為",10))  #待用 
    
    indi.add(u"中市小台純主力買企圖",indi.LowPassFilter("小台純主力買企圖",10))  #已使用
    indi.add(u"中市小台純主力賣企圖",indi.LowPassFilter("小台純主力賣企圖",10))  #已使用
    indi.add(u"中市小台純主力買作為",indi.LowPassFilter("小台純主力買作為",10))  #待用
    indi.add(u"中市小台純主力賣作為",indi.LowPassFilter("小台純主力賣作為",10))  #待用 
    
    
    
    ########################################################################################################  
    v,w,x,y,z=indi.GetWantPower("金期委買口","金期委賣口","金期委買筆","金期委賣筆",2.2,1.9)
    indi.add(u"金期未純化主力企圖",v) 
    indi.add(u"金期純主力買企圖",w) 
    indi.add(u"金期純主力賣企圖",x) 
    indi.add(u"金期純主力企圖",(w-x))
    indi.add(u"金期純散戶買企圖",y) 
    indi.add(u"金期純散戶賣企圖",z) 
    indi.add(u"金期純散戶企圖",(y-z))

    e,f,g,h,i,j=indi.GetDoPowerEx("金期買成筆","金期賣成筆","金期成交量",1.5,1.4,1.3,1.2)
    indi.add(u"金期未純化主力作為",(e-f)) 
    indi.add(u"金期純主力買作為",g) 
    indi.add(u"金期純主力賣作為",h) 
    indi.add(u"金期純主力作為",(g-h)) 
    indi.add(u"金期純散戶買作為",i) 
    indi.add(u"金期純散戶賣作為",j) 
    indi.add(u"金期純散戶作為",(i-j)) 
      
    ########################################################################################################  
    v,w,x,y,z=indi.GetWantPower("電期委買口","電期委賣口","電期委買筆","電期委賣筆",3,1.9)
    indi.add(u"電期未純化主力企圖",v) 
    indi.add(u"電期純主力買企圖",w) 
    indi.add(u"電期純主力賣企圖",x) 
    indi.add(u"電期純主力企圖",(w-x))
    indi.add(u"電期純散戶買企圖",y) 
    indi.add(u"電期純散戶賣企圖",z) 
    indi.add(u"電期純散戶企圖",(y-z))

    e,f,g,h,i,j=indi.GetDoPower("電期買成筆","電期賣成筆","電期成交量",1.3,1.9)
    indi.add(u"電期未純化主力作為",(e-f)) 
    indi.add(u"電期純主力買作為",g) 
    indi.add(u"電期純主力賣作為",h) 
    indi.add(u"電期純主力作為",(g-h)) 
    indi.add(u"電期純散戶買作為",i) 
    indi.add(u"電期純散戶賣作為",j) 
    indi.add(u"電期純散戶作為",(i-j)) 
'''