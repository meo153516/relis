from pygame import*
from random import randint,choice
import time
import sys
import pygame

window = display.set_mode(500, 700)
display.set_caption('dddd')
clock = pygame.time.Clock()
start_game = True
while start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game == False