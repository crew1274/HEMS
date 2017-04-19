import sys 
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def read(target_time):
    range_x=target_time-pd.to_timedelta(15, unit='m')    
    range_y=range_x+pd.to_timedelta(30, unit='m')   
    loc_pre=df.loc[range_x:range_y].Global_active_power 
    loc_pre_mean= loc_pre.rolling(window=15).mean()
    loc_pre_mean[15:].plot()
    plot.title(range_y)
    plot.show()

df=pd.read_csv('D:\Dropbox\paper/dataset/new_record.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index

#日期時間
date=format(sys.argv[1])
time=format(sys.argv[2])
gap=int(format(sys.argv[3]))
target_time=pd.to_datetime(date+' '+time)#轉換時間標籤

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

#計算DWT距離
distance, path = fastdtw(loc_pre.values, loc_before.values, dist=euclidean)
print(distance)

#計算移動平均的DWT距離
distance, path = fastdtw(loc_pre_mean[15:].values, loc_before_mean[15:].values, dist=euclidean)
print('移動平均後的DWT:%s' %(distance))

read(target_time)
min_target_time=target_time-pd.to_timedelta(gap , unit='d')
read(min_target_time)