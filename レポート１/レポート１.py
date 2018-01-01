# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:10:54 2017

@author: mickn

pattarn information(Wed 2) KNN-method
"""
import os
import csv
import numpy as np
#import random
import math
import matplotlib.pyplot as mpl
# os.chdir(r'/Users/mickn/Desktop/2017autumn/パターン情報学/レポート１/')


iris_data = open('iris.csv')
#5. class: -- Iris Setosa -- Iris Versicolour -- Iris Virginica

reader = csv.reader(iris_data)
datas = []

def euclid(x,y):
    f_del = (float(x[0])-float(y[0]))**2
    s_del = (float(x[1])-float(y[1]))**2
    t_del = (float(x[2])-float(y[2]))**2
    y_del = (float(x[3])-float(y[3]))**2
    return math.sqrt(f_del+s_del+t_del+y_del)

for row in reader:
    print(row)
    datas.append(row)

data_size = len(datas)

for i in range(data_size):
    datas[i].append(0)

success = np.zeros(30)
"""
"""
for  k in range(30):
    for sample in datas:
        #zerosにしてindexで管理した方が楽だった
        setosa = 0
        versi = 0
        virgin = 0

        for i in range(data_size):
            datas[i][5] = (euclid(datas[i],sample))
        #リストで取得
        #１個ランダム要素取得→ユークリッド距離計算

        print('sample is ----')
        print(sample)
        datas.sort(key = lambda x:x[5])
        #datasdatas.pop(0)
        #k近傍取得
        k_mean = datas[1:k+2]
        for exam in k_mean:
            setosa += exam.count('Iris-setosa')
            versi += exam.count('Iris-versicolor')
            virgin += exam.count('Iris-virginica')
        if(setosa is max(setosa, versi, virgin)):
            label = 'Iris-setosa'
            print('is setosa')
        if(versi is max(setosa, versi, virgin)):
            label ='Iris-versicolor'
            print('is versi')
        if(virgin is max(setosa, versi, virgin)):
            label ='Iris-virginica'
            print('is virgin')
        if(label == datas[0][4]):
            success[k] += 1
i = np.arange(0,30,1)
mpl.plot(i+1,success[i]/150)
mpl.show()
