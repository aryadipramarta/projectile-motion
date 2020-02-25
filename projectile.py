# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
import math

Px1 = 0
Py1 = 0
Ax1 = 0
Ay1 = -9.8
t1 = 0
g = 9.8
m = 0.15
D = 0.0013
Dt = 0.01
Vo = 50
theta = math.radians(35)
sinTheta = math.sin(theta)
cosTheta = math.cos(theta)
Vy1 = Vo*sinTheta
Vx1 = Vo*cosTheta
t2 = 0
Vx2 = Vo*cosTheta
Vy2 = Vo*sinTheta
V = math.sqrt((Vy2 * Vy2) + (Vx2 * Vx2))
Ax2 = -(D/m) * V * Vx2
Ay2 = -g-(D/m) * V * Vy2
Px2 = 0
Py2 = 0
posisiX = []
posisiY = []
posisiX2 = []
posisiY2 = []
while Py1 >= 0 :
    Px1 = Px1 + Vx1*Dt
    Py1 = Py1 + Vy1*Dt
    Vx1 = Vx1 + Ax1*Dt
    Vy1 = Vy1 + Ay1*Dt
    t1 = t1 + Dt
    posisiX.append(Px1)
    posisiY.append(Py1)
    print("Waktu ",round(t1,2))
    print("Posisi X",round(Px1,3))
    print("Posisi Y",round(Py1,3))
    print("Nilai Vx",round(Vx1,3))
    print("Nilai Vy",round(Vy1,3))

while Py2 >= 0 :
    Px2 = Px2 + Vx2*Dt
    Py2 = Py2 + Vy2*Dt
    Vx2 = Vx2 + Ax2*Dt
    Vy2 = Vy2 + Ay2*Dt
    t2 = t2 + Dt
    posisiX2.append(Px2)
    posisiY2.append(Py2)

plt.plot(posisiX,posisiY)
plt.plot(posisiX2,posisiY2)
plt.xlabel("Posisi X")
plt.ylabel("Posisi Y")
plt.title("Posisi X dan Posisi Y")
plt.legend(["Mengabaikan Hambatan Udara","Mempertimbangkan hambatan udara"])
plt.show()
    