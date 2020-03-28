# -*- coding: utf-8 -*-
import sys,imp
import datetime
import lib.dblib as dl;             imp.reload(dl);
import lib.indicator as indl;       imp.reload(indl);
import lib.strategy_lib as sl;      imp.reload(sl);
import numpy as np

sys.path.append("..") 

DateCount=800
init_start=1 #30   //延遲下單的策略才要調 30 否則調 1
#########################################

def getOpenVolABS(data,count,start=1):
    vol=0
    if len(data)<start+count:
        return 0
    if start==1: 
        ended=count
    else:
        ended=start+count
    for i in range(start,ended):
        vol+=abs(data[i-1])
    return vol

def getWeekDay(d):
    #c = datetime.datetime.strptime('Sep-21-09 16:34','%b-%d-%y %H:%M')
    date=datetime.datetime.strptime(d, "%y/%m/%d")
    return date.weekday()+1
    # 1~7 =週一 ~ 週日
    
def getMonthDay(d):
    date=datetime.datetime.strptime(d, "%y/%m/%d")
    return date.day
    
def getTotalFilterData(D,II):
    indl.GetIndicatorByType(II,"大台未純化大單作為")
    indl.GetIndicatorByType(II,"大台未純化大單企圖")
    indl.GetIndicatorByType(II,"小台未純化大單作為")
    indl.GetIndicatorByType(II,"小台未純化大單企圖")
    indl.GetIndicatorByType(II,"金期未純化大單作為")
    indl.GetIndicatorByType(II,"金期未純化大單企圖")
    indl.GetIndicatorByType(II,"電期未純化大單作為")
    indl.GetIndicatorByType(II,"電期未純化大單企圖")
    
    
    HiLoLength=max(II.get("大台高點"))-min(II.get("大台低點"))
    KLength=abs(II.get("大台指數")[len(II.get("大台指數"))-1]-II.get("大台指數")[0])
    ShadowLength=HiLoLength-KLength
    Z=0
    
    F=getMonthDay(D)
    G=getWeekDay(D) 
    H=getOpenVolABS(II.get("大台成交量"),15,start=init_start) 
    I=getOpenVolABS(II.get("大台主力"),15,start=init_start)
    J=getOpenVolABS(II.get("大台散戶"),15,start=init_start)    
    K=getOpenVolABS(II.get("大台黑手"),15,start=init_start) 
    L=getOpenVolABS(II.get("大台未純化大單企圖"),15,start=init_start)
    M=getOpenVolABS(II.get("大台未純化大單作為"),15,start=init_start)
#    N=getOpenVolABS(II.get("大台純主力買企圖")-II.get("大台純主力賣企圖"),15,start=init_start)
#    O=getOpenVolABS(II.get("大台純主力買作為")-II.get("大台純主力賣作為"),15,start=init_start)
#    P=getOpenVolABS(II.get("大台純散戶買企圖")-II.get("大台純散戶賣企圖"),15,start=init_start)
#    Q=getOpenVolABS(II.get("大台純散戶買作為")-II.get("大台純散戶賣作為"),15,start=init_start)
    
    R=getOpenVolABS(II.get("小台成交量"),15,start=init_start)
    S=getOpenVolABS(II.get("小台主力"),15,start=init_start)
    T=getOpenVolABS(II.get("小台散戶"),15,start=init_start)
    U=getOpenVolABS(II.get("小台黑手"),15,start=init_start)
    V=getOpenVolABS(II.get("小台未純化大單企圖"),15,start=init_start)
    W=getOpenVolABS(II.get("小台未純化大單作為"),15,start=init_start)
#    X=getOpenVolABS(II.get("小台純主力買企圖")-II.get("小台純主力賣企圖"),15,start=init_start)
#    Y=getOpenVolABS(II.get("小台純主力買作為")-II.get("小台純主力賣作為"),15,start=init_start)
#    Z=getOpenVolABS(II.get("小台純散戶買企圖")-II.get("小台純散戶賣企圖"),15,start=init_start)
#    AA=getOpenVolABS(II.get("小台純散戶買作為")-II.get("小台純散戶賣作為"),15,start=init_start)

    AB=getOpenVolABS(II.get("電期成交量"),15,start=init_start)
    AC=getOpenVolABS(II.get("電期主力"),15,start=init_start)
    AD=getOpenVolABS(II.get("電期散戶"),15,start=init_start)
    AE=getOpenVolABS(II.get("電期黑手"),15,start=init_start)
    AF=getOpenVolABS(II.get("電期未純化大單企圖"),15,start=init_start)
    AG=getOpenVolABS(II.get("電期未純化大單作為"),15,start=init_start)
#    AH=getOpenVolABS(II.get("電期純主力買企圖")-II.get("電期純主力賣企圖"),15,start=init_start)
#    AI=getOpenVolABS(II.get("電期純主力買作為")-II.get("電期純主力賣作為"),15,start=init_start)
#    AJ=getOpenVolABS(II.get("電期純散戶買企圖")-II.get("電期純散戶賣企圖"),15,start=init_start)
#    AK=getOpenVolABS(II.get("電期純散戶買作為")-II.get("電期純散戶賣作為"),15,start=init_start)

    AL=getOpenVolABS(II.get("金期成交量"),15,start=init_start)
    AM=getOpenVolABS(II.get("金期主力"),15,start=init_start)
    AN=getOpenVolABS(II.get("金期散戶"),15,start=init_start)
    AO=getOpenVolABS(II.get("金期黑手"),15,start=init_start)
    AP=getOpenVolABS(II.get("金期未純化大單企圖"),15,start=init_start)
    AQ=getOpenVolABS(II.get("金期未純化大單作為"),15,start=init_start)
#    AR=getOpenVolABS(II.get("金期純主力買企圖")-II.get("金期純主力賣企圖"),15,start=init_start)
#    AS=getOpenVolABS(II.get("金期純主力買作為")-II.get("金期純主力賣作為"),15,start=init_start)
#    AT=getOpenVolABS(II.get("金期純散戶買企圖")-II.get("金期純散戶賣企圖"),15,start=init_start)
#    AU=getOpenVolABS(II.get("金期純散戶買作為")-II.get("金期純散戶賣作為"),15,start=init_start)
    return (HiLoLength,KLength,ShadowLength,F,G,H,I,J,K,L,M,Z,Z,Z,Z,R,S,T,U,V,W,Z,Z,Z,Z,AB,AC,AD,AE,AF,AG,Z,Z,Z,Z,AL,AM,AN,AO,AP,AQ,Z,Z,Z,Z)


FilterData=[]
DayList=[]
if __name__ == '__main__':
    try:
        dbstr= db.connstr
    except:
        db = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
        td=dl.TradeData(db.conn)
    
    DaysStart=td.DateCount-DateCount
    for i in range(0,td.DateCount-DaysStart):
        indi=td.FetchDateByMem(td.DateList[i+DaysStart])
        a=indi.get("大台指數")
        #indi.GetBaseIndicator()
        indl.GetSpecialIndicator(indi)
        FilterData.append(getTotalFilterData(td.DateList[i+DaysStart],indi))
        DayList.append(td.DateList[i+DaysStart])
        
        #日,星期,大台開盤量,小台開盤量
            
    t=[u"震幅",u"K棒長",u"影線長",u"日",u"星期",u"大量",u"大主",u"大散",u"大黑",u"大未主企",u"大未主作",u"大純主企",u"大純主作",u"大純散企",u"大純散作",u"小量",u"小主",u"小散",u"小黑",u"小未主企",u"小未主作",u"小純主企",u"小純主作",u"小純散企",u"小純散作",u"電量",u"電主",u"電散",u"電黑",u"電未主企",u"電未主作",u"電純主企",u"電純主作",u"電純散企",u"電純散作",u"金量",u"金主",u"金散",u"金黑",u"金未主企",u"金未主作",u"金純主企",u"金純主作",u"金純散企",u"金純散作"]
    d=DayList
    a=np.array(FilterData)
    




    
'''
    HiLoLength=max(II.get("大台高點"))-min(II.get("大台低點"))
    KLength=abs(II.get("大台指數")[len(II.get("大台指數"))-1]-II.get("大台指數")[0])
    ShadowLength=HiLoLength-KLength
      
    F=getMonthDay(D)
    G=getWeekDay(D)
    
    H=getOpenVolABS(II.get("大台成交量"),15,start=init_start)
    I=getOpenVolABS(II.get("大台主力"),15,start=init_start)
    J=getOpenVolABS(II.get("大台散戶"),15,start=init_start)    
    K=getOpenVolABS(II.get("大台黑手"),15,start=init_start)
    L=getOpenVolABS(II.get("大台未純化主力企圖"),15,start=init_start)
    M=getOpenVolABS(II.get("大台未純化主力作為"),15,start=init_start)
    N=getOpenVolABS(II.get("大台純主力買企圖")-II.get("大台純主力賣企圖"),15,start=init_start)
    O=getOpenVolABS(II.get("大台純主力買作為")-II.get("大台純主力賣作為"),15,start=init_start)
    P=getOpenVolABS(II.get("大台純散戶買企圖")-II.get("大台純散戶賣企圖"),15,start=init_start)
    Q=getOpenVolABS(II.get("大台純散戶買作為")-II.get("大台純散戶賣作為"),15,start=init_start)

    R=getOpenVolABS(II.get("小台成交量"),15,start=init_start)
    S=getOpenVolABS(II.get("小台主力"),15,start=init_start)
    T=getOpenVolABS(II.get("小台散戶"),15,start=init_start)
    U=getOpenVolABS(II.get("小台黑手"),15,start=init_start)
    V=getOpenVolABS(II.get("小台未純化主力企圖"),15,start=init_start)
    W=getOpenVolABS(II.get("小台未純化主力作為"),15,start=init_start)
    X=getOpenVolABS(II.get("小台純主力買企圖")-II.get("小台純主力賣企圖"),15,start=init_start)
    Y=getOpenVolABS(II.get("小台純主力買作為")-II.get("小台純主力賣作為"),15,start=init_start)
    Z=getOpenVolABS(II.get("小台純散戶買企圖")-II.get("小台純散戶賣企圖"),15,start=init_start)
    AA=getOpenVolABS(II.get("小台純散戶買作為")-II.get("小台純散戶賣作為"),15,start=init_start)

    AB=getOpenVolABS(II.get("電期成交量"),15,start=init_start)
    AC=getOpenVolABS(II.get("電期主力"),15,start=init_start)
    AD=getOpenVolABS(II.get("電期散戶"),15,start=init_start)
    AE=getOpenVolABS(II.get("電期黑手"),15,start=init_start)
    AF=getOpenVolABS(II.get("電期未純化主力企圖"),15,start=init_start)
    AG=getOpenVolABS(II.get("電期未純化主力作為"),15,start=init_start)
    AH=getOpenVolABS(II.get("電期純主力買企圖")-II.get("電期純主力賣企圖"),15,start=init_start)
    AI=getOpenVolABS(II.get("電期純主力買作為")-II.get("電期純主力賣作為"),15,start=init_start)
    AJ=getOpenVolABS(II.get("電期純散戶買企圖")-II.get("電期純散戶賣企圖"),15,start=init_start)
    AK=getOpenVolABS(II.get("電期純散戶買作為")-II.get("電期純散戶賣作為"),15,start=init_start)
    
    AL=getOpenVolABS(II.get("金期成交量"),15,start=init_start)
    AM=getOpenVolABS(II.get("金期主力"),15,start=init_start)
    AN=getOpenVolABS(II.get("金期散戶"),15,start=init_start)
    AO=getOpenVolABS(II.get("金期黑手"),15,start=init_start)
    AP=getOpenVolABS(II.get("金期未純化主力企圖"),15,start=init_start)
    AQ=getOpenVolABS(II.get("金期未純化主力作為"),15,start=init_start)
    AR=getOpenVolABS(II.get("金期純主力買企圖")-II.get("金期純主力賣企圖"),15,start=init_start)
    AS=getOpenVolABS(II.get("金期純主力買作為")-II.get("金期純主力賣作為"),15,start=init_start)
    AT=getOpenVolABS(II.get("金期純散戶買企圖")-II.get("金期純散戶賣企圖"),15,start=init_start)
    AU=getOpenVolABS(II.get("金期純散戶買作為")-II.get("金期純散戶賣作為"),15,start=init_start)
  
    return (HiLoLength,KLength,ShadowLength,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AF,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS,AT,AU)
'''