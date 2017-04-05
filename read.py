import sys 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
df=pd.read_csv('D:\Dropbox\paper/dataset/new_record.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
loc=df['2007/8/28 12:00:00':'2007/8/28 13:00:00'].Global_active_power
print(loc)
mean = loc.rolling(window=15).mean()
print(loc)
mean.plot()
plot.title('Histogram of Power')
plot.show()