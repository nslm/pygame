import pygame
from time import sleep
import sys
 
pygame.init()
 
 
width, height = 900, 600
screen = pygame.display.set_mode((width, height))

image = pygame.image.load("base.png")
rect = image.get_rect()
image_background = pygame.image.load("2122627.png")
image_background = pygame.transform.scale(image_background, (width, height)) 
rect_background = image_background.get_rect()

stage = 0
stages = ((8,40,102,100), (111,40,87,100), (199,40,102,100), (303,40,77,100), (380,40,98,100), (480,40,107,100), (588,40,72,100))

stages2 = ((0,140,148,89),(148,140,141,89),(289,140,145,89),(435,140,143,89),(580,140,122,89),(0,230,108,90),(109,230,110,90),(218,230,97,90),(315,230,83,90),(315,230,83,90))

def atk_animate(direction_stage):
  
  for pos_atk in stages2:
    d3 = {'left':pos_atk[0], 'right':820 - pos_atk[0] - pos_atk[2]}
    screen.fill((250,250,250))
    screen.blit(d1[direction_stage],rect,(d3[direction_stage],pos_atk[1],pos_atk[2],pos_atk[3]))
    pygame.display.update()
    sleep(0.06)
  screen.fill((250,250,250))

  d3 = {'left':400, 'right':820 - 400 - 300}
  
  #rect.x += dict_mov[direction][0]*2
  screen.blit(d1[direction_stage],rect,(d3[direction_stage],230,300,109))
  #rect.x -= dict_mov[direction][0]*2
  pygame.display.update()
  sleep(0.05)
  

n=10
dict_key = {'up':pygame.K_UP,'down':pygame.K_DOWN,'left':pygame.K_LEFT,'right':pygame.K_RIGHT}
dict_direction = {'up':3,'down':0,'left':1,'right':2}
d1 = {'left':image,'right':pygame.transform.flip(image, True, False)}



dict_mov = {'up':(0,-n),'down':(0,n),'left':(-n,0),'right':(n,0)}
pos = [300,500]


direction_stage = 'right'
is_pressed = False

while True:
    #screen.blit(image_background,rect_background,(0,0,width,height))
    screen.fill((250,250,250))
    if stage >= 6:
        stage = 0
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not is_pressed:
        stage = 0
    is_pressed = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_j]:
      atk_animate(direction_stage)
  
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
    sleep(0.05)

    
