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

                return Enemy('Enemy1', (455, random.randint(-WIN_HEIGHT, -1)))

            # return Enemy('Enemy1', (375, random.randint(0, WIN_HEIGHT)))

            case 'Enemy2':
                return Enemy('Enemy2', (375, random.randint(-WIN_HEIGHT, -1)))

            case 'Enemy3':
                return Enemy('Enemy3', (175, random.randint(-WIN_HEIGHT, -1)))

            case 'Enemy4':
                return Enemy('Enemy4', (575, random.randint(-WIN_HEIGHT, -1)))

            case 'Enemy5':
                return Enemy('Enemy5', (125, random.randint(-WIN_HEIGHT, -1)))

            case 'Enemy6':
                return Enemy('Enemy6', (610, random.randint(-WIN_HEIGHT, -1)))

