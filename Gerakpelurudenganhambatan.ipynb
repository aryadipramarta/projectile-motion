# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:05:06 2020

@author: Microsoft
"""


import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

fig = plt.figure() 
ax = plt.axes(xlim=(0, 250), ylim=(0, 45)) 
line, = ax.plot([], []) 

g = 9.8
m = 0.15
D = 0.0013
Dt = 0.01
Vo = 50
theta = math.radians(35)
sinTheta = math.sin(theta)
cosTheta = math.cos(theta)
t2 = 0
Vx2 = Vo*cosTheta
Vy2 = Vo*sinTheta
V = math.sqrt((Vy2 * Vy2) + (Vx2 * Vx2))
Ax2 = -(D/m) * V * Vx2
Ay2 = -g-(D/m) * V * Vy2
Px2 = 0
Py2 = 0
posisiX2 = []
posisiY2 = []
dataX2 = []
dataY2 = []

while Py2 >= 0 :
    Px2 = Px2 + Vx2*Dt
    Py2 = Py2 + Vy2*Dt
    Vx2 = Vx2 + Ax2*Dt
    Vy2 = Vy2 + Ay2*Dt
    t2 = t2 + Dt
    posisiX2.append(Px2)
    posisiY2.append(Py2)

def animation_frame(i):
	dataX2.append(posisiX2[i])
	dataY2.append(posisiY2[i])
    
	line.set_data(dataX2, dataY2)
	return line,


plt.title('Grafik Gerak Peluru Dengan Hambatan')
animation = FuncAnimation(fig, func=animation_frame, frames=1000, interval=3)
plt.show()