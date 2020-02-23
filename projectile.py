# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
import math

Ax = 0
Ay = -9.8

t = 0 
Dt = 0.1
Vy = 20*math.sin(0.785398)
Vx = 20*math.cos(0.785398)
Px = 0
Py = 0

print("Nilai t",t)
print("Nilai Px",Px)
print("Nilai Py",Py)
print("Nilai Vx",Vx)
print("Nilai Vy",Vy)
while Py >= 0 :
    Px = Px + Vx*Dt
    Py = Py + Vy*Dt
    Vx = Vx + Ax*Dt
    Vy = Vy + Ay*Dt
    t = t + Dt
    print("Nilai t",round(t,2))
    print("Nilai Px",round(Px,3))
    print("Nilai Py",round(Py,3))
    print("Nilai Vx",round(Vx,3))
    print("Nilai Vy",round(Vy,3))
    
    