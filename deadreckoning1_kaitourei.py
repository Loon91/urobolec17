#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
海中ロボット学 第3回
デッドレコニング測位の演習
ファイルを読み込んで、処理して、出力する
'''

import numpy as np
import matplotlib.pyplot as plt
import csv

def drawVehicle2D(pos, heading, axis):
    '''
    世界座標系にAUVを描画する。AUVは三角形とする。
    pos: AUVの水平位置 (x, y) [m]
    heading: AUVの方位角 [deg]
    axis： 描画するaxis
    '''
    length = 2.0  # AUVの長さ [m]
    width = 0.8  # AUVの幅 [m]
    
    p1 = np.array([length/3.0*2, 0])  # AUVの形を表す3角形の頂点
    p2 = np.array([-length/3.0, width/2.0])
    p3 = np.array([-length/3.0, -width/2.0])
  
    sina = np.sin(heading*np.pi/180)
    cosa = np.cos(heading*np.pi/180)
    R = np.array([[cosa, -sina], [sina, cosa]])  #回転行列
    
    p1 = pos + np.dot(R, p1)  # 世界座標系に変換
    p2 = pos + np.dot(R, p2)
    p3 = pos + np.dot(R, p3)
    axis.plot([p1[1], p2[1], p3[1], p1[1]], [p1[0], p2[0], p3[0], p1[0]], 'k')  # 三角形を描画
    axis.plot(pos[1], pos[0], 'ok')  # 中心を描画


filename = 'velocity.csv'  # ファイル名
x = np.array([0.0, 0.0])  # 水平位置の初期値 x[m], y[m]
a = 0.0  # 方位の初期値 [deg]
t = 0.0  # 経過時間 [sec]

f = open(filename, 'r')  # ファイルを開く
reader = csv.reader(f)  # csvモジュールを使う準備
header = next(reader)  # 1行目（ヘッダ）を読み飛ばす
# print header

fig, ax = plt.subplots()  # 航跡プロットの準備
ax.set_xlabel('Y [m]')  #X軸を上向きに描画するため、XY軸を入れ替える
ax.set_ylabel('X [m]')
ax.grid(True)  # グリッドを表示
ax.axis('equal')  # 軸のスケールを揃える（重要！）
#ax.set_xlim(-10, 10)  #プロットする範囲を指定
#ax.set_ylim(-10, 10)

drawVehicle2D(x, a, ax)  # 初期状態をプロット

for row in reader:
    # print row
    t_new = float(row[0])  # 最新データの時刻 [sec]
    v = np.array([float(row[1]), float(row[2])])  #水平速度 ベクトル表記 (u, v) [m/s]
    r = float(row[3])  # ヨー角速度 [deg/s]
    
    dt = t_new - t  # 前のデータとの時間差
    t = t_new
    
    sina = np.sin(a*np.pi/180)
    cosa = np.cos(a*np.pi/180)
    R = np.array([[cosa, -sina], [sina, cosa]])  # 回転行列 R(a)
    
    x = x + np.dot(R, v) * dt  # 水平位置の更新
    a = a + r * dt  # 方位の更新
    print x, a
    drawVehicle2D(x, a, ax)  # 現在の状態をプロット
    plt.pause(.1)  # リアルタイムに描画させるために必要
    
f.close()  # ファイルを閉じる
plt.show()  # グラフウィンドウを開いたままにする
