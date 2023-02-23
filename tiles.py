#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import math
import pygame
import sys
pygame.init()

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))



# Initialize an empty numpy array with the desired shape
boxinf = np.zeros((12, 5))

# Assign the values from the provided list of lists
boxinf[:, 0] = [0, 20, 30, 50, 60, 90, 110, 120, 140, 150, 170, 180]
boxinf[:, 2] = [30, 20, 30, 20, 30, 30, 20, 30, 20, 30, 20, 30]
boxinf[:, 3] = [100, 60, 100, 60, 100, 100, 60, 100, 60, 100, 60, 100]
boxinf[:, 4] = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]


# Repeat the array for 12 rows

pianoloc = np.zeros((84, 4))

for i in range(7):
    for j in range(12):
        pianoloc[12*i+j][0]=(boxinf[j][0]+210*i)/2
        pianoloc[12*i+j][1]=boxinf[j][1]/2
        pianoloc[12*i+j][2]=boxinf[j][2]/2
        pianoloc[12*i+j][3]=boxinf[j][3]/2


screen.fill((255,255,255))

start_x=100
start_y=400

for i in range(84):
    print(i,pianoloc[i][0],pianoloc[i][1],pianoloc[i][2],pianoloc[i][3])
    
for i in range(84):  # Add a nested loop to iterate over the rows of boxinf
        if boxinf[i%12][4] == 1:
            pygame.draw.rect(screen, (0,0,0), (start_x+pianoloc[i][0], start_y+pianoloc[i][1], pianoloc[i][2], pianoloc[i][3]))

for i in range(84):  # Add a nested loop to iterate over the rows of boxinf
        if boxinf[i%12][4] == 0:
            pygame.draw.rect(screen, (0,0,0), (start_x+pianoloc[i][0], start_y+pianoloc[i][1], pianoloc[i][2], pianoloc[i][3]), 1)
       
#pygame.draw.rect(screen, (0,0,0), (100,200,500,300))
pygame.display.flip() # update the screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# In[ ]:




