import pygame
from pygame import image
from pygame.locals import QUIT
import keyboard
width = 800
height = 746.5
barSize = 150
doorSize = 400
del_x = 5

color_bg = (0, 0, 0)
color_white = (255, 255, 255)
color_lightGray = (200, 200, 200)
color_darkGray = (100, 100, 100)
color_red = (255,0,0)

running = True

# Elevator State

# global curr_floor, up_down, floor_state, floor_x, floor_y
floor_x, floor_y = (1050,105)
curr_floor = 1
up_down = 'up'
floor_state = [0 for i in range(11)]
# Traverse Status Dictionary
def traverse(status, floor):
    font = pygame.font.Font('freesansbold.ttf', 32)
    global floor_x , floor_y
    
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
                screen.blit(temp, (floor_x+ 80, floor_y) )
                floor_y += 40
    else :
        for i in range(10,0,-1):
            if floor_state[i] == 1:
                temp = font.render(str(i), True,color_bg)
                screen.blit(temp, (floor_x+ 80, floor_y) )
                floor_y += 40
                    
# Panel Control
def panel_control():
    if up_down == 'up':
        for i in range(curr_floor,11):
            if floor_state[i] == 1:
                font = pygame.font.Font('freesansbold.ttf', 64)
                temp = font.render(str(i), True, color_red)
                screen.blit(temp, (460, 120) )
                break
# Scheduling function
def input_floor(screen, status):
    global floor_x, floor_y
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Input Floor', True, color_bg)
    pygame.draw.rect(screen, color_bg,[990, 90, 300, 60], 5)
    screen.blit(text, (floor_x, floor_y))
    floor_y += 60
    traverse(status, (floor_x, floor_y ))
    panel_control()
# Door Open and Close
def Open_Close():
    if switch == 'open':
        if door_1.w <= 562:
            screen.blit(elevator, (0,0))
            door_1.center = (door_1_x, door_1_y)
            door_1.w += del_x
            pygame.draw.rect(screen, color_white, door_1)
            pygame.display.update()
    elif switch == 'close':
        if door_1.w >= 0:
            screen.blit(elevator, (0,0))
            door_1.center = (door_1_x, door_1_y)
            door_1.w -= del_x
            pygame.draw.rect(screen, color_white, door_1)
            pygame.display.update()

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
    switch = 'idle'
    global status 
    status = {'o':False, 'c':False, '1':False, '2':True, '3':False, '4':True, '5':False, '6':False, '7':False, '8':False, '9':True, '10':False}
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
        Open_Close()
        pygame.display.update()