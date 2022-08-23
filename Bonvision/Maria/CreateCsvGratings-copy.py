# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:31:14 2021

@author: Liad Baruchin
"""

import csv
import os
import numpy as np

rangeX, rangeY, Dia, White = 0,0,0,0

header = ['Orientations','Spatial Frequencies','Temporal Frequencies','Contrasts']




data = np.array([0,0,0,0]).T
### Following: Visual Receptive Field Properties of Neurons in the Superficial Superior Colliculus of the Mouse

####Changing Spatial Frequencies

fileName = 'csvGratings'
orientations = [30, 60, 90, 120, 150, 180, 210, 240,270, 300, 330, 360]#np.arange(0,360,30)#np.array([0,45,90,135,180,225,270,315])
Sfrequencies = [0.08]#[0.01,0.02,0.04,0.08,0.16,0.32]
Tfrequencies = [2]#[0.5,1,2,4,8,16,32]#[1,2,5,10,20,40]#[0.5,1,2,4,8,16,32]
contrasts = [1]#[0,0.25,0.5,1]

#########################################################################################

####Changing Temporal Frequencies

# fileName = 'csvGratingsTemporalChange'
# orientations = [0, 90, 180,270]#np.arange(0,360,30)#np.array([0,45,90,135,180,225,270,315])
# Sfrequencies = [0.08]
# Tfrequencies = [0.5, 1, 2, 4, 8 ,16]#[0.5,1,2,4,8,16,32]#[1,2,5,10,20,40]#[0.5,1,2,4,8,16,32]
# contrasts = [1]#[0,0.25,0.5,1]

#########################################################################################

####Changing Contrast

# fileName = 'csvGratingsContrastChange'
# orientations = [0, 90, 180,270]#np.arange(0,360,30)#np.array([0,45,90,135,180,225,270,315])
# Sfrequencies = [0.08]
# Tfrequencies = [2]#[1,2,5,10,20,40]#[0.5,1,2,4,8,16,32]
# contrasts = [0,0.125,0.25,0.5,0.75,1]

#########################################################################################

# orientations = [0, 90, 180,270]#np.arange(0,360,30)#np.array([0,45,90,135,180,225,270,315])
# Sfrequencies = [0.08]#[0.01,0.02,0.05,0.1,0.5,1]#[0.01,0.02,0.05,0.1,0.2,0.4,0.8]
# Tfrequencies = [2]#[0.5,1,2,4,8,16,32]#[1,2,5,10,20,40]#[0.5,1,2,4,8,16,32]
# contrasts = [0,0.125,0.25,0.5,0.75,1]#[1]#[0,0.25,0.5,1]


filePath = 'D:\Experimental-Protocols\\' +fileName + '.csv'
# # Create Data
# os.getcwd()
# contents = []
# with open('C:\\BonsaiExamples\\settingStationary.csv', mode='r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
    
#     for row in csv_reader:
#         contents.append(row)
# settings= np.array(contents[1])
# xs = settings[0].astype(int)
# xe = settings[1].astype(int)
# ys = settings[2].astype(int)
# ye = settings[3].astype(int)
# skip = settings[4].astype(int)
# sizes = np.array(settings[5].split(',')).astype(int)
# speeds = np.array(settings[6].split(',')).astype(int)
# xRange = np.arange(xs,xe,skip)
# yRange = np.arange(ys,ye,skip)
# sizeRange = sizes
# speedRange = speeds # degress per second      

for ori in orientations:
    for sf in Sfrequencies: 
        for tf in Tfrequencies:  
            for c in contrasts:                    
                data = np.vstack((data,[ori,sf,tf,c]))           
            
data = np.unique(data[1:,:],axis=0)
totTime = len(data)*2
print('Total Time: ' + str((totTime + totTime*4)/60) +' Minutes')
              

with open(filePath, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
    
