import sys 
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

df=pd.read_csv('D:\Dropbox\paper/dataset/new_record.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
date=format(sys.argv[1])#日期
time=format(sys.argv[2])#時間
target_time=pd.to_datetime(date+' '+time)#轉換時間標籤
range_y=target_time
range_x=range_y-pd.to_timedelta(1, unit='h')#往前抓一小時
loc_pre=df.loc[range_x:range_y].Global_active_power
print(loc_pre)
print(loc_pre.values)
range_y=target_time-pd.to_timedelta(7, unit='d')#往前抓一天
range_x=range_y-pd.to_timedelta(1, unit='h')#往前抓一小時
loc_before=df.loc[range_x:range_y].Global_active_power
print(loc_before)
print(loc_before.values)
distance, path = fastdtw(loc_pre.values, loc_before.values, dist=euclidean)
print(distance)