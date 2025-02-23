import pygame
from abc import ABC, abstractmethod



class Entity(ABC):

    def __init__(self, name: str, position: tuple, scale_factor: float = 1.0):
        self.name = name



        # Carregar a imagem da pasta 'Cars' (para todos os carros e o jogador)
        original_surf = pygame.image.load(f'./assets/cars/{name}.png').convert_alpha()

        # Redimensionar a imagem conforme o scale_factor
        width, height = original_surf.get_width(), original_surf.get_height()
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Aplicar o redimensionamento e atualizar a superfície
        self.surf = pygame.transform.scale(original_surf, (new_width, new_height))

        # Inicializar o retângulo da entidade com a posição fornecida
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

#
# from abc import ABC, abstractmethod  # ABSTRACT CLASS
#
# import pygame.image
#
#
#
# class Entity(ABC):
#
#     def __init__(self,name:str,position:tuple, scale_factor: float = 1.0):
#         self.name = name
#         self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
#         self.surf = pygame.image.load('./assets/Cars' + name + '.png').convert_alpha()
#         self.rect = self.surf.get_rect(left=position[0],top=position[1])
#         self.speed = 0
#
#
#
#
#     @abstractmethod
#     def move(self):
#         pass