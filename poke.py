import pygame
from time import sleep
 
pygame.init()
 
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

image = pygame.image.load("gZ3c5.png")
image_background = pygame.image.load("background.jfif")
image_background = pygame.transform.scale(image_background, (945, 1680)) 
rect = image.get_rect()
rect_background = image_background.get_rect()

n = 5
dict_key = {'up':pygame.K_UP,'down':pygame.K_DOWN,'left':pygame.K_LEFT,'right':pygame.K_RIGHT}
dict_direction = {'up':3,'down':0,'left':1,'right':2}
dict_mov = {'up':(0,-n),'down':(0,n),'left':(-n,0),'right':(n,0)}
pos = [302,405]
map_pos = [200,1200]

object_list = [(0,64,0,1680),(825,1000,0,1680), (0,375,0,40), (505,1000,0,40), (265,380,75,460), (345,615,535,670), (0,140,535,670)]
object_list = object_list + [(0,1000,1605,2000), (0,455,1455,2000), (505,1000,1455,2000), (0,455,955,1100)]

stage = 0
direction_stage = 'up'
is_pressed = False

while True:
    screen.fill((0, 0, 0))
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
    for direction in ('up','down','left','right'):
        if keys[dict_key[direction]]:
            mov = True
            for hitbox in object_list:
                if hitbox[0] < pos[0]+dict_mov[direction][0]+map_pos[0] < hitbox[1] and hitbox[2] < pos[1]+dict_mov[direction][1]+map_pos[1] < hitbox[3]:
                    mov = False
            if mov and 0 + n*2 < pos[0]+dict_mov[direction][0] < width -64 -n*2 and 0 + n*2 < pos[1]+dict_mov[direction][1] < height -64 - n*2:
                pos[0], pos[1] = pos[0]+dict_mov[direction][0], pos[1]+dict_mov[direction][1]
            else:
                if mov and 0 < map_pos[0]+dict_mov[direction][0] < 945 and 0 < map_pos[1]+dict_mov[direction][1] < 1680:
                    map_pos[0], map_pos[1] = map_pos[0]+dict_mov[direction][0], map_pos[1]+dict_mov[direction][1]
            stage+=1
            is_pressed = True
            direction_stage = direction
            break

    rect.x, rect.y = pos
    screen.blit(image_background,rect_background,(map_pos[0],map_pos[1],width,height))
    screen.blit(image,rect,(64*stage,64*dict_direction[direction_stage],64,64))
    pygame.display.update()
    sleep(0.05)

    
