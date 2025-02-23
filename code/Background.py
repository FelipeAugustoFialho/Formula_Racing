import pygame
from code.Const import ENTITY_SPEED, WIN_HEIGHT



class Background:

    def __init__(self, name, position):
        self.name = name
        self.acceleration = 0  # Inicializando aceleração
        self.default_speed = ENTITY_SPEED.get(self.name, 5)  # Pega a velocidade padrão

        # Carregar o background ou o carro corretamente
        if 'Bg' in name:
            self.surf = pygame.image.load(f'./assets/{name}.png').convert_alpha()
        elif 'car' in name:
            self.surf = pygame.image.load(f'./assets/Cars/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)



    def move(self):

        keys = pygame.key.get_pressed()  # Captura teclas pressionadas

        # Se pressionar "Cima", acelera o fundo
        if keys[pygame.K_UP]:
            self.acceleration += 0.1  # Acelera gradualmente
        else:
            self.acceleration = 0  # Volta para a velocidade padrão quando a tecla for solta

        # Atualiza a velocidade com base na aceleração
        current_speed = self.default_speed + self.acceleration
        self.rect.centery += current_speed

        # Reset do fundo para loop infinito
        if self.rect.top >= WIN_HEIGHT:
            self.rect.y = -self.rect.height

