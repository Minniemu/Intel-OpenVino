import sys
import pygame
from pygame import image
from pygame.locals import QUIT

width = 800
height = 746.5
barSize = 150
doorSize = 400
del_x = 5

color_bg = (0, 0, 0)
color_white = (255, 255, 255)
color_lightGray = (200, 200, 200)
color_darkGray = (100, 100, 100)

running = True

# initialize
pygame.init()

# build screen
screen = pygame.display.set_mode((1000, 1000))
# set window title
pygame.display.set_caption("elevator")
# fill window
screen.fill(color_lightGray)

# font
dead_font = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

#load image
elevator = pygame.image.load('image/ele.png')
elevator.convert()
screen.blit(elevator, (0,0))

# set rectangle: Rect(left, top, width, height)
door_1 = pygame.Rect(width, barSize, 0, height)
door_1_x ,door_1_y = (469,603)

pygame.display.update()

while running:
    clock.tick(10) # 30 exe/secs
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
   
    # set door
    if door_1.w <= 562:
        door_1.center = (door_1_x, door_1_y)
        door_1.w += del_x
    
    # door_1.width = 50
    # Draw
    pygame.draw.rect(screen, color_white, door_1)
    
    pygame.display.update()