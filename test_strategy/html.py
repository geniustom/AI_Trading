# coding=UTF-8
###############################################################################   
  
from bokeh.plotting import figure, output_file, show, hplot
from bokeh.models.widgets import Slider
output_file('layout.html')
p = figure(width=400,height=200) # 建立圖表
p.line([1,2,3,4,5],[5,4,3,2,1])
slide = Slider()                 # 建立 Slider
layout = hplot(p,slide)          # 將圖表與 Slider 利用 hplot 排版
show(layout)