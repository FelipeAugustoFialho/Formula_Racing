import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Background import Background
from code.Entity import Entity
from code.Const import C_WHITE, WIN_HEIGHT
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name,game_mode ):

        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 20000


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

            #METODO CHAT
        # while self.running:
        #     self.handle_events()
        #     self.update()
        #     self.render()
        #     self.game_clock.tick(60)  # Mantém FPS fixo



    # def handle_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #
    #
    #
    # def update(self):
    #     # Movimenta e desenha o fundo
    #     for bg in self.backgrounds:
    #         bg.move()  # Move o fundo
    #         self.window.blit(bg.image, bg.rect)
    #
    #         # Desenha o fundo na tela
    #
    #     # Atualiza e desenha os outros elementos do jogo (como o jogador)
    #     for entity in self.entity_list:
    #         entity.move()  # Move o jogador
    #         self.window.blit(entity.surf, entity.rect)  # Desenha o jogador na tela
    #
    #
    #
    # def render(self):
    #     # Renderizando os backgrounds
    #     for bg in self.backgrounds:
    #         self.window.blit(bg.image, bg.rect)
    #
    #     # Renderizando as entidades
    #     for ent in self.entity_list:
    #         self.window.blit(ent.surf, ent.rect)
    #
    #     # Atualizando a tela
    #     pygame.display.flip()
    #
    #     # Exibindo textos
    #     self.level_text(text_size=18, text=f'{self.name} - Timeout:{self.timeout / 1000:.1f}s',
    #                     text_color=C_WHITE, text_center_pos=(120, 10)) #(10, 5))
    #
    #     self.level_text(text_size=18, text=f'fps:{self.game_clock.get_fps():.0f}', text_color=C_WHITE,
    #                     text_center_pos=(55, WIN_HEIGHT - 25))  # Usando self.game_clock.get_fps() #(10, WIN_HEIGHT - 35))
    #
    #     self.level_text(text_size=18, text=f'entidades:{len(self.entity_list)}', text_color=C_WHITE,
    #                     text_center_pos=(80, WIN_HEIGHT - 10)) #(10, WIN_HEIGHT - 20))
    #     pygame.display.flip()
    #
    # def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    #     text_font: Font = pygame.font.SysFont(name="arial black", size=text_size)
    #     text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    #     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    #     self.window.blit(text_surf, text_rect)
    #
