# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:51:02 2017

@author: mickn
pattarn information(Wed2) k-means method
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import random

iris_data = open('iris.csv')

reader = csv.reader(iris_data)
datas = []
claster = [[],[],[],[],[]]
delta = [0,0,0,0,0]
cog = [[0,0,0,0,'gracvitational center', 0,0],[0,0,0,0,'gracvitational center', 0,0],[0,0,0,0,'gracvitational center', 0,0],[0,0,0,0,'gracvitational center', 0,0],[0,0,0,0,'gracvitational center', 0,0]]
cog_0 = [[],[],[],[],[]]
length = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
width = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]

def euclid(x,y):
    f_del = (float(x[0])-float(y[0]))**2
    s_del = (float(x[1])-float(y[1]))**2
    t_del = (float(x[2])-float(y[2]))**2
    y_del = (float(x[3])-float(y[3]))**2
    return math.sqrt(f_del+s_del+t_del+y_del)
    
def center(x):      #when x is empty????????????????????????
    if len(x) is 0:
        return None
    pos_sum = [0.0,0.0,0.0,0.0]
    for vec in x:
        for j in range(4):
            pos_sum[j] += float(vec[j])
    for j in range(4):
        pos_sum[j]/=len(x)
    return pos_sum
    
def dis_sort(son, mom):
    for dau in mom:
        dau[5] = euclid(dau, son)
    mom.sort(key = lambda x:x[5])
    
    
'''
main code
'''    
for row in reader:
    datas.append(row) #data import
"""
datasの０〜４はいじらない
"""
data_size = len(datas)

for i in range(data_size):
    datas[i].append(0)      #distance append
    datas[i].append('label number')    #judged label append
    
#setosa = []
#versi = []
#virgin = []
#flower = {'Iris-setosa':setosa,'Iris-versicolor':versi,'Iris-virginica':virgin} #辞書で定義

for k in range(2,3):
    samples = random.sample(datas, k) #k個のランダム抽出：初期値
    for i in range(k):
        cog_0[i] = samples[i]
    
    for i in range(len(samples)):
        samples[i][6] = i
    
    for cnt in range(100): 
        for i in range(k):
            claster[i] = []
        for exams in datas:
            dis_sort(exams, samples)
            exams[6] = samples[0][6]    #１番近い要素のラベルを６番に割り当て
            claster[exams[6]].append(exams)
        #cog formation
        for i in range(len(claster)):
            cog[i] = center(claster[i])
            
        #representative re-selectionここ要デバッグ
        for i in range(k):
            for exams in claster[i]:
                exams[5] = euclid(exams, cog[i])
            claster[i].sort(key = lambda x: x[5])
            delta[i] = abs(euclid(samples[i],cog[i])-claster[i][0][5])
            samples[i] = claster[i][0]
            delta[i] = euclid(cog_0[i],cog[i])
            cog_0[i] = cog[i]
            
        #print(cog)
        print(delta)
        if max(delta)<0.001:
            print('break by delta')
            break
        for i in range(k):
            for flower in claster[i]:       
                length[k][i].append(float(flower[0]))
                width[k][i].append(float(flower[1]))
            plt.scatter(length[k][i],width[k][i])
            plt.show()