import sys 
import pandas as pd
import matplotlib.pyplot as plot

def main():
    date=format(sys.argv[1])#日期
    time=format(sys.argv[2])#時間
    target_time=pd.to_datetime(date+' '+time)#轉換時間標籤
    range_y=target_time
    range_x=range_y-pd.to_timedelta(3, unit='h')
    range_time=range_x,range_y
    print(range_time)
    loc=df.loc[range_time[0]:range_time[1]]
    mean = loc.rolling(window=15).mean()
    print(mean)
    print('===============================')
    mean.plot()
    for i in range(1,5,1):
        range_y=target_time-pd.to_timedelta(7*i, unit='d')#抓取上禮拜資料
        range_x=range_y-pd.to_timedelta(1, unit='h') #抓取前1小時
        range_time=range_x,range_y
        print(range_time)
        loc=df.loc[range_time[0]:range_time[1]] #抓資料
        mean = loc.rolling(window=15).mean()    #計算移動平均
        print(mean)
        print('===============================')
    
    plot.show()


if __name__ == "__main__":
    df=pd.read_csv('D:\Dropbox\paper/dataset/new_record_3_dim.csv') #讀取資料
    df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
    main()