# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:37:38 2022

@author: maria
"""
"""
this is to compare how well the calibration worked by applying a linear regression model
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#support functions (should be placed in a separate file eventually)

#normalizing the array
def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


#files location

#files
files = [r"C:\Users\LABadmin\Desktop\Red\2022-10-24\Red7.bin",
         r"C:\Users\LABadmin\Desktop\Green\2022-10-24\Green7.bin",
         r"C:\Users\LABadmin\Desktop\Blue\2022-10-24\Blue7.bin"]

#%% Plot photodiode trace for red, green and blue 
    
start = 4000
step = 2000
end = 22000
arrays = list()
fig, axs = plt.subplots(1, 1, figsize=(15, 9))
for item in files:
    temp = np.fromfile(item,dtype='float64')    
    temp = normalize_data(temp)
    axs.plot(temp)
    temp = np.reshape(temp[start:end:1], (-1,step))
    arrays.append(temp)
    axs.legend(files)

#%%Plot mean luminance for each step per color

fig, axs = plt.subplots(1, 3, figsize=(15, 9))
axs[0].plot(np.mean(arrays[0],1),'o', color= "red")
axs[1].plot(np.mean(arrays[1],1),'o', color="green")
axs[2].plot(np.mean(arrays[2],1),'o', color= "blue")


#%%All traces in the same plot
fig, axs = plt.subplots(1, 1, figsize=(15, 9))
axs.plot(np.mean(arrays[0],1),color= "red")
axs.plot(np.mean(arrays[1],1),color="green")
axs.plot(np.mean(arrays[2],1),color= "blue")


#%% Linear reg evaluation

x= np.array([0,1,2,3,4,5,6,7,8]).reshape((-1,1))

for ind,colors in enumerate(['red','green','blue']):
    color= np.mean(arrays[ind],1)
    model = LinearRegression().fit(x, color)
    r_sq = model.score(x, color)
    print(f'coefficient of determination {colors}: {r_sq}' )







