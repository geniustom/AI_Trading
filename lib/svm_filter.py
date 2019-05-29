# -*- coding: utf-8 -*-
import sys
import datetime
import dblib as dl;             reload(dl);
import indicator as indl;       reload(indl);
import strategy_lib as sl;      reload(sl);
import numpy as np

sys.path.append("..") 

DateCount=476
init_start=1 #30   //延遲下單的策略才要調 30 否則調 1
init_step=15

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
    
#########################################

FilterData=[]
DayList=[]
if __name__ == '__main__':
    try:
        dbstr= db.connstr
    except:
        db = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
        td=dl.TradeData(db.conn)
    
    DaysStart=td.DateCount-DateCount
    x=init_start
    y=init_step
    for i in range(0,td.DateCount-DaysStart):
        indi=td.FetchDateByMem(td.DateList[i+DaysStart])
        indl.GetSpecialIndicator(indi)

        Day=td.DateList[i+DaysStart]
        DayList.append(Day)

        TXVF=indi.get("大台成交量")[x:x+y]
        TXMainF=indi.get("大台主力")[x:x+y]
        TXBadF=indi.get("大台散戶")[x:x+y]
        TXDarkF=indi.get("大台黑手")[x:x+y]
        TXWantMainF=indi.get("大台純主力買企圖")[x:x+y]-indi.get("大台純主力賣企圖")[x:x+y]
        TXDoMainF=indi.get("大台純主力買作為")[x:x+y]-indi.get("大台純主力賣作為")[x:x+y]
        TXWantBadF=indi.get("大台純散戶買企圖")[x:x+y]-indi.get("大台純散戶賣企圖")[x:x+y]
        TXDoBadF=indi.get("大台純散戶買作為")[x:x+y]-indi.get("大台純散戶賣作為")[x:x+y]
        
        MTXVF=indi.get("小台成交量")[x:x+y]
        MTXMainF=indi.get("小台主力")[x:x+y]
        MTXBadF=indi.get("小台散戶")[x:x+y]
        MTXDarkF=indi.get("小台黑手")[x:x+y]
        MTXWantMainF=indi.get("小台純主力買企圖")[x:x+y]-indi.get("小台純主力賣企圖")[x:x+y]
        MTXDoMainF=indi.get("小台純主力買作為")[x:x+y]-indi.get("小台純主力賣作為")[x:x+y]
        MTXWantBadF=indi.get("小台純散戶買企圖")[x:x+y]-indi.get("小台純散戶賣企圖")[x:x+y]
        MTXDoBadF=indi.get("小台純散戶買作為")[x:x+y]-indi.get("小台純散戶賣作為")[x:x+y]
        
        #DataVector=np.concatenate((TXVF,TXMainF,TXBadF,TXDarkF,TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXVF,MTXMainF,MTXBadF,MTXDarkF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        #DataVector=np.concatenate((TXMainF,TXBadF,TXDarkF,TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXMainF,MTXBadF,MTXDarkF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        #DataVector=np.concatenate((TXMainF,TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXMainF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        DataVector=np.concatenate((TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        #DataVector=np.concatenate((TXVF,MTXVF))
        #DataVector=np.concatenate((TXVF,TXMainF,TXBadF,TXDarkF,MTXVF,MTXMainF,MTXBadF,MTXDarkF))
                            
        FilterData.append(DataVector)


    TrainDate=DayList
    TrainData=np.array(FilterData)
    
    
    
'''        
        TXVF=indi.get("大台成交量")[x:x+y]
        TXMainF=indi.get("大台主力")[x:x+y]
        TXBadF=indi.get("大台散戶")[x:x+y]
        TXDarkF=indi.get("大台黑手")[x:x+y]
        TXWantMainF=indi.get("大台純主力買企圖")[x:x+y]-indi.get("大台純主力賣企圖")[x:x+y]
        TXDoMainF=indi.get("大台純主力買作為")[x:x+y]-indi.get("大台純主力賣作為")[x:x+y]
        TXWantBadF=indi.get("大台純散戶買企圖")[x:x+y]-indi.get("大台純散戶賣企圖")[x:x+y]
        TXDoBadF=indi.get("大台純散戶買作為")[x:x+y]-indi.get("大台純散戶賣作為")[x:x+y]
        
        MTXVF=indi.get("小台成交量")[x:x+y]
        MTXMainF=indi.get("小台主力")[x:x+y]
        MTXBadF=indi.get("小台散戶")[x:x+y]
        MTXDarkF=indi.get("小台黑手")[x:x+y]
        MTXWantMainF=indi.get("小台純主力買企圖")[x:x+y]-indi.get("小台純主力賣企圖")[x:x+y]
        MTXDoMainF=indi.get("小台純主力買作為")[x:x+y]-indi.get("小台純主力賣作為")[x:x+y]
        MTXWantBadF=indi.get("小台純散戶買企圖")[x:x+y]-indi.get("小台純散戶賣企圖")[x:x+y]
        MTXDoBadF=indi.get("小台純散戶買作為")[x:x+y]-indi.get("小台純散戶賣作為")[x:x+y]
        
        #DataVector=np.concatenate((TXVF,TXMainF,TXBadF,TXDarkF,TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXVF,MTXMainF,MTXBadF,MTXDarkF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        #DataVector=np.concatenate((TXMainF,TXBadF,TXDarkF,TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXMainF,MTXBadF,MTXDarkF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        DataVector=np.concatenate((TXMainF,TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXMainF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        #DataVector=np.concatenate((TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))
        #DataVector=np.concatenate((TXVF,TXDoMainF))
'''

'''
        TXVF=getOpenVolABS(indi.get("大台成交量"),15,start=init_start)
        TXMainF=getOpenVolABS(indi.get("大台主力"),15,start=init_start)
        TXBadF=getOpenVolABS(indi.get("大台散戶"),15,start=init_start)
        TXDarkF=getOpenVolABS(indi.get("大台黑手"),15,start=init_start)
        TXWantMainF=getOpenVolABS(indi.get("大台純主力買企圖")-indi.get("大台純主力賣企圖"),15,start=init_start)
        TXDoMainF=getOpenVolABS(indi.get("大台純主力買作為")-indi.get("大台純主力賣作為"),15,start=init_start)
        TXWantBadF=getOpenVolABS(indi.get("大台純散戶買企圖")-indi.get("大台純散戶賣企圖"),15,start=init_start)
        TXDoBadF=getOpenVolABS(indi.get("大台純散戶買作為")-indi.get("大台純散戶賣作為"),15,start=init_start)
        
        MTXVF=getOpenVolABS(indi.get("小台成交量"),15,start=init_start)
        MTXMainF=getOpenVolABS(indi.get("小台主力"),15,start=init_start)
        MTXBadF=getOpenVolABS(indi.get("小台散戶"),15,start=init_start)
        MTXDarkF=getOpenVolABS(indi.get("小台黑手"),15,start=init_start)
        MTXWantMainF=getOpenVolABS(indi.get("小台純主力買企圖")-indi.get("小台純主力賣企圖"),15,start=init_start)
        MTXDoMainF=getOpenVolABS(indi.get("小台純主力買作為")-indi.get("小台純主力賣作為"),15,start=init_start)
        MTXWantBadF=getOpenVolABS(indi.get("小台純散戶買企圖")-indi.get("小台純散戶賣企圖"),15,start=init_start)
        MTXDoBadF=getOpenVolABS(indi.get("小台純散戶買作為")-indi.get("小台純散戶賣作為"),15,start=init_start)
        
        DataVector=np.array((TXVF,TXMainF,TXBadF,TXDarkF,TXWantMainF,TXDoMainF,TXWantBadF,TXDoBadF,MTXVF,MTXMainF,MTXBadF,MTXDarkF,MTXWantMainF,MTXDoMainF,MTXWantBadF,MTXDoBadF))

'''