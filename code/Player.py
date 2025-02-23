import pygame
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Player(Entity):
    pressed_key = None

    def __init__(self, name: str, position: tuple, scale_factor=1.0):
        super().__init__(name, position, scale_factor)
        self.image = pygame.image.load(f'./assets/cars/Player.png').convert()

        #self.image = pygame.transform.scale(self.image, (150, 150))

        # self.surf = self.image  # Atualiza a superfície usada na renderização
        # self.rect = self.surf.get_rect(center=position,)


    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Movendo o jogador
        if pressed_key[pygame.K_LEFT] and self.rect.left > 130:
            self.rect.centerx -= 8
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH - 85:
            self.rect.centerx += 8

        # Se pressionar a seta para cima, aumenta a velocidade do fundo
        # if pressed_key[pygame.K_UP]:
        #     self.speed += 5



