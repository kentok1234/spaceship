import pygame
from pygame.locals import *
import random

# Inisialisasi game
pygame.init ()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# Set icon, title and screen
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Spaceship')
background = pygame.image.load('background.jpeg')


# Set space and enemy
# space
spaceship = pygame.image.load('asset\images\ship.png')
spPosX = (width - spaceship.get_width()) / 2
spPosY = 450
changeX = 0
changeY = 0

def ship(img, x, y):
    screen.blit(img, (x, y))

# enemy
alien = pygame.image.load('asset\images\\alien.png')
enemyX = random.randint(0, 500)
enemyY = -32
e_move_X = 1
e_move_Y = 0.05

def enemy(img, x, y):
    screen.blit(img, (x, y))

# Game running
running = True
while running:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Movement
        #Key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeX = 0.5
            if event.key == pygame.K_LEFT:
                changeX = -0.5
            if event.key == pygame.K_UP:
                changeY = -0.5
            if event.key == pygame.K_DOWN:
                changeY = 0.5
        #Key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeY = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                changeX = 0

        # Game quit
        if event.type == pygame.QUIT:
            running = False

    spPosX += changeX
    spPosY += changeY

    # collision ship dengan screen x
    if spPosX > (500 - (spaceship.get_width() / 2)):
        spPosX = 500 - (spaceship.get_width() / 2)
    elif spPosX < (0 - (spaceship.get_width() / 2)):
        spPosX = 0 - (spaceship.get_width() / 2)
    # collision ship dengan screen y
    if spPosY > (500 - spaceship.get_height()):
        spPosY = 500 - spaceship.get_height()
    if spPosY < 0:
        spPosY = 0
    
    # enemy move:
    enemyX += e_move_X
    enemyY += e_move_Y
    if enemyX > (500 - alien.get_width()):
        enemyX = 500 - alien.get_width()
        e_move_X = -1
    elif enemyX < 0:
        enemyX = 0
        e_move_X = 1

    ship(spaceship, spPosX, spPosY)
    enemy(alien, enemyX, enemyY)
    pygame.display.update()