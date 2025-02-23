import random

import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple, scale_factor=1.0):
        super().__init__(name, position, scale_factor)



    def move(self):

        # Movimento vertical para baixo
        self.rect.y += ENTITY_SPEED.get(self.name, 5)  # Inimigo desce a cada frame

        # Quando o inimigo atingir o fundo, ele reaparece no topo
        if self.rect.top > WIN_HEIGHT:
            self.rect.y = -self.rect.height  # Reaparece logo acima da tela
            self.rect.x = random.randint(100, WIN_WIDTH - 200) #40,40 # Posição horizontal aleatória




        # # Movimento vertical para baixo
        # self.rect.y += ENTITY_SPEED.get(self.name, 5)  # Aumenta a posição 'y' para descer
        #
        # # Quando o inimigo atingir o fundo, reposiciona no topo
        # if self.rect.top > WIN_HEIGHT:
        #     self.rect.bottom = 0  # Coloca o inimigo no topo
        #     self.rect.x = random.randint(40, WIN_WIDTH - 40)  # Posição horizontal aleatória

        #
        # self.rect.centery -= ENTITY_SPEED[self.name]
        # if self.rect.top <= 0:
        #     self.rect.bottom = WIN_HEIGHT
        #
        # pass
