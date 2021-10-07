import pygame, sys, time
from pygame.locals import*

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sound!!")

soundObj = pygame.mixer.Sound('C:/Users/PC-OPERAÇÃO-LUCAS/Documents/GitHub/Estudo-de-Pyhton/Exercicios/Guanabara Estudos/Mundo 1 PY/testeteste.wav')
soundObj.play()
input()
time.sleep(1) #wait and let the sound play for X second
soundObj.stop()

while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()