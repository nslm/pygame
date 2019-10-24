import pygame
from random import randint

pygame.init()
largura = 600
altura = 390
tamanho = 15
fps = 8
tela = pygame.display.set_mode([largura,altura])
relogio = pygame.time.Clock()
pygame.display.set_caption('cobrinha')


branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

def cobra(cobraXY,lista):
    for i in range(len(cobraXY)):
        pygame.draw.rect(tela, lista[i], [cobraXY[i][0], cobraXY[i][1], tamanho, tamanho])


def fruta(mx,my):
    pygame.draw.rect(tela, vermelho, [mx, my, tamanho, tamanho])


def jogo():
    px = randint(0,(largura-tamanho)/tamanho)*tamanho
    py = randint(0,(altura-tamanho)/tamanho)*tamanho
    mx = randint(0,(largura-tamanho)/tamanho)*tamanho
    my = randint(0,(altura-tamanho)/tamanho)*tamanho
    cobraXY = []
    listacor=[preto]
    dx = 0
    dy = 0
    v = 15
    comp = 1

    endgame = False

    while not endgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if dy <= 0:
                        dy = -v
                        dx = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if dy >= 0:
                        dy = v
                        dx = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if dx >= 0:
                        dx = v
                        dy = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if dx <= 0:
                        dx = -v
                        dy = 0

        tela.fill(branco)
        px += dx
        py += dy

        if px==mx and py==my:
            mx = randint(0, (largura - tamanho) / tamanho) * tamanho
            my = randint(0, (altura - tamanho) / tamanho) * tamanho
            comp+=1
            cor = randint(0,2)
            if cor==0:
                cor=preto
            if cor==1:
                cor=azul
            if cor==2:
                cor=verde
            listacor.append(cor)
        lista = [px, py]
        if lista in cobraXY and comp>1:
            endgame = True
        cobraXY.append(lista)
        if len(cobraXY)>comp:
            del cobraXY[0]


        cobra(cobraXY,listacor)
        fruta(mx,my)
        pygame.display.update()
        relogio.tick(fps)

        if px<=0 or px>=largura or py<=0 or py>=altura:
            endgame = True


jogo()
pygame.quit()
