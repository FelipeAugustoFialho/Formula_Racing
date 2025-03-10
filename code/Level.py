import random
import sys
import time

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.GameOver import GameOver
from code.Enemy import Enemy
from code.Entity import Entity
from code.Const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, ENTITY_SCORE, EVENT_CRASH, MENU_OPTION, EVENT_SCORE
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Score import Score


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):

        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.sprite_group = pygame.sprite.Group()  # Inicializa o grupo de sprites
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        player = EntityFactory.get_entity('Player')
        player.score = 0
        self.entity_list.append(player)
        self.crash_occurred = False  # Adiciona esta variável
        self.crash_time = 0  # Tempo da colisão


        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME, EVENT_SCORE)

        self.timeout = 20000



    def run(self,player_score:list[int]):
        pygame.mixer_music.load(f'./assets/EngineSound.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        pygame.mixer_music.set_volume(0.1)
        game_over = GameOver(self.window)




        while True:
            clock.tick(60)  # FPS


            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)

                if hasattr(ent, 'move'):  # Verifica se a entidade tem o método move
                    ent.move()  # Chama move() apenas para entidades que possuem esse método

                    # TESTE
                if isinstance(self.entity_list, list):
                    for ent in self.entity_list:
                        if isinstance(ent, Enemy):  # Garante que estamos lidando com um inimigo
                            if ent.rect.top > WIN_HEIGHT:  # Verificando se o inimigo saiu da tela
                                print(f"Inimigo {ent} saiu da tela, removendo...")
                                ent.health = 0  # Zera a saúde do inimigo

                            if ent.health == 0:
                                for player in self.entity_list:
                                    if isinstance(player, Player):  # Garante que é um jogador

                                        player_score = player.score + ent.score  # Soma o score ao jogador




                                        print(f"Score do jogador atualizado para {player_score}.")




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3', 'Enemy4', 'Enemy5', 'Enemy6'))
                    self.entity_list.append(EntityFactory.get_entity(choice))



                if self.crash_occurred:
                    elapsed_time = pygame.time.get_ticks() - self.crash_time
                    if elapsed_time > 1000:  # 1000ms = 1 second
                        for ent in self.entity_list:
                            if isinstance(ent,Player):
                                player_score [0] = ent.score
                                #Score(self.window).save(player_score)
                                # AQUI ESTA SALVANDO
                                Score(self.window).save([player.score])  # Passando uma lista com um único valor

                                #teste
                                player_score += ent.score
                                print(f"Score atualizado do jogador 'crash': {player_score}")


                                #
                                pass

                        return True  # Volta para o menu


                if event.type == EVENT_CRASH:
                    self.crash_time = pygame.time.get_ticks()  # Marca o tempo da colisão
                    self.crash_occurred = True  # Sinaliza que ocorreu uma colisão

                    ## CHAMAR GAME OVER
                    # Score(self.window).save(player_score)
                    # break
                    # if self.crash_occurred == True:
                    #     score = player_score
                    #     score.save(player_score)





                    # Collisions

                EntityMediator.verify_collision(entity_list=self.entity_list, sprite_group=self.sprite_group)

               # EntityMediator.verify_health(entity_list=self.entity_list)
                # No código onde você chama EntityMediator.verify_health
                EntityMediator.verify_health(entity_list=self.entity_list, window=self.window)

            # Exibindo textos
            self.level_text(text_size=18, text=f'{self.name} - Timeout:{self.timeout / 1000:.1f} s',
                            text_color=C_WHITE, text_center_pos=(120, 10))  # (10, 5))
            self.level_text(text_size=18, text=f'Score: {player_score}',
                             text_color=C_WHITE, text_center_pos=(90, 40))

            self.level_text(text_size=18, text=f'fps:{clock.get_fps():.0f}', text_color=C_WHITE,
                            text_center_pos=(
                            55, WIN_HEIGHT - 25))  # Usando self.game_clock.get_fps() #(10, WIN_HEIGHT - 35))

            self.level_text(text_size=18, text=f'entidades:{len(self.entity_list)}', text_color=C_WHITE,
                            text_center_pos=(80, WIN_HEIGHT - 10))  # (10, WIN_HEIGHT - 20))


            pygame.display.flip()

        pass



    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="arial black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


