# coding=UTF-8
import os
import numpy as np
import common    as cm;      reload(cm);
import lib.dblib as dl;      reload(dl);
import lib.analytics as an;  reload(an);
import matplotlib.pyplot as plt

'''
    ====== 夢幻球隊演算法 ======
    假設預計要組出M支資金規模下的最佳策略配置
    首先將所有策略中目前正在破MDD的剃除，整理出一份存活策略清單，策略數為N
    接著採用局域最佳化擴展到全域最佳化演算法，第一回合先從存活策略清單找出獲利風險比+凱利值最高者
    而後從剩下的N-1支，找出一支與第一支合併後獲利風險比+凱利值最高者
    直到從剩下的N-M支，找出一支與前M支合併後獲利風險比+凱利值最高者
    最終結果即為M支資金規模下的最佳策略配置 (獲利最高、風險最低、曲線最平滑)
'''


def CheckProfit(test_s): #確認某個策略近days日的總獲利為正
    days=20
    n=len(test_s)
    if sum(test_s[n-days:])>0 :
        return 1
    else:
        return 0
    


def CheckAlive(test_s):   #確認某個策略目前是否正在破MDD中
    n=len(test_s)
    max_index=0
    max_value=0
    min_index=0
    min_value=0
    s=np.zeros(n)
    max_seq=np.zeros(n)
    for i in range(n):
        if i==0:
            s[i]=test_s[i]
        else:
            s[i]=test_s[i]+s[i-1]
    
    for i in range(n):
        if s[i]>max_value:
            max_value=s[i]
            max_index=i
        max_seq[i]=max_value    #創高序列
        
        if max_seq[i]-s[i]>min_value:
            min_index=i
            min_value=max_seq[i]-s[i]
    
    #print "創高位置：", max_index , "破MDD位置：" , min_index
    if min_index>max_index:  #若破底比創高晚發生，代表此策略掛了
        return 0 
    else:
        return 1


def CalProfit(org,new):
    testnew=org+new
    #net,mdd,kelly=an.CalMDD(testnew,0)
    net=sum(testnew)
    #recent_profit=sum(testnew[len(testnew)-30:])  #good (30最佳)
    ###################################################################
    #return kelly*net , testnew
    #return (kelly+(net/mdd))*net , testnew
    #return (kelly+(net/mdd))*recent_profit , testnew
    #return kelly*(net/mdd)*net , testnew
    #return kelly*(net/mdd)*recent_profit , testnew
    #return kelly , testnew
    #return recent_profit , testnew
    #return (net/mdd)*net , testnew
    #return kelly+(net/mdd) , testnew
    #return net*recent_profit , testnew   #good
    return net , testnew #good
    
'''
心得：
1. net最好
2. (kelly+(net/mdd))*net 最穩
3. 賺錢的時候不換組合，賠錢超過一定幅度之後才換組合

'''    
    
    
def GetLowCorrSet(M,N,L,S,A):   # M:策略組合數 , N:總策略數 , L:資料長度 , S:
    print "策略數：" , N , ", 資料長度：", L
    count=0
    SelectedStrategy=np.zeros(N)
    SpanningProfit=np.zeros(L)
    
    for i in range(M):
        localBest=0
        for j in range(N):
            if SelectedStrategy[j]==0 and A[j]==1:
                count+=1
                x,y=CalProfit(SpanningProfit,S[:L,j])
                if x>localBest: 
                    localBest=x
                    localBestProfit=y
                    localBestIndex=j
        SpanningProfit=localBestProfit
        SelectedStrategy[localBestIndex]=1
    print "最佳策略風險報酬獲利加權值：" ,x , "疊代次數：", count
    return SelectedStrategy

def GetAliveStrategyList(S,N,L):
    AliveStrategyList=np.zeros(N)
    wins=0
    for i in range(N):
        if CheckProfit(S[:L,i])==1 and CheckAlive(S[:L,i])==1:
            AliveStrategyList[i]=1
            wins+=1
            
    print "目前存活的策略數：",wins
    return AliveStrategyList
    
    
def FindBestStrategySet(S,m,n,l):  #S:所有策略每日績效 , m:預期要組出的策略數 , n:總策略數 , l:資料回測長度
    print "====== 夢幻球隊演算法 ======"
    AliveList=GetAliveStrategyList(S,n,l)
    print "最佳策略組合配置演算法之目標策略數：",m
    return GetLowCorrSet(m,n,l,S,AliveList)


def CalProfitInStrategySetOnDay(A,index): #輸入可用策略清單與指定日期索引，算出當日績效
    profit=0
    for i in range(len(A)):
        if A[i]==1:
            profit+=AT3[index,i]
    return profit

def StrategySetIsAlive(P,SETS,M):   #確認今天的策略是否該換了 P:當日個策略損益 S:策略集合，M策略組合數
    swin=0
    slose=0
    for i in range(len(SETS)):
        if SETS[i]==1:
            if P[i]>0:
                swin+=1
            else:
                slose+=1
    #print "P:",SETS,"Win:",swin," Lose:",slose
    if slose>swin*3 or (len(SETS)==0):
        return 0
    else:
        return 1


#=================================  單日測試  =================================
'''
m=20
n=len(T1) #取得策略數
l=len(T3) #取得回測資料長度

sets=FindBestStrategySet(m,n,l)   
for i in range(n):
    if sets[i]==1:
        print T1[i]
        
'''    
#================================全面測試&回測==================================        
m=25             #預計要組出的策略數
AT1=T1+T1
AT3=np.hstack((T3,T3))
#AT1=T1
#AT3=T3
n=len(AT1)       #取得策略數
l_all=len(AT3)   #取得回測資料長度
l=60             #計算MDD的前看長度

PC=[]            #待回測的profit curve
PC_Best=[]       #最佳的profit curve
sets=[]
#chang_p=-m*19    #15是25支策略的最佳值
chang_p=-360      #15是25支策略的最佳值 相當於350~370點
p=chang_p
for i in range(l_all-l-1):    #i=0~(476-l-1)
    S=AT3[i:i+l,:]
    print TotalDate[i+l+1]
    if p<=chang_p:    #賠錢才換策略，賺錢不換 (一直換來換去沒比較好)  if StrategySetIsAlive(AT3[i+l+1,:],sets,m)==0: 
        sets=FindBestStrategySet(S,m,n,l)
    p=CalProfitInStrategySetOnDay(sets,i+l+1)
    PC.append(p)
    set_best=sorted(AT3[i+l+1,:],reverse=True)      #當日策略損益由高到低排序
    #PC_Best.append(sum(set_best[:m]))               #排序後M支策略當天的最佳損益
    PC_Best.append(sum(set_best)/len(set_best)*m)     #排序後M支策略當天的平均損益

plt.plot(dl.seq_intg(np.array(PC)),"b")
plt.plot(dl.seq_intg(np.array(PC_Best)),"r")
an.CalMDD(PC,1)



'''
#sets=FindBestStrategySet(AT3,m,n,l)
out=[]
for i in range(n):
    if sets[i]==1:
        out.append(AT1[i])
print out
'''