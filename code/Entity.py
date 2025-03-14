import pygame
from abc import ABC, abstractmethod

from code.Const import ENTITY_HEALTH, ENTITY_SCORE, ENTITY_DAMAGE, EVENT_SCORE


class Entity(ABC):

    def __init__(self, name: str, position: tuple, scale_factor: float = 1.0):
        self.name = name
        self.surf = pygame.image.load(f'./assets/cars/'+ name +'.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]




    @abstractmethod
    def move(self):
        pass

