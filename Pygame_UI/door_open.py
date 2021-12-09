import sys
import pygame
from pygame.locals import QUIT

width = 800
height = 800
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
screen.fill(color_bg)

# font
dead_font = pygame.font.SysFont(None, 60)

clock = pygame.time.Clock()

# set rectangle: Rect(left, top, width, height)


door_1_left = pygame.Rect(width, barSize, 0, height)
door_1_x ,door_1_y = (400,500)
door_1_right = pygame.Rect(width, barSize, 0, height)
door_1_x_l ,door_1_y_l = (400,500)
# pygame.draw.rect(screen, color_darkGray, door_1_shadow)
pygame.display.update()

while running:
    clock.tick(10) # 30 exe/secs
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
   
    # set door
    if door_1_left.w <= 200 and door_1_right.w <=200:
        door_1_x -= del_x
        door_1_left.center = (door_1_x, door_1_y)
        door_1_left.w += del_x
        door_1_x_l += del_x
        door_1_right.center = (door_1_x_l, door_1_y_l)
        door_1_right.w += del_x
        print(door_1_left.w)
    # Draw
    pygame.draw.rect(screen, color_white, door_1_left)
    pygame.draw.rect(screen, color_white, door_1_right)
    
    pygame.display.update()