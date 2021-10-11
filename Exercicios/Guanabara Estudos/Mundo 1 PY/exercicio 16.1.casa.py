import pygame

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.music.load('C:/Users/Lucas/Documents/GitHub/Estudo-de-Pyhton/Exercicios/Guanabara Estudos/Mundo 1 PY/teste.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()