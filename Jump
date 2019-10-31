import pygame
import time
pygame.init()
largura = 750
altura = 800
tela = pygame.display.set_mode([largura,altura])
fundo = pygame.image.load('imagens/fundo.png')
relogio = pygame.time.Clock()
tamanho = 25
fps = 15
n1 = pygame.transform.scale(pygame.image.load('imagens/anselmo.jpg'),(tamanho, tamanho))
n2 = pygame.transform.scale(pygame.image.load('imagens/icon.jpg'),(tamanho*6, tamanho))
n3 = pygame.transform.scale(pygame.image.load('imagens/monitoria.png'),(tamanho*18, tamanho*3))


class slime():
    def __init__(self):
        self.px = 375
        self.py = 650
    def plot(self):
        tela.blit(n1,(self.px,self.py))

class superficies():
    def __init__(self,px,py):
        self.px = px
        self.py = py
    def plot(self):
        tela.blit(n2,(self.px,self.py))

def lista():
    chao1 = superficies(0,575)
    chao2 = superficies(200,475)
    chao12 = superficies(400,375)
    chao13 = superficies(600,275)
    chao3 = superficies(600,175)
    chao4 = superficies(400, 75)
    chao5 = superficies(600,-25)
    chao6 = superficies(400,-125)
    chao7 = superficies(200,-225)
    chao8 = superficies(0,-325)
    chao9 = superficies(200,-425)
    chao10 = superficies(200,-525)
    chao11 = superficies(400,-625)
    chaobase1 = superficies(0,675)
    chaobase2 = superficies(150,675)
    chaobase3 = superficies(300,675)
    chaobase4 = superficies(450,675)
    chaobase5 = superficies(600,675)
    chaobase6 = superficies(0,-725)
    chaobase7 = superficies(150,-725)
    chaobase8 = superficies(300,-725)
    chaobase9 = superficies(450,-725)
    chaobase10 = superficies(600,-725)
    fim = superficies(0,-800)
    return [chao1,chao2,chao3,chao4,chao5,chao6,chao7,chao8,chao9,chao10,chao11,chao12,chao13,chaobase1,chaobase2,chaobase3,chaobase4,chaobase5,chaobase6,chaobase7,chaobase8,chaobase9,chaobase10,fim]
lista_superficies = lista()
anselmo = slime()

def game():
    RIGHT_press = False
    LEFT_press = False
    endgame = False
    while not endgame:

        apoiado = False
        for i in lista_superficies:
            if i.py==anselmo.py+tamanho and i.px-tamanho/2 <= anselmo.px < i.px + tamanho*6.5:
                apoiado = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    RIGHT_press = True
                    LEFT_press = False
                if event.key == pygame.K_LEFT:
                    LEFT_press = True
                    RIGHT_press = False
                if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and apoiado:
                    for i in lista_superficies:
                        i.py += tamanho * 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                RIGHT_press = False
            if event.key == pygame.K_LEFT:
                LEFT_press = False

        if RIGHT_press and anselmo.px < largura - tamanho:
            anselmo.px += tamanho
        if LEFT_press and anselmo.px > 0:
            anselmo.px -= tamanho

        if not apoiado:
            for j in lista_superficies:
                j.py -= tamanho

        tela.blit(fundo,(0,0))
        anselmo.plot()
        for i in lista_superficies:
            i.plot()
        tela.blit(n3,(lista_superficies[23].px,lista_superficies[23].py))
        pygame.display.update()
        relogio.tick(fps)
game()
