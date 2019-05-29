'''
import dblib as lb
import numpy as np
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
# 1.9 , 1.4 最佳參數
# 純小台主力作為 +1754 純小台散戶作為 +804
e,f,g,h,i,j=indi.GetDoPower("小台買成筆","小台賣成筆","小台成交量",1.9,1.4,energy=0)
indi.add(u"小台未純化主力買作為",e) 
indi.add(u"小台未純化主力賣作為",f) 
indi.add(u"小台未純化主力作為",(e-f))

indi.add(u"小台純主力買作為",g) 
indi.add(u"小台純主力賣作為",h) 
indi.add(u"小台純散戶買作為",i) 
indi.add(u"小台純散戶賣作為",j) 

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

e,f,g,h,i,j=indi.GetDoPower("金期買成筆","金期賣成筆","金期成交量",0,1.9)
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
