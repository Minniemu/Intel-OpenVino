from time import time
import pygame
from pygame import image
from pygame.locals import QUIT
import keyboard
import time
width = 800
height = 507
barSize = 150
doorSize = 400
del_x = 5

#Color RGB
color_bg = (0, 0, 0)
color_white = (255, 255, 255)
color_lightGray = (200, 200, 200)
color_darkGray = (100, 100, 100)
color_red = (255,0,0)

running = True
# set rectangle: Rect(left, top, width, height)
door_1 = pygame.Rect(width, barSize, 0, height)
door_1_x ,door_1_y = (316, 409)
door_1.center = (door_1_x, door_1_y)
# Elevator State

# global curr_floor, up_down, floor_state, floor_x, floor_y
floor_x = 800
floor_y = 90
curr_floor = 1
up_down = 'up'
status = {'o':False, 'c':False, '1':True, '2':False, '3':False, '4':False, '5':True, '6':False, '7':False, '8':False, '9':False, '10':False}
floor_state = [0 for i in range(11)]
# Traverse Status Dictionary
def traverse():
    #load image
    screen.fill(color_white)
    elevator = pygame.image.load('.\Pygame_UI\elevator_1.png')
    elevator.convert()
    screen.blit(elevator, (0,0))
    #Word
    font = pygame.font.Font('freesansbold.ttf', 32)
    x = 800
    y = 150
    text = font.render('Input Floor', True, color_bg)
    pygame.draw.rect(screen, color_bg,[735, 75, 300, 60], 5)
    screen.blit(text, (floor_x, floor_y))
    for k in status:
        # print('key = '+k+ ',value = '+str(status[k]))
        if k != 'o' and k != 'c':
            if status[k] == True:
                floor_state[int(k)] = 1
            else:
                floor_state[int(k)] = 0
    if up_down == 'up':
        for i in range(1,11):
            if floor_state[i] == 1:
                temp = font.render(str(i), True,color_bg)
                screen.blit(temp, (x+ 80, y) )
                y += 40
    else :
        for i in range(10,0,-1):
            if floor_state[i] == 1:
                temp = font.render(str(i), True,color_bg)
                screen.blit(temp, (x+ 80, y) )
                y += 40
                    
# Panel Control
def panel_control():
    if up_down == 'up':
        for i in range(curr_floor,11):
            traverse()
            font = pygame.font.Font('freesansbold.ttf', 58)
            temp = font.render(str(i), True, color_red)
            screen.blit(temp, (310, 75) )
            pygame.display.update()
            clock.tick(10)
            time.sleep(1)
            if floor_state[i] == 1:
                Open_Close(i)
                status[str(i)] = False

            
# Scheduling function
def input_floor(screen, status):
    traverse()
    panel_control()

# Door Open and Close
def Open_Close(floor):
    # Panel Floor Number
    font = pygame.font.Font('freesansbold.ttf', 58)
    temp = font.render(str(floor), True, color_red)
    # Open Door
    while door_1.w <= 379.5:
        screen.blit(temp, (310, 75) )
        pygame.display.update()
        screen.blit(elevator, (0,0))
        door_1.center = (door_1_x, door_1_y)
        door_1.w += del_x
        pygame.draw.rect(screen, color_white, door_1)
        clock.tick(30)
        pygame.display.update()
    screen.blit(temp, (310, 75) )
    pygame.display.update()
    time.sleep(1)
    # Close Door
    while door_1.w >= 0:
        screen.blit(temp, (310, 75) )
        pygame.display.update()
        screen.blit(elevator, (0,0))
        door_1.center = (door_1_x, door_1_y)
        door_1.w -= del_x
        pygame.draw.rect(screen, color_white, door_1)
        clock.tick(30)
        pygame.display.update()
    screen.blit(temp, (310, 75) )
    pygame.display.update()
    time.sleep(1)

if __name__ == '__main__':
    # initialize
    pygame.init()

    # build screen
    global screen 
    screen = pygame.display.set_mode((1300, 700))
    # set window title
    pygame.display.set_caption("elevator")
    # fill window
    screen.fill(color_white)

    # font
    dead_font = pygame.font.SysFont(None, 60)
    clock = pygame.time.Clock()

    #load image
    elevator = pygame.image.load('.\Pygame_UI\elevator_1.png')
    elevator.convert()
    screen.blit(elevator, (0,0))

    
    # pygame.display.update()
    switch = 'idle'
    
    input_floor(screen, status)

    while running:
        clock.tick(60) # 30 exe/secs
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        if keyboard.is_pressed('o'):
            switch = 'open'
        elif keyboard.is_pressed('c'):
            switch = 'close'
        # set door
        input_floor(screen, status)
        
        pygame.display.update()