import sys
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from collections import Counter
from random import randint ,randrange

def valid(target_time,gap):
    #抓取時間範圍
    range_x=target_time-pd.to_timedelta(15, unit='m')
    range_y=range_x+pd.to_timedelta(30, unit='m')#往後抓15分鐘
    loc_pre=df.loc[range_x:range_y].Global_active_power
    #抓取欲比對的時間範圍
    range_x=target_time-pd.to_timedelta( gap , unit='d')-pd.to_timedelta(15, unit='m')
    range_y=range_x+pd.to_timedelta(30, unit='m')#往後抓15分鐘
    loc_before=df.loc[range_x:range_y].Global_active_power
    #計算移動平均
    loc_pre_mean = loc_pre.rolling(window=15).mean()
    loc_before_mean = loc_before.rolling(window=15).mean()
    distance, path = fastdtw(loc_pre_mean[15:].values, loc_before_mean[15:].values, dist=euclidean)
    print('驗證移動平均後的DWT:%s' %(distance))
    return distance


def valid_read(target_time, gap):
    range_y=target_time
    range_x=range_y-pd.to_timedelta(gap, unit='m')   
    loc_pre=df.loc[range_x:range_y].Global_active_power 
    loc_pre_mean= loc_pre.rolling(window=15).mean()
    loc_pre_mean[15:].plot()
    plot.title(target_time)
    plot.show()

def main( target_time , gap ):
    #抓取時間範圍
    range_y=target_time
    range_x=range_y-pd.to_timedelta(gap, unit='m')    #往前抓取1小時
    loc_pre=df.loc[range_x:range_y].Global_active_power #撈資料
    loc_pre_mean= loc_pre.rolling(window=15).mean()    #計算移動平均
    #print(loc_pre_mean[15:].values)
    #print('===============================')
    min_distance = None
    stamp = None
    #星期為單位比較相似度
    for i in range(1,6,1):
        #1,2,3,4,5
        range_y=target_time-pd.to_timedelta(7*i, unit='d')#抓取前i禮拜資料
        range_x=range_y-pd.to_timedelta(gap, unit='m') #抓取前gap分鐘
        range_time=range_x,range_y
        loc_before = df.loc[range_time[0]:range_time[1]].Global_active_power #抓資料
        #計算移動平均
        loc_before_mean= loc_before.rolling(window=15).mean()
        #print(loc_before_mean[15:].values)
        #計算移動平均的DWT距離
        distance, path = fastdtw(loc_pre_mean[15:].values, loc_before_mean[15:].values, dist=euclidean)
        #print(distance)
        #print('===============================')
        #尋找最小的距離並記錄timestamp        
        if min_distance == None:
            min_distance=distance
            stamp = i*7
        if min_distance >  distance:
            min_distance=distance
            stamp = i*7
    #天為單位比較相似度
    for i in range(1,6,1):
        #1,2,3,4,5
        range_y=target_time-pd.to_timedelta(1*i, unit='d')
        range_x=range_y-pd.to_timedelta(gap, unit='m') 
        range_time=range_x,range_y
        loc_before = df.loc[range_time[0]:range_time[1]].Global_active_power #抓資料
        #計算移動平均
        loc_before_mean= loc_before.rolling(window=15).mean()
        #print(loc_before_mean[15:].values)
        #計算移動平均的DWT距離
        distance, path = fastdtw(loc_pre_mean[15:].values, loc_before_mean[15:].values, dist=euclidean)
        #print(distance)
        #print('===============================')
        if min_distance >  distance:
            min_distance=distance
            stamp = i
    print('==================================')
    print(gap)
    print(min_distance)
    print(stamp)
    return min_distance , stamp

if __name__ == "__main__":
    df=pd.read_csv('D:\Dropbox\paper/dataset/new_record.csv')#讀取資料
    df.index = pd.to_datetime(df['Datetime']) #轉換index，因為從csv讀取無index
    '''
    #輸入時間
    date=format(sys.argv[1])
    time=format(sys.argv[2])
    target_time=pd.to_datetime(date+' '+time)#轉換時間標籤
    '''
    record = []
    threshold = 15
    count = 0
    #隨機時間
    for i in range(0,5,1):
        target_time=pd.to_datetime('%s/%s/%s %s:%s'%(randint(2007,2009),randint(1,12),randint(1,28),randint(0,23),randrange(0,59,15)))
        stamp_tmp = []
        dist_tmp = []
        for gap in range(30,105,15):
            #30、45、60、75、90
            min_distance , stamp = main(target_time, gap)
            dist_tmp.append(min_distance)
            stamp_tmp.append(stamp)
        print(dist_tmp)
        print(stamp_tmp)
        #fine the most common element in list
        stamp=Counter(stamp_tmp).most_common(1)
        print('猜測與 %s 時用電行為最相似的時間: %s 天前' %(target_time,stamp[0][0]))
        threshold=0
        for k in range(5):
            if stamp_tmp[k] == stamp[0][0]:
                if threshold < dist_tmp[k]:
                    threshold = dist_tmp[k]
        print('預估相似值為:%s'%(threshold))
        distance_tmp = valid(target_time,stamp[0][0])
        if(distance_tmp > threshold ):
            tmp=[target_time,stamp[0][0],distance_tmp,True]
            count= count +1
        else:
            tmp=[target_time,stamp[0][0],distance_tmp,False]
        record.append(tmp)
    record = pd.DataFrame(record,columns=['datetimes','stamp','distance','alert'])
    print(record)
    print('錯誤警報:%s次'%(count))
    record.to_csv('record.csv',mode='a',header=False)    
    #min_target_time=target_time-pd.to_timedelta(stamp , unit='d')
    #valid_read(target_time,gap)
    #valid_read(min_target_time,gap)
    