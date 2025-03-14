import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, MENU_OVER
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.GameOver import GameOver

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
            while True:
                score = Score(self.window)
                menu = Menu(self.window)
                menu_return = menu.run()
                game_over = GameOver(self.window)



                if menu_return == MENU_OPTION[0]:
                    player_score = 0
                    level = Level(self.window, 'Level1', menu_return, player_score)
                    level_return = level.run(player_score)

                    # Loop de reinício do jogo
                    while True:
                        if level_return:
                            game_over.game_over()  # Toca a música de game over
                            game_over_return = game_over.run()  # Executa a tela de game over



                            if game_over_return == MENU_OVER[0]:  # Jogar novamente
                                level = Level(self.window, 'Level1', menu_return, player_score)
                                level_return = level.run(player_score)  # Reinicia o nível

                            elif game_over_return == MENU_OVER[1]:  # Ver score
                                score.save(player_score)  # Exibe a pontuação
                                print(f'Seu score da classe Game:{player_score}')
                                #Score(self.window).save(player_score)
                                score.show()  # Mostra a pontuação final

                                level_return = None  # Sai do loop de jogo, retorna ao menu

                            if not level_return:  # Caso o jogador queira sair ou não tenha mais níveis
                                break  # Sai do loop e retorna para o menu

                elif menu_return == MENU_OPTION[1]:
                    score.show()  # Exibe a pontuação do jogador

                elif menu_return == MENU_OPTION[2]:
                    pygame.quit()  # Fecha o jogo
                    quit()

                else:
                    break  # Sai do loop principal do jogo

