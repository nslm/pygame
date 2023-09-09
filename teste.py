import pygame
from time import sleep
import sys
 
pygame.init()
 
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

image = pygame.image.load("base.png")
rect = image.get_rect()

stage = 0
stages = ((8,40,102,100), (111,40,87,100), (199,40,102,100), (303,40,77,100))

n=5
dict_key = {'up':pygame.K_UP,'down':pygame.K_DOWN,'left':pygame.K_LEFT,'right':pygame.K_RIGHT}
dict_direction = {'up':3,'down':0,'left':1,'right':2}
d1 = {'left':image,'right':pygame.transform.flip(image, True, False)}



dict_mov = {'up':(0,-n),'down':(0,n),'left':(-n,0),'right':(n,0)}
pos = [200,200]


direction_stage = 'right'
is_pressed = False

while True:
    screen.fill((250, 250, 250))
    if stage >= 3:
        stage = 0
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not is_pressed:
        stage = 0
    is_pressed = False
    keys=pygame.key.get_pressed()
    for direction in ('left','right'):
        if keys[dict_key[direction]]:
            if 0 + n*2 < pos[0]+dict_mov[direction][0] < width -64 -n*2 and 0 + n*2 < pos[1]+dict_mov[direction][1] < height -64 - n*2:
                pos[0], pos[1] = pos[0]+dict_mov[direction][0], pos[1]+dict_mov[direction][1]

            stage+=1
            is_pressed = True
            direction_stage = direction
            break

    rect.x, rect.y = pos
    #screen.blit(image_background,rect_background,(map_pos[0],map_pos[1],width,height))
    d2 = {'left':stages[stage][0], 'right':820 - stages[stage][0] - stages[stage][2]}
        
    screen.blit(d1[direction_stage],rect,(d2[direction_stage],stages[stage][1],stages[stage][2],stages[stage][3]))
    pygame.display.update()
    sleep(0.2)

    
