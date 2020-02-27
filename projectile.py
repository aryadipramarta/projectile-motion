# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

fig = plt.figure() 
ax = plt.axes(xlim=(0, 250), ylim=(0, 45)) 
line, = ax.plot([], []) 

Px1 = 0
Py1 = 0
Ax1 = 0
Ay1 = -9.8
t1 = 0
g = 9.8
Dt = 0.01
Vo = 50
theta = math.radians(35)
sinTheta = math.sin(theta)
cosTheta = math.cos(theta)
Vy1 = Vo*sinTheta
Vx1 = Vo*cosTheta
posisiX = []
posisiY = []
dataX1 = []
dataY1 = []
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

def animation_frame(i):
	dataX1.append(posisiX[i])
	dataY1.append(posisiY[i])
    
	line.set_data(dataX1, dataY1)
	return line,

plt.title('Grafik Gerak Peluru Mengabaikan Hambatan')
animation = FuncAnimation(fig, func=animation_frame, frames=1000, interval=2)
plt.show()    