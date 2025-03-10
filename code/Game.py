import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, MENU_OVER
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.GameOver import GameOver

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # 600,480

    def run(self):
            while True:
                score = Score(self.window)
                menu = Menu(self.window)
                menu_return = menu.run()  # Aqui você pega a opção do menu
                game_over = GameOver(self.window)

                if menu_return == MENU_OPTION[0]:
                    player_score = 0
                    level = Level(self.window, 'Level1', menu_return, player_score)
                    level_return = level.run(player_score)

                    # Loop de reinício do jogo
                    while True:
                        if level_return:  # Se o jogador completou ou perdeu o nível
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

                # def run(self):
    #     while True:
    #         score = Score(self.window)
    #         menu = Menu(self.window)
    #         menu_return = menu.run()  # Aqui você pega a opção do menu
    #         game_over = GameOver(self.window)
    #
    #         if menu_return == MENU_OPTION[0]:
    #             player_score = 0
    #             level = Level(self.window, 'Level1', menu_return, player_score)
    #             level_return = level.run(player_score)
    #
    #             # Loop de reinício do jogo
    #             while True:
    #
    #                 if level_return:  # Se o jogador completou ou perdeu o nível
    #                     game_over.game_over()  # Toca a música de game over
    #                     game_over_return = game_over.run()  # Executa a tela de game over
    #                     #Score(self.window).save(player_score)
    #
    #                     if game_over_return == MENU_OVER[0]:  # Jogar novamente
    #                         level = Level(self.window, 'Level1', menu_return, player_score)
    #                         level_return = level.run(player_score)  # Reinicia o nível
    #
    #                     elif game_over_return == MENU_OVER[1]:  # Ver score
    #
    #                         score.save(player_score)  # Exibe a pontuação
    #                         #Score(self.window).save(player_score)
    #                         # level_return = Level(self.window, 'Score', score.save())  # Salva a pontuação
    #                         level_return = Level(self.window, 'Score', score.save(player_score))
    #
    #
    #
    #                         level_return = level.run(player_score)  # Retorna ao nível de score
    #
    #                     if not level_return:  # Caso o jogador queira sair ou não tenha mais níveis
    #                         break  # Sai do loop e retorna para o menu
    #
    #         elif menu_return == MENU_OPTION[1]:
    #             score.show()  # Exibe a pontuação do jogador
    #
    #         elif menu_return == MENU_OPTION[2]:
    #             pygame.quit()  # Fecha o jogo
    #             quit()
    #
    #         else:
     #           pass  # Caso o menu não tenha nenhuma opção válida



# import pygame
# from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, MENU_OVER
# from code.Level import Level
# from code.Menu import Menu
# from code.Score import Score
# from code.GameOver import GameOver
#
# class Game:
#     def __init__(self):
#         pygame.init()
#         self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # 600,480
#
#     def run(self):
#
#         while True:
#             score = Score(self.window)
#             menu = Menu(self.window)
#             menu_return = menu.run()
#             game_over = GameOver(self.window)
#
#
#
#             if menu_return == MENU_OPTION[0]:
#                 player_score = 0
#                 level = Level(self.window, 'Level1', menu_return,player_score)
#                 level_return = level.run(player_score)
#
#                 if level_return:
#                     game_over.game_over()  # Apenas toca o som de game over
#                     game_over_return = game_over.run()  # Executa a tela de game over e captura a opção escolhida
#
#                     level_return = level.run(game_over)
#                     if game_over and MENU_OVER[0]:
#                         score = Level(self.window, 'Level1',menu_return,player_score)
#                         level_return = level.run(player_score)
#                   #   if game_over and MENU_OVER[1]:
#                   #       score = Level(self.window, 'Score', score.save())
#                   #       level_return = level.run(score.save)
#                   # else:
#                   #       level_return=level.run()
#                 # if level_return:
#                 #         score.save(menu_return, player_score)
#                 # if level_return == level.run(game_over):
#                 #     score.show()
#
#
#                 # score.show()
#                 if level_return:
#                     level = Level(self.window, 'Score', score.show(), player_score)
#                     level_return = level.run(player_score)
#                 if level_return:
#                     score.save(menu_return, player_score)
#
#
#             elif menu_return == MENU_OPTION[1]:
#                 score.show()
#
#             elif menu_return == MENU_OPTION[2]:
#                 pygame.quit()
#                 quit()
#             else:
#                 pass
