# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import particlefilter as pf

             
plotinterval = 10  # 何秒ごとに描画するか
condition = 1  # 条件番号

fig, ax = plt.subplots()  # 航跡プロットの準備
ax.set_xlabel('Y [m]')  #X軸を上向きに描画するため、XY軸を入れ替える
ax.set_ylabel('X [m]')
ax.grid(True)  # グリッドを表示
ax.axis('equal')  # 軸のスケールを揃える（重要！）

P = pf.ParticleFilter(1000)
P.scatter([0, 0, 0], [1., 2., 5.])    
for i in range(100):
    if condition == 1:
        P.move([1., 0., 0.], [0.1, 0.1, 1.0], 1.)
    else:
        P.move([0., 0., 0.], [1.0, 1.0, 1.0], 1.)
        if i % 10 == 0:
            P.observeLBL(10., 0., [10., 0., 0.], 0.5, 3)
            P.resample()
    if i % plotinterval == 0:
        P.display(ax)
        plt.pause(.1)
    
plt.show()
