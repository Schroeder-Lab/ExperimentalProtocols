# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:31:14 2021

@author: liad0
"""

import csv
import numpy as np

rangeX, rangeY, Dia, White = 0,0,0,0

header = ['X_Start','X_End','Y_Start','Y_End','Size','Duration']

filePath = 'C:\BonsaiExamples\csvSampleMoving.csv'

data = np.array([0,0,0,0,0,0]).T

sizeRange = [1,2]
xRange = np.arange(15,45,5)
yRange = np.arange(-10,40,5)
speedRange = [10,20, 40, 80, 160, 320] # degress per second

# Create Data

for sp in speedRange:
    for s in sizeRange:
        xRange_ = np.arange(xRange[0],xRange[-1],max(xRange[1]-xRange[0],s/2))
        for x in xRange:
            # Circles flying straight
            # Different X position starting top and then bottom
            dur = abs(yRange[-1]-yRange[0])/sp
            if (dur>0):
                data = np.vstack((data,[x,x,yRange[0],yRange[-1],s,dur]))
                data = np.vstack((data,[x,x,yRange[-1],yRange[0],s,dur]))
            
            # Different X positions start, fly diagonally
            # Up   
            xDist = x-xRange[0]
            dur = (np.sqrt(2)*xDist)/sp
            if (dur>0):
                data = np.vstack((data,[x,xRange[0],yRange[0],yRange[0]+xDist,s,dur]))
            xDist = abs(x-xRange[-1])
            dur = (np.sqrt(2)*xDist)/sp
            if (dur>0):
                data = np.vstack((data,[x,xRange[-1],yRange[0],yRange[0]+xDist,s,dur]))
            # Down
            xDist = x-xRange[0]
            dur = (np.sqrt(2)*xDist)/sp
            if (dur>0):
                data = np.vstack((data,[x,xRange[0],yRange[-1],yRange[0],s,dur]))
            xDist = abs(x-xRange[-1])
            dur = (np.sqrt(2)*xDist)/sp
            if (dur>0):
                data = np.vstack((data,[x,xRange[-1],yRange[-1],yRange[0],s,dur]))
        for y in yRange:
            # Different Y position starting left and then right
            dur = abs(yRange[-1]-yRange[0])/sp
            if (dur>0):
                data = np.vstack((data,[xRange[0],xRange[-1],y,y,s,dur]))
                data = np.vstack((data,[xRange[-1],xRange[0],y,y,s,dur]))
            
            # Different Y positions start, fly diagonally
            # Down
            yDist = x-yRange[0]
            dur = (np.sqrt(2)*yDist)/sp
            if (dur>0):
                data = np.vstack((data,[xRange[0],xRange[-1],y,yRange[0],s,dur]))
            xDist = abs(x-yRange[-1])
            dur = (np.sqrt(2)*yDist)/sp
            if (dur>0):
                data = np.vstack((data,[xRange[0],xRange[-1],y,yRange[-1],s,dur]))
            # Up
            yDist = x-yRange[0]
            dur = (np.sqrt(2)*yDist)/sp
            if (dur>0):
                data = np.vstack((data,[xRange[-1],xRange[0],y,yRange[0],s,dur]))
            xDist = abs(x-yRange[-1])
            dur = (np.sqrt(2)*yDist)/sp
            if (dur>0):
                data = np.vstack((data,[xRange[-1],xRange[0],y,yRange[-1],s,dur]))

totTime = np.sum(data[:,-1])
print('Total Time: ' + str(totTime/60) +' Minutes')
              

with open(filePath, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)