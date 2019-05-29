# -*- coding: utf-8 -*-

import sys   
sys.path.append("..") 

import lib.dblib as dl
import lib.indicator as il
import lib.strategy_lib as sl
import lib.tracking as tl
import lib.analytics as an

import numpy as np
import pylab as pl
import scipy as sc
import matplotlib.pyplot as plt






dbt = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
tdt=dl.TradeData(dbt.conn)
dayindi=il.indicatorGroup()


#dayindi=tdt.FetchDateByDB("15/07/03")   #要想辦法賺兩趟
#dayindi=tdt.FetchDateByDB("15/07/09")
#dayindi=tdt.FetchDateByDB("15/07/13")
#dayindi=tdt.FetchDateByDB("15/08/11")
#dayindi=tdt.FetchDateByDB("15/03/26")  #史上賠最慘的一天
#dayindi=tdt.FetchDateByDB("16/01/28")  #該做多但籌碼卻偏空的一天
#dayindi=tdt.FetchDateByDB("16/01/22")  #開盤跌80點到11:30後漲了100點 (要想辦法賺兩趟)
#dayindi=tdt.FetchDateByDB("16/02/26")  #要想辦法賺兩趟
#dayindi=tdt.FetchDateByDB("16/03/09")  #要想辦法賺兩趟
#dayindi=tdt.FetchDateByDB("16/03/10")  #擴張型走勢，要賺逆勢

#dayindi=tdt.FetchDateByDB("16/04/19")  #一分鐘殺90點..要觀察跡象
#dayindi=tdt.FetchDateByDB("16/04/22")   #擴張型走勢，要賺逆勢
#dayindi=tdt.FetchDateByDB("16/05/09")   #頭重腳輕造成中傷
#dayindi=tdt.FetchDateByDB("16/05/10")  #頭重腳輕造成重傷
dayindi=tdt.FetchDateByDB("16/05/20")  #擴張型亂刷造成重傷
#dayindi=tdt.FetchDateByDB("16/06/06")  #擴張型+S走勢造成重傷
#dayindi=tdt.FetchDateByDB("16/05/23")   #被刷後大賺
il.GetSpecialIndicator(dayindi)

#plt.plot(dayindi.get(u"大台指數"),"g")

#plt.plot(-dayindi.get(u"大台散戶"),"r")
#plt.plot(dayindi.get(u"大台黑手"),"g")
#plt.plot(-dayindi.get(u"小台散戶"),"y")



#plt.plot(dayindi.get(u"慢市金期買賣差"),"r")
#plt.plot(dayindi.get(u"慢市電期買賣差"),"g")

#baseT= 120
#base1= dayindi.get("大台未純化主力企圖")[baseT]
#base2= dayindi.get("小台未純化主力企圖")[baseT]

#plt.plot(dayindi.get(u"大台未純化主力企圖")-base1,"y")
#plt.plot(dayindi.get(u"小台未純化主力企圖")-base2,"c")
#plt.plot(dayindi.get(u"金期未純化主力企圖"),"r")
#plt.plot(dayindi.get(u"電期未純化主力企圖"),"g")


#plt.plot(dayindi.get(u"小台未純化主力企圖"),"c")
#plt.plot(dayindi.get(u"小台未純化主力企圖動能"),"b")

#plt.plot(dayindi.get(u"小台未純化主力作為"),"r")
#plt.plot(dayindi.get(u"小台未純化主力作為動能"),"g")

'''
plt.plot(dayindi.get(u"小台未純化主力作為"),"r")
plt.plot(dayindi.get("電期未純化主力作為"),"g")
plt.plot(dayindi.get("金期未純化主力作為"),"b")
avg=np.mean([dayindi.get(u"小台未純化主力作為"),dayindi.get("金期未純化主力作為"),dayindi.get("電期未純化主力作為")],axis=0)
plt.plot(avg,"y")
'''
'''
plt.plot(dayindi.get(u"慢市大台黑手"),"r")
plt.plot(dayindi.get(u"慢市小台黑手"),"g")

plt.plot(dayindi.get(u"中市大台黑手"),"b")
plt.plot(dayindi.get(u"中市小台黑手"),"y")
'''
#plt.plot(dayindi.get(u"大台未純化主力作為"),"r")
#plt.plot(dayindi.get(u"小台未純化主力作為"),"g")

#plt.plot(dayindi.get(u"大台黑手"),"g")
#plt.plot(dayindi.get(u"小台黑手"),"r")

#plt.plot(dayindi.get(u"中市大台未純化主力企圖")-dayindi.get(u"中市小台未純化主力企圖"),"r")
#plt.plot(dayindi.get(u"中市小台未純化主力企圖"),"g")

#plt.plot(dayindi.get(u"慢市大台散戶"),"r")
#plt.plot(dayindi.get(u"慢市小台散戶"),"g")

#plt.plot(dayindi.get(u"小台黑手"),"g")

#plt.plot(dayindi.get(u"大台純主力買企圖N")-dayindi.get(u"大台純主力賣企圖N"),"r")
#plt.plot(dayindi.get(u"大台純主力買企圖")-dayindi.get(u"大台純主力賣企圖"),"g")
#plt.plot(dayindi.get(u"大台純散戶買企圖")-dayindi.get(u"大台純散戶賣企圖"),"c")
#plt.plot(dayindi.get(u"小台純主力買企圖")-dayindi.get(u"小台純主力賣企圖"),"g")
#plt.plot(dayindi.get(u"小台純散戶買企圖")-dayindi.get(u"小台純散戶賣企圖"),"y")

#plt.plot(dayindi.get(u"大台純主力買作為N")-dayindi.get(u"大台純主力賣作為N"),"r")
#plt.plot(dayindi.get(u"大台純主力買作為")-dayindi.get(u"大台純主力賣作為"),"g")
#plt.plot(dayindi.get(u"大台純散戶買作為")-dayindi.get(u"大台純散戶賣作為"),"c")
#plt.plot(dayindi.get(u"小台純主力買作為")-dayindi.get(u"小台純主力賣作為"),"g")
#plt.plot(dayindi.get(u"小台純散戶買作為")-dayindi.get(u"小台純散戶賣作為"),"y")

#plt.plot(dayindi.get(u"上漲家數"),"y")
#plt.plot(dayindi.get(u"下跌家數"),"g")
#plt.plot(dayindi.get(u"平盤家數"),"b")

#plt.plot(dayindi.get(u"慢市小台未純化主力企圖"),"r")
#plt.plot(dayindi.get(u"小台未純化主力企圖"),"g")

#plt.plot(dayindi.get(u"小台買賣差"),"g")
#plt.plot(dayindi.get(u"慢市小台買賣差"),"r")
#plt.plot(dayindi.get(u"慢市大台買賣差"),"g")

#plt.plot(dayindi.get(u"小台黑手"),"g")
#plt.plot(dayindi.get(u"慢市小台黑手"),"r")

#plt.plot(dayindi.get(u"慢市上漲家數變動"),"r")
#plt.plot(dayindi.get(u"慢市下跌家數變動"),"g")

#plt.plot(dayindi.get(u"大台黑手")+dayindi.get(u"小台黑手"),"r")
#plt.plot(-dayindi.get(u"大台散戶")-dayindi.get(u"小台散戶"),"g")

plt.plot(dayindi.get(u"大台黑手"),"r")
#plt.plot(dayindi.get(u"小台黑手"),"g")
#plt.plot(-dayindi.get(u"小台散戶"),"g")

plt.plot(-dayindi.get(u"大台散戶"),"g")
#plt.plot(-dayindi.get(u"小台散戶"),"g")



plt.show()
plt.plot(dayindi.get(u"指數波動"),"b")
plt.plot(dayindi.get(u"現期價差"),"r")
plt.show()




