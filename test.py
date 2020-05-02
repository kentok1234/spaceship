import pygame
from pygame.locals import *
import random

pygame.init()

# Layar game
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# musuh
alien_num = 5
alien = pygame.image.load('asset\images\\alien.png')
alien_group = []
alien_X = []
alien_Y = []
alien_moveX = []
alien_moveY = []
e_respawnX = random.randint(0,500)
e_respawnY = -(alien.get_width()*alien_num)
distance = 0

for i in range(alien_num):
    alien_group.append(alien)
    alien_X.append(e_respawnX+distance)
    alien_Y.append(e_respawnY+distance) 
    alien_moveX.append(0.1)
    alien_moveY.append(0.01) 
    distance += 32
def draw_alien(img, x, y, i):
    screen.blit(img[i], (x[i], y[i]))

running = True
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # enemy move:
    for i in range(alien_num):
        alien_X[i] += alien_moveX[i]
        alien_Y[i] += alien_moveY[i]  
        if alien_X[i] > (500 - alien_group[i].get_width()):
            alien_X[i] = 500 - alien_group[i].get_width()
            alien_moveX[i] = -0.1
        elif alien_X[i] < 0:
            alien_X[i] = 0
            alien_moveX[i] = 0.1  
        draw_alien(alien_group, alien_X, alien_Y, i)
    pygame.display.update()