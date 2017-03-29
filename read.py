import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
df=pd.read_csv('new_record.csv') #讀取資料
df.index = pd.to_datetime(df['Time'])
del df['Time']
print(df['2007-4-1':'2007-4-2'])
