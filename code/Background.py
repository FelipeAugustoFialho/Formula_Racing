import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT
from code.Player import Player

class Background:
    def __init__(self, name, position):
        
        # Verifique se é um background ou carro
        self.name = name
        if 'Bg' in name:
            # Carregar o background da pasta 'assets'
            self.surf = pygame.image.load(f'./assets/{name}.png').convert_alpha()
        if'car' in name:
            # Carregar os carros da pasta 'assets/Cars'
            self.surf = pygame.image.load(f'./assets/Cars/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)



    def move(self,):
        # Se o fundo sair da tela, reposiciona ele no topo para criar o efeito de loop infinito
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.rect.y = -self.rect.height

        # if self.name.pressed_key[pygame.K_UP]:
        #     self.speed += 5
