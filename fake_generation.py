import sys 
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import random

date = "2008/10/20 20:00"
gap = 3 #3小時
mean = 15
range  = 0.75 , 1
df = pd.read_csv('D:\Dropbox\paper/dataset/new_record_fake.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
#轉換時間標籤
range_x = pd.to_datetime(date)
range_y = range_x+pd.to_timedelta(gap, unit='h')
loc = df.loc[range_x:range_y]
for  index,i in loc.iterrows():
    #print(i['Global_active_power'])
    #df.loc[index,['Global_active_power']].replace([1],inplace=True)
    df.loc[index,'Global_active_power'] = random.uniform(range[0],range[1])
#顯示當天用電圖
print(df.Global_active_power.loc[range_x:range_y])
loc_pre = df.Global_active_power.loc[date.split()[0]]
loc_pre_mean = loc_pre.rolling(window=mean).mean()
loc_pre_mean.plot()
plot.title('%s fake'%(date))
plot.show()
