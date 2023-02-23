#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pygame')


# In[ ]:


import numpy as np
import math
import pygame
import sys
pygame.init()

screen_width = 1000 # 스크린 가로길이
screen_height = 500 # 스크린 세로길이
screen = pygame.display.set_mode((screen_width, screen_height)) #스크린 생성
pygame.display.set_caption("Small Piano")





# Initialize an empty numpy array with the desired shape
boxinf = np.zeros((12, 5)) # 피아노 건반 위치에 대한 정보

# Assign the values from the provided list of lists
boxinf[:, 0] = [0, 20, 30, 50, 60, 90, 110, 120, 140, 150, 170, 180]
boxinf[:, 2] = [30, 20, 30, 20, 30, 30, 20, 30, 20, 30, 20, 30]
boxinf[:, 3] = [100, 60, 100, 60, 100, 100, 60, 100, 60, 100, 60, 100]
boxinf[:, 4] = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]


# Repeat the array for 12 rows

pianoloc = np.zeros((84, 4)) # 피아노 건반 위치에 대한 정보

for i in range(7):
    for j in range(12):
        pianoloc[12*i+j][0]=(boxinf[j][0]+210*i)/2
        pianoloc[12*i+j][1]=boxinf[j][1]/2
        pianoloc[12*i+j][2]=boxinf[j][2]/2
        pianoloc[12*i+j][3]=boxinf[j][3]/2


screen.fill((255,255,255)) #스크린 흰색으로 도배

#건반이 시작하는 왼쪽 위 꼭짓점 위치
start_x=100 
start_y=400

pressed = np.zeros((84))

def draw_piano():
    #흰 건반 색칠
    for i in range(84):  # Add a nested loop to iterate over the rows of boxinf
        if boxinf[i%12][4] == 0:
            if pressed[i] == 1:
                pygame.draw.rect(screen,(0,255,0), (start_x+pianoloc[i][0], start_y+pianoloc[i][1], pianoloc[i][2], pianoloc[i][3]))
            else:
                pygame.draw.rect(screen, (0,0,0), (start_x+pianoloc[i][0], start_y+pianoloc[i][1], pianoloc[i][2], pianoloc[i][3]), 1)
    #검은 건반 색칠
    for i in range(84):  # Add a nested loop to iterate over the rows of boxinf
        if boxinf[i%12][4] == 1:
            if pressed[i] == 1:
                pygame.draw.rect(screen, (0,255,0), (start_x+pianoloc[i][0], start_y+pianoloc[i][1], pianoloc[i][2], pianoloc[i][3]))
            else:
                pygame.draw.rect(screen, (0,0,0), (start_x+pianoloc[i][0], start_y+pianoloc[i][1], pianoloc[i][2], pianoloc[i][3]))

#pygame.draw.rect(screen, (0,0,0), (100,200,500,300))
pygame.display.flip() # update the screen

done = False
clock = pygame.time.Clock()
c_sound = pygame.mixer.Sound("pianowav\FX_piano01.wav")
c3_sound = pygame.mixer.Sound("pianowav\FX_piano02.wav")
d_sound = pygame.mixer.Sound("pianowav\FX_piano03.wav")
d3_sound = pygame.mixer.Sound("pianowav\FX_piano04.wav")
e_sound = pygame.mixer.Sound("pianowav\FX_piano05.wav")
f_sound = pygame.mixer.Sound("pianowav\FX_piano06.wav")
f3_sound = pygame.mixer.Sound("pianowav\FX_piano07.wav")
g_sound = pygame.mixer.Sound("pianowav\FX_piano08.wav")
g3_sound = pygame.mixer.Sound("pianowav\FX_piano09.wav")
a_sound = pygame.mixer.Sound("pianowav\FX_piano10.wav")
a3_sound = pygame.mixer.Sound("pianowav\FX_piano11.wav")
b_sound = pygame.mixer.Sound("pianowav\FX_piano12.wav")
while not done:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pressed[36] = 1
                c_sound.play()
            elif event.key == pygame.K_w:
                pressed[37] = 1
                c3_sound.play()
            elif event.key == pygame.K_e:
                pressed[38] = 1
                d_sound.play()
            elif event.key == pygame.K_r:
                pressed[39] = 1
                d3_sound.play()
            elif event.key == pygame.K_t:
                pressed[40] = 1
                e_sound.play()
            elif event.key == pygame.K_y:
                pressed[41] = 1
                f_sound.play()
            elif event.key == pygame.K_u:
                pressed[42] = 1
                f3_sound.play()
            elif event.key == pygame.K_i:
                pressed[43] = 1
                g_sound.play()
            elif event.key == pygame.K_o:
                pressed[44] = 1
                g3_sound.play()
            elif event.key == pygame.K_p:
                pressed[45] = 1
                a_sound.play()
            elif event.key == pygame.K_LEFTBRACKET:
                pressed[46] = 1
                a3_sound.play()
            elif event.key == pygame.K_RIGHTBRACKET:
                pressed[47] = 1
                b_sound.play()
            elif event.key == pygame.K_SPACE:
                pygame.quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pressed[36] = 0
            elif event.key == pygame.K_w:
                pressed[37] = 0
            elif event.key == pygame.K_e:
                pressed[38] = 0
            elif event.key == pygame.K_r:
                pressed[39] = 0
            elif event.key == pygame.K_t:
                pressed[40] = 0
            elif event.key == pygame.K_y:
                pressed[41] = 0
            elif event.key == pygame.K_u:
                pressed[42] = 0
            elif event.key == pygame.K_i:
                pressed[43] = 0
            elif event.key == pygame.K_o:
                pressed[44] = 0
            elif event.key == pygame.K_p:
                pressed[45] = 0
            elif event.key == pygame.K_LEFTBRACKET:
                pressed[46] = 0
            elif event.key == pygame.K_RIGHTBRACKET:
                pressed[47] = 0
    draw_piano()
    pygame.display.flip()
    clock.tick(60)


# In[ ]:


# In[ ]:





# In[ ]:




