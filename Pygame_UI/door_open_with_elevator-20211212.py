# Implement By Array
from time import time
import pygame
from pygame import image
from pygame.locals import QUIT
import keyboard
import time
width = 800
height = 722
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
door_1_x ,door_1_y = (456, 585)
door_1.center = (door_1_x, door_1_y)
# Panel Info.
panel_x1, panel_y1 = (450, 115)
panel_x2, panel_y2 = (795, 290)
# global curr_floor, up_down, floor_state, floor_x, floor_y
floor_x = 1050
floor_y = 105
curr_floor = 10
up_down = 'down'
status = {'o':False, 'c':False, '1':False, '2':True, '3':False, '4':False, '5':False, '6':True, '7':False, '8':False, '9':True, '10':False}
floor_state = [0 for i in range(11)]
flag = False
# Traverse Status Dictionary
def traverse():
    #load image
    screen.fill(color_white)
    elevator = pygame.image.load('D:\Intel-OpenVino\Pygame_UI\elevator_1.png')
    elevator.convert()
    screen.blit(elevator, (0,0))
    # Word
    x, y = (1050, 165)
    text = font_small.render('Input Floor', True, color_bg)
    pygame.draw.rect(screen, color_bg,[990, 90, 300, 60], 5)
    screen.blit(text, (floor_x, floor_y))
    # Transpose status dictionary to array
    for k in status:
        if k != 'o' and k != 'c':
            if status[k] == True:
                floor_state[int(k)] = 1
            else:
                floor_state[int(k)] = 0

    # Print the floor & Detect if the elevator should stop
    count = 0
    global flag
    if up_down == 'up': # UP
        for i in range(1,11):
            if floor_state[i] == 1:
                temp = font_small.render(str(i), True,color_bg)
                screen.blit(temp, (x+ 80, y) )
                y += 40
                if i > curr_floor:
                    count += 1
    else : #DOWN
        for i in range(10,0,-1):
            if floor_state[i] == 1:
                temp = font_small.render(str(i), True,color_bg)
                screen.blit(temp, (x+ 80, y) )
                y += 40
                if i < curr_floor:
                    count += 1
    if count == 0:
        flag = True
    else : 
        flag = False

# Panel Control
def panel_control():
    global up_down, curr_floor, flag
    if up_down == 'up' and not flag:
        for i in range(1,11):
            traverse()
            if flag :
                break
            temp = font_big.render(str(i), True, color_red)
            screen.blit(temp, (panel_x1, panel_y1))
            screen.blit(temp, (panel_x2, panel_y2))
            pygame.display.update()
            time.sleep(1)
            if floor_state[i] == 1:
                Open_Close(i)
                status[str(i)] = False
            curr_floor = i
            
        up_down = 'down'
    elif up_down == 'down' and not flag:
        for i in range(10,0,-1):
            traverse()
            if flag :
                break
            temp = font_big.render(str(i), True, color_red)
            screen.blit(temp, (panel_x1, panel_y1) )
            screen.blit(temp, (panel_x2, panel_y2))
            pygame.display.update()
            time.sleep(1)
            if floor_state[i] == 1:
                Open_Close(i)
                status[str(i)] = False
            curr_floor = i

        up_down = 'up'
    temp = font_big.render(str(curr_floor), True, color_red)
    screen.blit(temp, (panel_x1, panel_y1) )
    screen.blit(temp, (panel_x2, panel_y2))
    pygame.display.update()
            
# Scheduling function
def input_floor(screen, status):
    traverse()
    panel_control()

# Door Open and Close
def Open_Close(floor):
    # Panel Floor Number
    temp = font_big.render(str(floor), True, color_red)
    # Open Door
    while door_1.w <= 541:
        screen.blit(temp, (panel_x1, panel_y1))
        screen.blit(temp, (panel_x2, panel_y2))
        pygame.display.update()
        screen.blit(elevator, (0,0))
        door_1.center = (door_1_x, door_1_y)
        door_1.w += del_x
        pygame.draw.rect(screen, color_white, door_1)
        clock.tick(30)
        pygame.display.update()
    screen.blit(temp, (panel_x1, panel_y1))
    screen.blit(temp, (panel_x2, panel_y2))
    pygame.display.update()
    time.sleep(1)
    # Close Door
    while door_1.w >= 0:
        screen.blit(temp, (panel_x1, panel_y1))
        screen.blit(temp, (panel_x2, panel_y2))
        pygame.display.update()
        screen.blit(elevator, (0,0))
        door_1.center = (door_1_x, door_1_y)
        door_1.w -= del_x
        pygame.draw.rect(screen, color_white, door_1)
        clock.tick(30)
        pygame.display.update()
    screen.blit(temp, (panel_x1, panel_y1))
    screen.blit(temp, (panel_x2, panel_y2))
    pygame.display.update()
    time.sleep(1)

if __name__ == '__main__':
    # initialize
    pygame.init()

    # build screen
    global screen 
    screen = pygame.display.set_mode((1500, 1000))
    # set window title
    pygame.display.set_caption("elevator")
    # fill window
    screen.fill(color_white)
    #Font Info.
    font_small = pygame.font.Font('freesansbold.ttf', 32)
    font_big = pygame.font.Font('freesansbold.ttf', 64)
    # font
    dead_font = pygame.font.SysFont(None, 60)
    clock = pygame.time.Clock()

    #load image
    elevator = pygame.image.load('D:\Intel-OpenVino\Pygame_UI\elevator_1.png')
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