import sys 
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import random
date = "2008/5/16 9:00"
gap = 3
mean = 15
df = pd.read_csv('D:\Dropbox\paper/dataset/new_record_fake.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
#轉換時間標籤
range_x = pd.to_datetime(date)
range_y = range_x+pd.to_timedelta(gap, unit='h')
loc = df.loc[range_x:range_y]
for  index,i in loc.iterrows():
    #print(i['Global_active_power'])
    df.loc[index,'Global_active_power'] = random.uniform(3,3.25)
#顯示當天用電圖
print(df.Global_active_power.loc[range_x:range_y])
loc_pre = df.Global_active_power.loc[date.split()[0]]
loc_pre_mean = loc_pre.rolling(window=mean).mean()
loc_pre_mean.plot()
plot.title('%s fake'%(date))
plot.show()
'''
#抓取時間範圍
range_x=target_time-pd.to_timedelta(15, unit='m')
range_y=range_x+pd.to_timedelta(30, unit='m')#往後抓15分鐘
loc_pre=df.loc[range_x:range_y].Global_active_power

range_x=target_time-pd.to_timedelta( gap , unit='d')-pd.to_timedelta(15, unit='m')
range_y=range_x+pd.to_timedelta(30, unit='m')#往後抓15分鐘
loc_before=df.loc[range_x:range_y].Global_active_power

#計算移動平均
loc_pre_mean = loc_pre.rolling(window=15).mean()
loc_before_mean = loc_before.rolling(window=15).mean() 

print(loc_pre_mean[15:])
print(loc_pre_mean[15:].values)
print(loc_before_mean[15:])
print(loc_before_mean[15:].values)


read(target_time)
min_target_time=target_time-pd.to_timedelta(gap , unit='d')
read(min_target_time)

'''