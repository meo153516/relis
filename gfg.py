from pygame import*
from random import randint
import time
import sys
import pygame
pygame.init()

#клас-батько для спрайтів. #конструктор сласу
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__
        #кожен спрайт повинен зберігати властивість імаге - зображення
        self.image = transform.scale(image.load(player_image), (100, 80))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість рект - прямокутник, в який він прис
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Game(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__
        #кожен спрайт повинен зберігати властивість імаге - зображення
        self.image = transform.scale(image.load(player_image), (130, 100))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість рект - прямокутник, в який він прис
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

Q = GameSprite("Q.png", 60, 410, 0)
W = GameSprite("W.png", 300, 410, 0)
E = GameSprite("E.png", 540, 410, 0)
znak1 = Game("znak.png", 70, 180, 0)
znak2 = Game("znak.png", 500, 180, 0)
protuv = GameSprite("protuv.png", 520, 70, 0)
vu = GameSprite("vu.png", 70, 70, 0)
window = pygame.display.set_mode((700, 500))
fon = pygame.image.load("Stil.png")
display.set_caption('dddd')
clock = pygame.time.Clock()
start_game = True
bot = randint(1, 3)

kamin = Game("kamin.png", 70, 180, 0)
nozn = Game("nozn.png", 70, 180, 0)
papir = Game("papir.png", 70, 180, 0)
while start_game:
    window.blit(fon,(0, 0))
    Q.reset()
    Q.update()
    W.reset()
    W.update()
    E.reset()
    E.update()
    znak1.reset()
    znak1.update()
    znak2.reset()
    znak2.update()
    protuv.reset()
    protuv.update()
    vu.reset()
    vu.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                kamin.reset()
                kamin.update()
            if event.key == pygame.K_w:
                nozn.reset()
                nozn.update()
            if event.key == pygame.K_e:
                papir.reset()
                papir.update()

                



    pygame.display.update()

    clock.tick(60)
        