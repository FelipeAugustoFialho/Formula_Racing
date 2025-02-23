from code.Background import Background
from code.Const import WIN_HEIGHT
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
                return Player('Player', (375, 440), 0.2)
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


                    #METODO CHAT
                # bg1 = Background('Level1Bg', (0, 0))
                # bg2 = Background('Level1Bg', (0, -WIN_HEIGHT))
                # return [bg1, bg2]




