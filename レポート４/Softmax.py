# -*- coding: utf-8 -*-
"""
Spyder Editor

Pattarn Information
---Softmax Recursion
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import time

t_0 = time.clock()
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/mnist_data/", one_hot=True)

"""
Global definition
"""
eta = 0.025 #学習係数（二分探索？？）
loop = 1000     #試行回数限度
limit  = 0.0001 #許容誤差

"""
ソフトマックス関数
各クラスの事後確率と等しい
"""
def sofmax(x):  #Matrix(列ベクトルN個)
    xex = np.exp(x)
    xum = np.sum(xex,axis=0)    #列毎の和（Nベクトル）
    return xex/xum      #softmax関数行列を返す

"""
多クラス交差エントロピー関数
ーー尤度最大化パラメータを求めたい。
"""
def del_log(X_l,T_l,P_l):
    dJ = np.dot(X_l.T,P_l-T_l)    #負の対数尤度関数行列（損失関数）の微分
    return dJ
"""
事後確率行列P
"""
def prob_aft(W_l,X_l):
    P = sofmax(np.dot(W_l.T,X_l.T))
    return P
"""
勾配降下法
"""
def grad(W_l,eta_l,X_l,T_l):
    P_l = prob_aft(W_l,X_l)
    del_l = eta_l*del_log(X_l,T_l,P_l)
    W_l = W_l - del_l
    return max(np.abs(del_l))
"""
ソフトマックス回帰の学習
"""
def learning(X_l,T_l):
    delta  = limit+1    #最大修正量
    W_l = np.zeros((len(X_l.T),len(T_l.T)))     #重み行列（初期値？？）
    cnt = 0
    while delta >= limit:
        if cnt >= loop:
            break
        else:
            delta = grad(W_l,eta,X_l,T_l)
    return W_l

def action(W_l,D_l):
              





t_1 = time.clock()
print('runtime :', t_1-t_0)
