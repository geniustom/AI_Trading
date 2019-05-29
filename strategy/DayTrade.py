# coding=UTF-8

import os
import common    as cm;      reload(cm);
import lib.dblib as dl;      reload(dl);
import s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47
import s01_1,s05_1,s10_1,s11_1,s12_1,s15_1,s18_1,s20_1,s21_1,s22_1,s25_1,s26_1,s27_1,s28_1,s29_1,s30_1,s31_1,s32_1,s33_1,s34_1,s35_1,s36_1,s37_1
import s21_i,s22_i,s38_i,s39_i,s40_i,s41_i,s42_i,s43_i,s44_i
import n01,n02,n03,n04,n05,n06,n07



try:
    dbstr = db.connstr
    datecount = td.DateCount
except:
    db = dl.DBConn(host="127.0.0.1",uid="sa",pwd="geniustom",cata="FutureHis")
    td=dl.TradeData(db.conn)


'''
reload(s1)
reload(s2)
reload(s3)
reload(s4)
reload(s5)
reload(s6)
reload(s7)
reload(s8)
reload(s9)
reload(s10)
reload(s11)
'''

def daytrade(s):
    return cm.runDayTrade(db,td,fName=s.FName,cName=__name__,sName=s.s1,sTittle=s.STittle)

TotalProfit=0
TotalProfit+= daytrade(s01)
TotalProfit+= daytrade(s02)
TotalProfit+= daytrade(s03)
TotalProfit+= daytrade(s04)
TotalProfit+= daytrade(s05)
TotalProfit+= daytrade(s06)
TotalProfit+= daytrade(s07)
TotalProfit+= daytrade(s08)
TotalProfit+= daytrade(s09)
TotalProfit+= daytrade(s10)
TotalProfit+= daytrade(s11)
TotalProfit+= daytrade(s12)
TotalProfit+= daytrade(s13)
TotalProfit+= daytrade(s14)
TotalProfit+= daytrade(s15)
TotalProfit+= daytrade(s16)
TotalProfit+= daytrade(s17)
TotalProfit+= daytrade(s18)
TotalProfit+= daytrade(s19)
TotalProfit+= daytrade(s20)
TotalProfit+= daytrade(s21)
TotalProfit+= daytrade(s22)
TotalProfit+= daytrade(s23)
TotalProfit+= daytrade(s24)
TotalProfit+= daytrade(s25)
TotalProfit+= daytrade(s26)
TotalProfit+= daytrade(s27)
TotalProfit+= daytrade(s28)
TotalProfit+= daytrade(s29)
TotalProfit+= daytrade(s30)
TotalProfit+= daytrade(s31)
TotalProfit+= daytrade(s32)
TotalProfit+= daytrade(s33)
TotalProfit+= daytrade(s34)
TotalProfit+= daytrade(s35)
TotalProfit+= daytrade(s36)
TotalProfit+= daytrade(s37)
TotalProfit+= daytrade(s38)
TotalProfit+= daytrade(s39)
TotalProfit+= daytrade(s40)
TotalProfit+= daytrade(s41)
TotalProfit+= daytrade(s42)
TotalProfit+= daytrade(s43)
TotalProfit+= daytrade(s44)
TotalProfit+= daytrade(s45)
TotalProfit+= daytrade(s46)
TotalProfit+= daytrade(s47)

TotalProfit+= daytrade(n01)
TotalProfit+= daytrade(n02)
TotalProfit+= daytrade(n03)
TotalProfit+= daytrade(n04)
TotalProfit+= daytrade(n05)
TotalProfit+= daytrade(n06)
TotalProfit+= daytrade(n07)

TotalProfit+= daytrade(s01_1)
TotalProfit+= daytrade(s05_1)
TotalProfit+= daytrade(s10_1)
TotalProfit+= daytrade(s11_1)
TotalProfit+= daytrade(s12_1)
TotalProfit+= daytrade(s15_1)
TotalProfit+= daytrade(s18_1)
TotalProfit+= daytrade(s20_1)
TotalProfit+= daytrade(s21_1)
TotalProfit+= daytrade(s22_1)
TotalProfit+= daytrade(s25_1)
TotalProfit+= daytrade(s26_1)
TotalProfit+= daytrade(s27_1)
TotalProfit+= daytrade(s28_1)
TotalProfit+= daytrade(s29_1)
TotalProfit+= daytrade(s30_1)
TotalProfit+= daytrade(s31_1)
TotalProfit+= daytrade(s32_1)
TotalProfit+= daytrade(s33_1)
TotalProfit+= daytrade(s34_1)
TotalProfit+= daytrade(s35_1)
TotalProfit+= daytrade(s36_1)
TotalProfit+= daytrade(s37_1)

TotalProfit+= daytrade(s21_i)
TotalProfit+= daytrade(s22_i)
TotalProfit+= daytrade(s38_i)
TotalProfit+= daytrade(s39_i)
TotalProfit+= daytrade(s40_i)
TotalProfit+= daytrade(s41_i)
TotalProfit+= daytrade(s42_i)
TotalProfit+= daytrade(s43_i)
TotalProfit+= daytrade(s44_i)

print u"\n\n今日總績效:",TotalProfit
