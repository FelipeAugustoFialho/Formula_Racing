import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Background import Background
from code.Entity import Entity
from code.Const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name,game_mode ):

        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        enemy_number = random.randint(1, 6)
        self.surf = pygame.image.load(f'./assets/cars/Enemy{enemy_number}.png')

        self.timeout = 20000
       # pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)


    def run(self):
        #pygame.mixer_music.load(f'./assets/EngineSound.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)  #FPS
            for ent in self.entity_list:
                self.window.blit(source=ent.surf,dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2','Enemy3','Enemy4','Enemy5','Enemy6'))
                    self.entity_list.append(EntityFactory.get_entity(choice))



                                             # Exibindo textos
            self.level_text(text_size=18, text=f'{self.name} - Timeout:{self.timeout / 1000:.1f}s',
                                text_color=C_WHITE, text_center_pos=(120, 10)) #(10, 5))

            self.level_text(text_size=18, text=f'fps:{clock.get_fps():.0f}', text_color=C_WHITE,
                                text_center_pos=(55, WIN_HEIGHT - 25))  # Usando self.game_clock.get_fps() #(10, WIN_HEIGHT - 35))

            self.level_text(text_size=18, text=f'entidades:{len(self.entity_list)}', text_color=C_WHITE,
                               text_center_pos=(80, WIN_HEIGHT - 10)) #(10, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="arial black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
