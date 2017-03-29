import pandas as pd
df=pd.read_csv('../dataset/record.csv') #讀取資料
#df=pd.read_csv('../dataset/test.csv') #讀取資料
print(df.describe)#資料顯示
print(df.dtypes)#資料格式
print(df.isnull().sum()) #偵測nan
df['Datetime'] = pd.to_datetime(df['Date']+" "+df['Time']) #時間處理
del df['Date']
del df['Time']
del df['Global_reactive_power']
del df['Voltage']
del df['Global_intensity']
df.index = df['Datetime']
del df['Datetime']
print(df.describe)
#df.to_csv('../dataset/new_test.csv')
df.to_csv('../dataset/new_record.csv')