import random
import pygame
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple, scale_factor=1.0):
        super().__init__(name, position, scale_factor)




    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]

