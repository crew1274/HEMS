import pandas as pd
#df=pd.read_csv('../dataset/record.csv') #讀取資料
df=pd.read_csv('../dataset/test.csv') #讀取資料
print(df.describe)#資料顯示
print(df.dtypes)#資料格式
print(df.isnull().sum()) #偵測nan
df['index'] = pd.to_datetime(df['Date']+" "+df['Time']) #時間處理
print(df)
new=pd.DataFrame({'Global_active_power':df['Global_active_power']})
new.index = df['index']
print(new.describe)
new.to_csv('../dataset/new_test.csv')