import sys 
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

df=pd.read_csv('D:\Dropbox\paper/dataset/new_record_fake.csv') #讀取資料
#df=pd.read_csv('D:\Dropbox\paper/dataset/new_record.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index

range_x=pd.to_datetime('2007/9/2 8:00')#轉換時間標籤
range_y=pd.to_datetime('2007/9/2 10:00')#轉換時間標籤
print(df.Global_active_power.loc[range_x:range_y])
df.loc[range_x:range_y,'Global_active_power'] = 2.8
print(df.Global_active_power.loc['2007/9/2'])
loc_pre=df.Global_active_power.loc['2007/9/2']
loc_pre_mean = loc_pre.rolling(window=15).mean()
loc_pre_mean.plot()
plot.title('2007/9/2 fake')
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