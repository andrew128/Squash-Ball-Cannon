# import libraries
from math import *
import matplotlib.pyplot as plt

# ============================================
# Declare array variables
t_array = []

dVydt_array = []
Vy_array = []
Y_array = []

dVxdt_array = []
Vx_array = []
X_array = []

# User input
Vy = float(raw_input("Enter initial Y velocity(meters/second): "))
Vy_array.append(Vy)
Y = float(raw_input("Enter initial Y position (meters): "))
Y_array.append(Y)

Vx = float(raw_input("Enter initial X velocity(meters/second): "))
Vx_array.append(Vx)
X =  float(raw_input("Enter initial X position(meters): "))
X_array.append(X)

dt = 0.034

# ============================================
# Loop for Y
t_y = 0
t_array.append(t_y)
while True:
    dVydt = -9.8 - (0.5 * Vy * abs(Vy) * 0.47 * 1.225 * 2 * pi * 0.01905**2) / 0.02325
    Y += Vy * dt
    Vy += dVydt * dt
    Vy_array.append(Vy)
    Y_array.append(Y)
    t_y += dt
    t_array.append(t_y)
    # Check when ball hits ground
    if Y <= 0:
        break

# ============================================
# Loop for X
t_x = dt # why do we need to change this to dt?
while True:
    dVxdt = -(0.5 * Vx**2 * 0.47 * 1.225 * 2 * pi * 0.01905**2) / 0.02325
    X += Vx * dt
    Vx += dVxdt * dt
    Vx_array.append(Vx)
    X_array.append(X)
    # Check when ball hits ground
    if t_x == t_y:
        break
    else:
        t_x += dt

print len(X_array)
print len(Y_array)

# ============================================
# plot
plt.plot(X_array, Y_array)
plt.show()
# ============================================
