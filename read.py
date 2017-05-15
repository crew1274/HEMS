import sys 
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
#選擇時間
stamp = '2008/5/16'
df=pd.read_csv('D:\Dropbox\paper/dataset/dataset.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
loc_pre=df.Global_active_power.loc[stamp]
loc_pre_mean = loc_pre.rolling(window=15).mean()
loc_pre_mean.plot()
plot.title(stamp)
plot.show()