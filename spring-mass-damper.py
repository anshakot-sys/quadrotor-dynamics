#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 21:00:00 2025

@author: anshakottapalli
"""


# import python libraries for math/plotting
import numpy as np
import matplotlib.pyplot as plt

# define parameters
m = 1 # mass
k = 1 # spring coefficient
c = 0 # dampening coefficient

# define gains
Kp = 1 # proportional gain
Kd = 4 # derivative gain

Acl = np.array([[0,1],[(-k/m - Kp/m),(-c/m - Kd/m)]]) # closed_loop system matrix

# define initial condition
p0 = 1 # position
v0 = 1 # velocity

x0 = np.array([[p0],[v0]]) # initial state vector

# define the time vector
t0 = 0 # initial time (seconds)
tf = 40 # final time
dt = 0.001 # time step
N = int(tf/dt) # number of time steps

# create a time vector
time_vector = np.linspace(t0,tf,num=N)

# numerical integration with Newton's Method
x_k = x0 # set the initial condition as the current state
x_save = np.zeros((x0.shape[0],40000)).astype(float) #state history
x_save[:,0] = x_k.transpose() # transpose flips the vector/matrix

# fill in x_save at each step using a for loop
for k in range(time_vector.shape[0]-1):
    x_k_dot = np.dot(Acl,x_k)
    
    x_kk = x_k_dot*dt + x_k # update step
    
    x_save[:,k+1] = x_kk.transpose()
    
    x_k = x_kk
    
### Plotting
plt.plot(time_vector,x_save[0,:]) # plot position
plt.plot(time_vector,x_save[1,:]) # plot velocity

plt.title("Closed-Loop Spring Mass Damper System")
plt.xlabel("time (sec.)")
plt.ylabel("system states")
plt.legend(['Position (m.)','Velocity (m./sec.)'])
plt.minorticks_on()
plt.grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)