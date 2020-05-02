import pygame
from pygame.locals import *
import random

# Inisialisasi game
pygame.init()

clock = pygame.time.Clock()
frame_per_second = 60
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# set default font
font_default = pygame.font.get_default_font()
font = pygame.font.Font(font_default, 12)

#print fps
print_fps = font.render('fps : {}'.format(int(clock.get_fps())), True, (255,255,255))

# Set icon, title and screen
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Spaceship')
background = pygame.image.load('background.jpeg')


# Set space and enemy
# space
spaceship = pygame.image.load('asset\images\ship.png')
shipX = (width - spaceship.get_width()) / 2
shipY = 450
s_move_X = 0
s_move_Y = 0

def ship(img, x, y):
    screen.blit(img, (x, y))

# enemy
alien_num = 5
alien = pygame.image.load('asset\images\\alien.png')
alien_group = []
alien_X = []
alien_Y = []
alien_moveX = []
alien_moveY = []
e_respawnX = random.randint(0,500)
e_respawnY = -(alien.get_width()*alien_num)
distanceX = 0
distanceY = 0

for i in range(alien_num):
    alien_group.append(alien)
    alien_X.append(e_respawnX+distanceX)
    alien_Y.append(e_respawnY+distanceY) 
    alien_moveX.append(0.5)
    alien_moveY.append(0.1) 
    distanceX += 64
    distanceY += 32
def draw_alien(img, x, y, i):
    screen.blit(img[i], (x[i], y[i]))

# bullet
bullet_width = 5
bullet_height = 5
bullet_X = 0
bullet_Y = 0
speed_bullet = 1
bullet_state = 'ready'
def draw_bullet(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, bullet_width, bullet_height))
def ship_fire(x, y):
    bullet_state = 'fire'
    draw_bullet(x, y)

# Game running
running = True
while running:

    

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Movement
        #Key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                s_move_X = 0.5
            if event.key == pygame.K_LEFT:
                s_move_X = -0.5
            if event.key == pygame.K_UP:
                s_move_Y = -0.5
            if event.key == pygame.K_DOWN:
                s_move_Y = 0.5
            if event.key == pygame.K_SPACE:
                bullet_X = shipX + (spaceship.get_width() /2) - 2
                bullet_Y = shipY
                bullet_state = 'fire'
                ship_fire(bullet_X, bullet_Y)
        #Key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                s_move_Y = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                s_move_X = 0

        # Game quit
        if event.type == pygame.QUIT:
            running = False

    shipX += s_move_X
    shipY += s_move_Y

    # collision ship dengan screen x
    if shipX > (500 - (spaceship.get_width() / 2)):
        shipX = 500 - (spaceship.get_width() / 2)
    elif shipX < (0 - (spaceship.get_width() / 2)):
        shipX = 0 - (spaceship.get_width() / 2)
    # collision ship dengan screen y
    if shipY > (500 - spaceship.get_height()):
        shipY = 500 - spaceship.get_height()
    if shipY < 0:
        shipY = 0
    
    ship(spaceship, shipX, shipY)

    # enemy move:
    for i in range(alien_num):
        alien_X[i] += alien_moveX[i]
        alien_Y[i] += alien_moveY[i]  
        if alien_X[i] > (500 - alien_group[i].get_width()):
            alien_X[i] = 500 - alien_group[i].get_width()
            alien_moveX[i] = -0.5
        elif alien_X[i] < 0:
            alien_X[i] = 0
            alien_moveX[i] = 0.5  
        draw_alien(alien_group, alien_X, alien_Y, i)
    
    # bullet move
    if bullet_state == 'fire':
        bullet_Y -= speed_bullet
        ship_fire(bullet_X, bullet_Y)

    screen.blit(print_fps, (0, 0)) 
    pygame.display.update()