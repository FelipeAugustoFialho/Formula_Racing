import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player
import pygame


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(3):
                    # Carregar imagens de fundo da pasta 'assets'
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, -WIN_HEIGHT)))
                return list_bg

            case 'Player':
                # Carregar imagem do jogador da pasta 'assets/Cars'
                # return Player('Player', (375, 440), 0.2)
                return Player('Player', (375, 400))

            case 'Enemy1':
                # # Definir limites para evitar que os inimigos apareçam nas calçadas
                # LEFT_MARGIN = 130  # Mesmo limite do jogador à esquerda
                # RIGHT_MARGIN = WIN_WIDTH - 85  # Mesmo limite do jogador à direita
                #
                # # Posição inicial do inimigo
                # pos_x = random.randint(LEFT_MARGIN, RIGHT_MARGIN)  # Dentro dos limites seguros da pista
                # pos_y = -50  # Inimigos começam acima da tela
                #
                # return Enemy('Enemy1', (pos_x, pos_y))

        # return Enemy('Enemy1', (375, 250))
                return Enemy('Enemy1', (375, random.randint(0, WIN_HEIGHT)))

            case 'Enemy2':
                return Enemy('Enemy2', (375, random.randint(0, WIN_HEIGHT)))

            case'Enemy3':
                return Enemy('Enemy3', (375, random.randint(0, WIN_HEIGHT)))


            case'Enemy4':
                return Enemy('Enemy4', (375, random.randint(0, WIN_HEIGHT)))

            case'Enemy5':
                return Enemy('Enemy5', (375, random.randint(0, WIN_HEIGHT)))
            case'Enemy6':
                return Enemy('Enemy6', (375, random.randint(0, WIN_HEIGHT)))
# case 'Enemy':
#  enemy_image = f'Enemy{random.randint(1, 6)}.png'
# return Enemy('Enemy', position, enemy_image)
# return Enemy('Enemy', (375, random.randint(0, WIN_WIDTH)))
# return Enemy('Enemy',(375,random.randint(WIN_WIDTH,0)))

# Adicione outros casos conforme necessário, por exemplo, se você tiver outros tipos de entidades.

# from code.Background import Background
# from code.Const import WIN_HEIGHT
# from code.Player import Player
#
#
# class EntityFactory:
#     @staticmethod
#     # def get_entity(entity_name: str, position=(0, 0), scale_factor=1.0):
#     def get_entity(entity_name: str, position=(0, 0)):
#
#         match entity_name:
#             case 'Level1Bg':
#                 list_bg = []
#                 for i in range(3):
#                     list_bg.append(Background(f'Level1Bg{i}',(0,0)))
#                     list_bg.append(Background(f'Level1Bg{i}', (0, -WIN_HEIGHT)))
#                 return  list_bg
#             case 'Player':
#                     return Player('Player', (375, 440), 0.2)


# METODO CHAT
# bg1 = Background('Level1Bg', (0, 0))
# bg2 = Background('Level1Bg', (0, -WIN_HEIGHT))
# return [bg1, bg2]
