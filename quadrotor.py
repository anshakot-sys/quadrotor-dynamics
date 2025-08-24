#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 12:15:06 2025

@author: anshakottapalli
"""
# import python libraries for math/plotting
import numpy as np
import matplotlib.pyplot as plt

# constants 
m = 0.18        # mass (kg)
Ixx = 0.00025   # moment of inertia (kg*m^2)
g = 9.81        # gravity (m/s^2)

# control gains 
Kp_y = 0.4
Kv_y = 1.0
Kp_z = 0.4
Kv_z = 1.0
Kp_phi = 18.0
Kv_phi = 5.0

## Test Cases

# Case:
u1 = 2*m*g
u2 = 0.01

# define initial condition
x0 = np.array([[0.0], [0.0], [0.0], [0.0], [0.0], [0.0]])  # Initial state

# define the time vector
t0 = 0 # initial time (seconds)
tf = 20 # final time
dt = 0.001 # time step
N = int(tf/dt) # number of time steps

# create a time vector
time_vector = np.linspace(t0,tf,num=N)

# numerical integration with Newton's Method
x_k = x0 # set the initial condition as the current state
x_save = np.zeros((x0.shape[0],int(tf/dt))).astype(float) #state history
x_save[:,0] = x_k.transpose() # transpose flips the vector/matrix

x_k_dot = np.zeros((x0.shape[0],x0.shape[1])).astype(float) #state history

# fill in x_save at each step using a for loop
for k in range(time_vector.shape[0]-1):
    
    ## if you choose to proceed with feedback control
    # this is where you'd compute u1 and u2 via the feedback control law

    x_k_dot[0] = x_k[3]
    x_k_dot[1] = x_k[4]
    x_k_dot[2] = x_k[5]
    x_k_dot[3] = (-1/m)*u1*np.sin(x_k[2])
    x_k_dot[4] = (1/m)*u1*np.cos(x_k[2]) - g
    x_k_dot[5] = (1/Ixx)*u2

    x_kk = x_k_dot*dt + x_k # update step
    
    x_save[:,k+1] = x_kk.transpose()
    
    x_k = x_kk
    
### Plotting all states
#plt.plot(time_vector,x_save[0,:]) # plot y
#plt.plot(time_vector,x_save[1,:]) # plot z
#plt.plot(time_vector,x_save[2,:]) # plot phi
#plt.plot(time_vector,x_save[3,:]) # plot y_dot
#plt.plot(time_vector,x_save[4,:]) # plot z_dot
#plt.plot(time_vector,x_save[5,:]) # plot phi_dot

#plt.xlabel('Time (s)')
#plt.ylabel('States')
#plt.legend(['y (horizontal)','z (vertical)','phi (angle)'])
#plt.title('2D Quadrotor Linearized Simulation')

### Plotting y vs z (trajectory)
plt.plot(x_save[0,:],x_save[1,:]) # plot y

plt.xlabel('y')
plt.ylabel('z')
#plt.legend(['y (horizontal)','z (vertical)','phi (angle)'])
plt.title('Quadrotor Trajectory')

plt.minorticks_on()
plt.grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)