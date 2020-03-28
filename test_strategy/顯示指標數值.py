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
dayindi=tdt.FetchDateByDB("16/01/22")  #開盤跌80點到11:30後漲了100點 (要想辦法賺兩趟)
#dayindi=tdt.FetchDateByDB("16/02/26")  #要想辦法賺兩趟
#dayindi=tdt.FetchDateByDB("16/03/09")  #要想辦法賺兩趟
#dayindi=tdt.FetchDateByDB("16/03/10")  #擴張型走勢，要賺逆勢

#dayindi=tdt.FetchDateByDB("16/04/19")  #一分鐘殺90點..要觀察跡象
#dayindi=tdt.FetchDateByDB("16/04/22")   #擴張型走勢，要賺逆勢
#dayindi=tdt.FetchDateByDB("16/05/09")   #頭重腳輕造成中傷
#dayindi=tdt.FetchDateByDB("16/05/10")  #頭重腳輕造成重傷
#dayindi=tdt.FetchDateByDB("16/05/11")   #頭重腳輕造成重傷
#dayindi=tdt.FetchDateByDB("16/05/20")  #擴張型亂刷造成重傷
#dayindi=tdt.FetchDateByDB("16/06/06")  #擴張型+S走勢造成重傷
#dayindi=tdt.FetchDateByDB("16/05/23")   #被刷後大賺
#dayindi=tdt.FetchDateByDB("16/06/22")   #被刷後大賺
#dayindi=tdt.FetchDateByDB("16/06/23")   #頭重腳輕造成重傷
#dayindi=tdt.FetchDateByDB("16/06/24")   #被重刷後大賺
#dayindi=tdt.FetchDateByDB("16/06/28")   #該做多但籌碼卻偏空的一天
#dayindi=tdt.FetchDateByDB("16/06/29")   #早盤拉高無任何跡象卻閃崩
#dayindi=tdt.FetchDateByDB("16/05/04")   #早盤大賺但尾盤要能停利
#dayindi=tdt.FetchDateByDB("16/07/21")   #明明一路上漲卻狂空
#dayindi=tdt.FetchDateByDB("16/08/04")   #應該要能賺2趟
#dayindi=tdt.FetchDateByDB("16/08/11")    #開低拉高大殺又拉高


il.GetSpecialIndicator(dayindi)
#=========================================================================
'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"指數波動"),"b")
plt.show()
'''

#print ("通道")
#ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
#plt.plot(dayindi.get(u"指數波動"),"b")
#ax=plt.subplot(212);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
#plt.plot(dayindi.get(u"小台純主力作為")-dayindi.get(u"小台純散戶作為"),"r")
#plt.plot(dayindi.get(u"小台未純化大單作為"),"b")
#plt.plot(dayindi.get(u"小台未純化大單作為高通道"),"r")
#plt.plot(dayindi.get(u"小台未純化大單作為低通道"),"g")
#plt.show()
#
#print ("小台贏家00")
#ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
#plt.plot(dayindi.get(u"指數波動"),"b")
#ax=plt.subplot(212);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
#il.GetIndicatorByType(dayindi,"小台贏家00")
#plt.plot(dayindi.get(u"小台贏家00"),"b")
#plt.plot(dayindi.get(u"小台贏家00高通道"),"r")
#plt.plot(dayindi.get(u"小台贏家00低通道"),"g")
#plt.show()

#plt.plot(dayindi.get(u"大台主力"),"b")
#plt.plot(dayindi.get(u"大台主力高通道"),"r")
#plt.plot(dayindi.get(u"大台主力低通道"),"g")
#plt.show()


#print ("大 主力/散戶")
#ax=plt.subplot(211);ax.yaxis.tick_right();
#plt.plot(dayindi.get(u"大台指數"),"b")
#plt.plot(dayindi.get(u"大台主力買作為價"),"r")
#plt.plot(dayindi.get(u"大台主力賣作為價"),"g")
#ax=plt.subplot(212);ax.yaxis.tick_right();
#plt.plot(dayindi.get(u"大台指數"),"b")
#plt.plot(dayindi.get(u"大台散戶買作為價"),"g")
#plt.plot(dayindi.get(u"大台散戶賣作為價"),"r")
#plt.show()

ax=plt.subplot(111);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"大台指數"),"b")
plt.show()
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
#plt.plot(dayindi.get(u"大台散戶")-dayindi.get(u"小台散戶"),"b")
plt.plot(dayindi.get(u"大台散戶"),"b")
plt.plot(dayindi.get(u"小台散戶"),"r")
ax=plt.subplot(212);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"大台黑手"),"b")
plt.plot(dayindi.get(u"小台黑手"),"r")
plt.show()
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
il.GetIndicatorByType(dayindi,"小台未純化大單作為")
il.GetIndicatorByType(dayindi,"小台未純化大單企圖")
plt.plot(dayindi.get("小台未純化大單作為"),"r")
plt.plot(dayindi.get("小台未純化大單企圖"),"b")
ax=plt.subplot(212);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot((dayindi.get("大台委買口")-dayindi.get("小台委買口"))-(dayindi.get("大台委賣口")-dayindi.get("小台委賣口")),"r")
plt.plot((dayindi.get("大台委買筆")-dayindi.get("小台委買筆"))-(dayindi.get("大台委賣筆")-dayindi.get("小台委賣筆")),"b")
#plt.plot(dayindi.get(u"上漲家數")-dayindi.get(u"下跌家數"),"r")

'''
print ("小 主力/散戶")
ax=plt.subplot(211);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台主力買作為價"),"r")
plt.plot(dayindi.get(u"小台主力賣作為價"),"g")
ax=plt.subplot(212);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台散戶買作為價"),"g")
plt.plot(dayindi.get(u"小台散戶賣作為價"),"r")
plt.show()
'''

#il.GetWinLoseDoPower(dayindi,0,15,"小台買成筆","小台賣成筆","小台成交量",30,0)

'''
print ("小台純 主力/散戶")
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"指數波動"),"b")
ax=plt.subplot(212);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
#plt.plot(dayindi.get(u"小台純主力作為")-dayindi.get(u"小台純散戶作為"),"r")
plt.plot(dayindi.get(u"小台純主力作為"),"r")
plt.plot(dayindi.get(u"小台純散戶作為"),"g")
plt.show()
'''

        
'''
print ("金期純 主力/散戶")
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"指數波動"),"b")
ax=plt.subplot(212);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"金期純主力作為"),"r")
plt.plot(dayindi.get(u"金期純散戶作為"),"g")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台未純化主力買作為價"),"r")
plt.plot(dayindi.get(u"小台未純化主力賣作為價"),"g")
plt.plot(dayindi.get(u"大台未純化主力買作為價"),"r")
plt.plot(dayindi.get(u"大台未純化主力賣作為價"),"g")
plt.show()
'''

'''
print ("主力買r,散戶賣g / 主力賣g,散戶買r")
ax=plt.subplot(211);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台主力買作為價"),"r")
plt.plot(dayindi.get(u"小台散戶賣作為價"),"g")
ax=plt.subplot(212);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台主力賣作為價"),"g")
plt.plot(dayindi.get(u"小台散戶買作為價"),"r")
plt.show()

print ("主力買r,散戶買g / 主力賣g,散戶賣r")
ax=plt.subplot(211);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台主力買作為價"),"r")
plt.plot(dayindi.get(u"小台散戶買作為價"),"g")
ax=plt.subplot(212);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台主力賣作為價"),"g")
plt.plot(dayindi.get(u"小台散戶賣作為價"),"r")
plt.show()

'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台主力買作為價"),"r")
plt.plot(dayindi.get(u"小台散戶買作為價"),"g")
ax=plt.subplot(212);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"小台指數"),"b")
plt.plot(dayindi.get(u"小台主力賣作為價"),"g")
plt.plot(dayindi.get(u"小台散戶賣作為價"),"r")
plt.show()
'''



'''
ax=plt.subplot(211);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"大台指數"),"b")
plt.plot(dayindi.get(u"大台主力賣作為價"),"g")
plt.plot(dayindi.get(u"大台散戶賣作為價"),"r")
ax=plt.subplot(212);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"大台指數"),"b")
plt.plot(dayindi.get(u"大台主力買作為價"),"r")
plt.plot(dayindi.get(u"大台散戶買作為價"),"g")
plt.show()


ax=plt.subplot(211);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"大台指數"),"b")
plt.plot(dayindi.get(u"大台主力買作為價"),"r")
plt.plot(dayindi.get(u"大台主力賣作為價"),"g")
ax=plt.subplot(212);ax.yaxis.tick_right();
plt.plot(dayindi.get(u"大台指數"),"b")
plt.plot(dayindi.get(u"大台散戶買作為價"),"g")
plt.plot(dayindi.get(u"大台散戶賣作為價"),"r")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
aa=dayindi.get(u"指數波動")
bb=dayindi.get(u"小台未純化主力企圖")
cc=dayindi.get(u"小台未純化主力作為")
plt.plot(bb,"g")
plt.plot(cc,"r")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
aa=dayindi.get(u"指數波動")
bb=dayindi.get(u"大台未純化主力企圖")
cc=dayindi.get(u"大台未純化主力作為")
plt.plot(bb,"g")
plt.plot(cc,"r")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get("大台買賣差"),"r")
plt.plot(dayindi.get("大台實掛單"),"g")
plt.show()
'''
'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get("小台買賣差"),"r")
plt.plot(dayindi.get("小台實掛單"),"g")
plt.show()
'''
'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get("大台委買口")-dayindi.get("大台五檔買累計"),"r")
plt.plot(dayindi.get("大台委賣口")-dayindi.get("大台五檔賣累計"),"g")
plt.show()
# 若走平代表高低點已出現..接下來是盤整
'''
'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get("大台實掛單"),"r")
plt.plot(dayindi.get("小台實掛單"),"g")
plt.show()
'''
'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get("小台委買口")-dayindi.get("小台五檔買累計"),"r")
plt.plot(dayindi.get("小台委賣口")-dayindi.get("小台五檔賣累計"),"g")
plt.show()
# 若走平代表高低點已出現..接下來是盤整
'''
'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(-dayindi.get(u"大台散戶"),"r")
plt.plot(-dayindi.get(u"小台散戶"),"g")
plt.plot(dayindi.get(u"大台黑手"),"b")
plt.plot(dayindi.get(u"小台黑手"),"y")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
#plt.plot(dayindi.get(u"大台黑手")+dayindi.get(u"小台黑手"),"r")
#plt.plot(-dayindi.get(u"大台散戶")-dayindi.get(u"小台散戶"),"g")
plt.plot(dayindi.get(u"大台黑手")+dayindi.get(u"小台黑手")-dayindi.get(u"大台散戶")-dayindi.get(u"小台散戶"),"g")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"小台未純化主力企圖"),"r")
plt.plot(dayindi.get("電期未純化主力企圖"),"g")
plt.plot(dayindi.get("金期未純化主力企圖"),"b")
plt.plot(dayindi.get(u"小台未純化主力企圖")/2+dayindi.get("電期未純化主力企圖")+dayindi.get("金期未純化主力企圖"),"k")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"小台未純化主力作為"),"r")
plt.plot(dayindi.get("電期未純化主力作為"),"g")
plt.plot(dayindi.get("金期未純化主力作為"),"b")
plt.plot(dayindi.get(u"小台未純化主力作為")/2+dayindi.get("電期未純化主力作為")+dayindi.get("金期未純化主力作為"),"k")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"小台未純化主力作為")-dayindi.get(u"小台未純化主力企圖"),"r")
plt.plot(dayindi.get("電期未純化主力作為")-dayindi.get(u"電期未純化主力企圖"),"g")
plt.plot(dayindi.get("金期未純化主力作為")-dayindi.get(u"金期未純化主力企圖"),"b")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"慢市大台黑手"),"r")
plt.plot(dayindi.get(u"慢市小台黑手"),"g")
plt.plot(dayindi.get(u"中市大台黑手"),"b")
plt.plot(dayindi.get(u"中市小台黑手"),"y")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"大台未純化主力企圖"),"r")
plt.plot(dayindi.get(u"小台未純化主力企圖"),"g")
plt.plot(dayindi.get(u"大台未純化主力作為"),"g")
plt.plot(dayindi.get(u"小台未純化主力作為"),"r")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
plt.plot(dayindi.get(u"現期價差"),"r")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
aa=dl.seq_diff(dayindi.get(u"指數波動"))
bb=dl.seq_diff(dayindi.get(u"小台未純化主力企圖"))
hh=[]
ll=[]
maxaa=0
minaa=0
for i in range(len(aa)):
    if aa[i]>maxaa:
        maxaa=aa[i]
    hh.append(maxaa)
for i in range(len(aa)):
    if aa[i]<minaa:
        minaa=aa[i]
    ll.append(minaa)
cc=dl.seq_intg((aa-ll)-(hh-aa))
#cc=aa/bb #dl.seq_intg((bb))
plt.plot(cc,"g")
plt.show()
'''

'''
ax=plt.subplot(211);ax.yaxis.tick_right();plt.plot(np.zeros(300),"m")
pp=dayindi.get(u"指數波動")
tt=dl.seq_diff(dayindi.get(u"小台未純化主力企圖"))
rr=[]
for i in range (1,len(pp)):
    if pp[i-1]==0:
        rr.append(0)
    else:
        rr.append((pp[i]-pp[i-1])/pp[i-1])
    #tt[i]=tt[i]*rr[i]
print rr
mm=dl.seq_intg(rr)
plt.plot(mm,"b")
plt.show()
'''







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


#plt.subplot(211)
#plt.plot(dayindi.get(u"小台未純化主力企圖")+dayindi.get("金期未純化主力企圖")+dayindi.get("電期未純化主力企圖"),"y")

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

#plt.plot(dayindi.get(u"大台黑手"),"r")
#plt.plot(dayindi.get(u"小台黑手"),"g")
#plt.plot(-dayindi.get(u"小台散戶"),"g")

#plt.plot(-dayindi.get(u"大台散戶"),"g")
#plt.plot(-dayindi.get(u"小台散戶"),"g")
