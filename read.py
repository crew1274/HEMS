import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
df=pd.read_csv('../dataset/new_record.csv') #讀取資料
df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
print(df['2007-4-1':'2007-4-2'])
