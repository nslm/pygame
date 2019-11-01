import pygame
from random import randint
pygame.init()
largura = 1000
altura = 800
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
tela = pygame.display.set_mode([largura,altura])
fundo = pygame.image.load('imagens/fundo.png')
p = pygame.image.load('imagens/p.png')
p2 = pygame.image.load('imagens/p2.png')
cano = pygame.image.load('imagens/tubo.png')
cano2 = pygame.image.load('imagens/tubo2.png')
relogio = pygame.time.Clock()
fps=7
px=500
py=400
v=40
tamanho=10
pontos = 0


class wall():
    def __init__(self):
        self.posi = randint(1,4)*100

    def pos(self,pos):
        p = pygame.draw.rect(tela,azul,[pos,0,100,self.posi])
        tela.blit(cano,p)
        p2 = pygame.draw.rect(tela,azul,[pos,self.posi-84,100,159])
        tela.blit(cano2,p2)


class bird():
    def __init__(self):
        self.px = 200
        self.py = 200
    def plot(self):
        self.h = pygame.draw.rect(tela, vermelho, [self.px, self.py, 20, 20])
        tela.blit(p,self.h)
    def salto(self):
        self.py -= 80
        tela.blit(p2,passarinho.h)
        pygame.display.update()

def texto(msg,cor,tam,x,y):
    font = pygame.font.SysFont(None,tam)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x,y])

l = largura
parede = wall()
passarinho=bird()

endgame = False

while not endgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                passarinho.salto()
    tela.blit(fundo,(0,0))
    parede.pos(l)
    passarinho.plot()
    texto('placar: ' + str(pontos), (255, 255, 0), 50, largura - 200, 20)
    passarinho.py +=15
    l -= 25
    if l<-0:
        l = largura
        parede = wall()
    if passarinho.py > altura:
        endgame = True
    if l-50 < passarinho.px < l+100:
        if not(parede.posi-50 < passarinho.py < parede.posi+125):
            endgame= True
    if passarinho.px==l:
        pontos += 1
    pygame.display.update()
    relogio.tick(fps)

pygame.quit()
