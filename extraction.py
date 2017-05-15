import time
tStart = time.time()
from collections import Counter

import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

date = "2008/12/28 18:00" 
interval = 3 #單位小時
run_gap = 10 #每隔幾分鐘檢查
mean = 15  #roll mean window size，window size 越長，抗躁能力越好
weight = 1  #權重
time_gap = 15 #比對時間長度
threshold = time_gap * weight #門檻值，比對時間越長，門檻值相對越高

def valid(target_time, gap):
    # 抓取時間範圍
    range_x = target_time - pd.to_timedelta(time_gap, unit='m')
    range_y = range_x + pd.to_timedelta(time_gap * 2, unit='m')
    loc_pre = df.loc[range_x:range_y].Global_active_power
    # 抓取欲比對的時間範圍
    range_x = target_time - pd.to_timedelta(gap, unit='d') - pd.to_timedelta(time_gap, unit='m')
    range_y = range_x + pd.to_timedelta(time_gap * 2, unit='m')  
    loc_before = df.loc[range_x:range_y].Global_active_power
    # 計算移動平均
    loc_pre_mean = loc_pre.rolling(window=mean).mean()
    loc_before_mean = loc_before.rolling(window=mean).mean()
    distance, path = fastdtw(loc_pre_mean[time_gap:].values, loc_before_mean[mean:].values, dist=euclidean)
    print('移動平均後的DWT:%s' % (distance))
    return distance

def valid_read(target_time, gap):
    range_y = target_time
    range_x = range_y - pd.to_timedelta(gap, unit='m')
    plot.show()

def main(target_time, gap):
    # 抓取時間範圍
    range_y = target_time
    range_x = range_y - pd.to_timedelta(gap, unit='m')  # 往前抓取1小時
    loc_pre = df.loc[range_x:range_y].Global_active_power  # 撈資料
    loc_pre_mean = loc_pre.rolling(window=mean).mean()  # 計算移動平均
    # print(loc_pre_mean[15:].values)
    min_distance = None
    stamp = None
    # 星期為單位比較相似度
    for i in range(1, 6, 1):
        # 1,2,3,4,5
        range_y = target_time - pd.to_timedelta(7 * i, unit='d')  # 抓取前i禮拜資料
        range_x = range_y - pd.to_timedelta(gap, unit='m')  # 抓取前gap分鐘
        range_time = range_x, range_y
        loc_before = df.loc[range_time[0]:range_time[1]].Global_active_power  # 抓資料
        # 計算移動平均
        loc_before_mean = loc_before.rolling(window=mean).mean()
        # print(loc_before_mean[15:].values)
        # 計算移動平均的DWT距離
        distance, path = fastdtw(loc_pre_mean[mean:].values, loc_before_mean[mean:].values, dist=euclidean)
        # print(distance)
        # 尋找最小的距離並記錄timestamp
        if min_distance == None:
            min_distance = distance
            stamp = i * 7
        if min_distance > distance:
            min_distance = distance
            stamp = i * 7
    # 天為單位比較相似度
    for i in range(1, 6, 1):
        # 1,2,3,4,5
        range_y = target_time - pd.to_timedelta(1 * i, unit='d')
        range_x = range_y - pd.to_timedelta(gap, unit='m')
        range_time = range_x, range_y
        loc_before = df.loc[range_time[0]:range_time[1]].Global_active_power  #抓資料
        # 計算移動平均
        loc_before_mean = loc_before.rolling(window=mean).mean()
        # print(loc_before_mean[15:].values)
        # 計算移動平均的DWT距離
        distance, path = fastdtw(loc_pre_mean[mean:].values, loc_before_mean[mean:].values, dist=euclidean)
        # print(distance)
        if min_distance > distance:
            min_distance = distance
            stamp = i
    print('==================================')
    print(gap)
    print(min_distance)
    print(stamp)
    return min_distance, stamp

if __name__ == "__main__":
    df = pd.read_csv('D:\Dropbox\paper/dataset/dataset.csv')  # 讀取資料
    df.index = pd.to_datetime(df['Datetime'])  # 轉換index，因為從csv讀取無index
    init_time = pd.to_datetime(date)  # 轉換時間標籤
    record = []
    counter = 0
    for invoke in range (int(interval*60 / run_gap)):
        target_time = init_time + pd.to_timedelta(invoke * run_gap, unit='m') 
        stamp_tmp = []
        distance = []
        for gap in range(30, 105, 15):
            # 30、45、60、75、90
            min_distance, stamp = main(target_time, gap)
            stamp_tmp.append(stamp)
            distance.append(min_distance)
        stamp = Counter(stamp_tmp).most_common(1) #找尋最常出現的元素
        print('猜測與 %s 時用電行為最相似的時間: %s 天前' % (target_time, stamp[0][0]))
        valid(target_time, stamp[0][0])
        distance_tmp = valid(target_time, stamp[0][0])
        if(distance_tmp > threshold):
            tmp = [target_time, stamp[0][0], distance_tmp, True]
            counter = counter+1
        else:
            tmp = [target_time, stamp[0][0], distance_tmp, False]
        record.append(tmp)
    print(record)
    print("正常用電時警報發生:%s次"%(counter))
    tEnd = time.time()
    print ("程式執行: %f 秒"%(tEnd - tStart))
        #min_tar:get_time=target_time-pd.to_timedelta(stamp , unit='d')
        # valid_read(target_time,gap)
        # valid_read(min_target_time,gap)
