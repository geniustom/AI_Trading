# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import scipy as sc
import lib.dblib as lb


def CalMDD(profit,detail):
    profit_total=lb.seq_intg(np.array(profit))
    profit_max=[]
    win_times=0
    lose_times=0
    win_total=0
    lose_total=0
    
    for i in range(len(profit_total)):
        if i==0: 
            profit_max.append(profit_total[i])
        else:
            profit_max.append(max(profit_total[i],profit_max[i-1]))
        if profit[i]>0:
            win_times+=1                                    #贏次數
            win_total+=profit[i]                            #總獲利
        if profit[i]<0:
            lose_times+=1                                   #輸次數
            lose_total-=profit[i]                           #總虧損
            
    
    trade_times = win_times + lose_times                    #交易次數
    win_rate    = float(win_times) / trade_times            #勝率
    lose_rate   = float(lose_times) / trade_times           #賠率
    avg_win     = float(win_total) / win_times              #平均每筆獲利
    avg_lose    = float(lose_total) / lose_times            #平均每筆虧損
    avg_winrate = avg_win / avg_lose                        #獲利虧損比
    pf          = win_total / lose_total                    #獲利因子
    kelly       = (win_rate-((1-win_rate)/avg_winrate))*100 #凱利值
    profit_dd   = profit_max-profit_total
    profit_mdd  = max(profit_dd)                            #MDD
    net_profit  = win_total-lose_total                      #淨利
    
    if detail==1:
        #print (u"贏次數:" ,win_times)
        #print (u"總獲利:" ,win_total)
        #print (u"輸次數:" ,lose_times)
        #print (u"總虧損:" ,lose_total)
        print (u"交易次數:" ,trade_times)
        print (u"勝率:" ,win_rate)
        #print (u"賠率:" ,lose_rate)
        #print (u"平均每筆獲利:" ,avg_win)
        #print (u"平均每筆虧損:" ,avg_lose)
        #print (u"獲利虧損比:" ,avg_winrate)
        #print (u"獲利因子:" ,pf)
        print (u"凱利值:" ,kelly)
        print (u"MDD:" ,profit_mdd)
        print (u"淨利:" , net_profit)
    
    return net_profit,profit_mdd,kelly
    
    





#print CalMDD(BackTest.profithist,0)
