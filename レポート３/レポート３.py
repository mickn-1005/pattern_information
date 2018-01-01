# -*- coding: utf-8 -*-
"""
パターン情報学　レポート３
線形重回帰の実装
expecting mpg by learning weight and horsepower....
"""

import numpy as np
import csv
import matplotlib.pyplot as plt
import importlib

importlib.import_module('mpl_toolkits.mplot3d').__path__
from mpl_toolkits.mplot3d import Axes3D

cars_data = open('auto-mpg.data')
reader = csv.reader(cars_data)
cars = []
indexes = {'1': "cylinders",\
'2':" displacement",\
'3':" horsepower ",\
'4':" weight",\
'5':" acceleration",\
'6':" model year",\
'7':" origin"}
paras = []
grid = 10       #軸のグリッド分割（識別教会用）

def border(w,x):
    return np.dot(w,x)

'''
create dataset
0 mpg
1 cylinders
2 displacement
3 horsepower
4 weight
5 acceleration
6 model year
7 origin
8 carname
'''
for row in reader:
    origin = row[0].split(" ")
    group = set(origin)
    edited = sorted(group , key=origin.index)
    edited.pop(1)
    cars.append(edited)

selected = set( input('燃費を分析するパラメータを番号で複数設定してください。\
（今回は3,4を選択してHorsepower,Weightについて解析してください）\n\
1: cylinders\n\
2: displacement\n\
3  horsepower \n\
4: weight\n\
5: acceleration\n\
6: model year\n\
7: origin\n\
 == '))

for elem in selected:
    if elem in indexes:
        paras.append(int(elem)-1)
paras = sorted(paras)
print('selected parameters:')
for i in paras:
    print(indexes[str(i)])

num_car = len(cars)
num_ind = len(paras)

'''
決定境界を設定
s.t. 重みベクトルwの解析
X_obs: 学習パターン観測ベクトル(2D:  0:horse, 1: weight)
::mDまで拡張できるように
t_gol: 学習パターン目標ベクトル(1D:  mpg)
'''
t_gol = np.zeros(num_car)
X_obs = np.ones((num_car,num_ind+1))
na = []

for i in range(num_car):
    try:
         t_gol[i] = cars[i][0]
         for j in range(num_ind):
             X_obs[i,j+1] = float(cars[i][paras[j]])
    except:
        na.append(i)
na.reverse()

for sing in na:
    X_obs = np.delete(X_obs,sing,0)
    t_gol = np.delete(t_gol,sing)

w_vec =np.dot(np.dot( np.linalg.pinv(np.dot(X_obs.T,X_obs)),X_obs.T) ,t_gol.T)

"""
結果の可視化(3D)
"""
#if num_ind > 2:
  #  axis_vec = input('二次元での結果の可視化を行います。\n\
    #上に示してある番号を参照してx軸、y軸に撮りたいパラメータ番号を順に入力してください。\n\
    #（２個の場合スキップされるシーケンス）\n')

axis = paras
fig1 = plt.figure()
ax1 = Axes3D(fig1)

ax1.scatter3D(X_obs.T[1],X_obs.T[2],t_gol)

x_border = np.arange(1.1*min(X_obs.T[1]),1.1*max(X_obs.T[1]),1.1*(max(X_obs.T[1])-min(X_obs.T[1]))/grid)
y_border = np.arange(1.1*min(X_obs.T[2]),1.1*max(X_obs.T[2]),1.1*(max(X_obs.T[2])-min(X_obs.T[2]))/grid)
X,Y = np.meshgrid(x_border,y_border)

ax1.plot_wireframe(X,Y,w_vec[0]+w_vec[1]*X+w_vec[2]*Y)
plt.show()