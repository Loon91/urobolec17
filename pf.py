# -*- coding: utf-8 -*-
"""
Created on Tue May 09 11:39:14 2017

@author: maki
"""

import numpy as np
import matplotlib.pyplot as plt

n = 10000  # サンプル数
sigma_u = 0.1  # サージ速度の標準偏差 [m/s]
sigma_v = 0.1  # スウェイ速度の標準偏差 [m/s]
sigma_r = 0.1  # ヨー角速度の標準偏差 [deg/s]

# 初期状態
x = np.random.normal(0.0, 1.0, n)
y = np.random.normal(0.0, 2.0, n)
psi = np.random.normal(0.0, 5.0, n)

fig, ax = plt.subplots()  # 航跡プロットの準備
ax.set_xlabel('Y [m]')  #X軸を上向きに描画するため、XY軸を入れ替える
ax.set_ylabel('X [m]')
ax.grid(True)  # グリッドを表示
ax.axis('equal')  # 軸のスケールを揃える（重要！）
ax.plot(y, x, '.')


