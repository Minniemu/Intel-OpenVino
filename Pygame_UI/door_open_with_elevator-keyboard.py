import pygame
from pygame import image
from pygame.locals import QUIT
import keyboard
import scheduling
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
def input_floor(screen, status):
    floor_x, floor_y = (1050,105)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Input Floor', True, color_bg)
    pygame.draw.rect(screen, color_bg,[990, 90, 300, 60], 5)
    screen.blit(text, (floor_x, floor_y))
    floor_y += 60
    for k in status:
        # print('key = '+k+ ',value = '+str(status[k]))
        if status[k] == True:
            temp = font.render(str(k), True,color_bg)
            screen.blit(temp, (floor_x+ 80, floor_y) )
            floor_y += 40
# initialize
pygame.init()

# build screen
screen = pygame.display.set_mode((1500, 1000))
# set window title
pygame.display.set_caption("elevator")
# fill window
screen.fill(color_white)

# font
dead_font = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

#load image
elevator = pygame.image.load('./image/ele.png')
elevator.convert()
screen.blit(elevator, (0,0))

# set rectangle: Rect(left, top, width, height)
door_1 = pygame.Rect(width, barSize, 0, height)
door_1_x ,door_1_y = (470,603)
door_1.center = (door_1_x, door_1_y)
# pygame.display.update()
switch = 'open'
status = {'o':False, 'c':False, '1':False, '2':True, '3':False, '4':True, '5':False, '6':False, '7':False, '8':False, '9':True, '10':False}
input_floor(screen, status)





while running:
    clock.tick(60) # 30 exe/secs
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
   
    # set door
    if switch == 'open':
        if door_1.w <= 562:
            screen.blit(elevator, (0,0))
            door_1.center = (door_1_x, door_1_y)
            door_1.w += del_x
            
    elif switch == 'close':
        if door_1.w >= 0:
            screen.blit(elevator, (0,0))
            door_1.center = (door_1_x, door_1_y)
            door_1.w -= del_x
    pygame.draw.rect(screen, color_white, door_1)
    pygame.display.update()