# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:20:12 2020

@author: Microsoft
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:08:55 2020

@author: Microsoft
"""


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
t2 = 0.01
Vx2 = Vo*cosTheta
Vy2 = Vo*sinTheta
Ax2 = 0
Ay2 = -9.8
Px2 = 0
Py2 = 0
Xo = 0
Yo = 0
posisiX = []
posisiY = []
posisiX2 = []
posisiY2 = []
print("Hasil Analitik")
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

print("Hasil Numerik")
while Py2 >= 0 :
    Px2 = Xo + (Vx2 * t2) + (1/2 * Ax2 * (t2*t2))
    Py2 = Yo + (Vy2 * t2) + (1/2 * Ay2 * (t2*t2))
    print("Posisi X",round(Px2,3))
    print("Posisi Y",round(Py2,3))
    print("Waktu",round(t2,3))
    t2 = t2+Dt
    posisiX2.append(Px2)
    posisiY2.append(Py2)
    
plt.plot(posisiX,posisiY)
plt.plot(posisiX2,posisiY2)
plt.xlabel("Nilai X")
plt.ylabel("Nilai Y")
plt.legend(["Analitik","Numerik"])
plt.title("Grafik Gerak Peluru Analitik dan Numerik")
plt.show()