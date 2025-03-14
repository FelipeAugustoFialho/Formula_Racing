import pygame
from code.Const import EVENT_CRASH

class Collision(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_group):
        super().__init__()
        self.surf = pygame.image.load("assets/collision.png").convert_alpha()
        self.rect = self.surf.get_rect(center=(x, y))
        self.lifetime = 60  # Tempo de exibição da explosão (frames)


        # Carregar e tocar o som da colisão
        self.crash_sound = pygame.mixer.Sound('./assets/carCrash.wav')
        self.crash_sound.set_volume(0.2)  # Define o volume da batida
        self.crash_sound.play()

        self.health = 100
        self.score = 0

        # Adiciona a explosão ao grupo de sprites visíveis
        sprite_group.add(self)


        pygame.event.post(pygame.event.Event(EVENT_CRASH))

    def update(self):

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()  # Remove a explosão da tela




