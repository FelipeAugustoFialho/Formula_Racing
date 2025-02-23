#C
import pygame

C_BLUE =(0,0,255)
C_WHITE =(255,255,255)
C_BLACK = (0,0,0)
C_RED = (255,0,0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 5,
    'Level1Bg1': 5,
    'Level1Bg2': 5,
    'Enemy1' : 4,
    'Enemy2' : 4,
    'Enemy3' : 4,
    'Enemy4' : 4,
    'Enemy5' : 4,
    'Enemy6' : 4,


}


SPEED = {'ENTITY_SPEED': ENTITY_SPEED}

SPAWN_TIME = 4000


#M
MENU_OPTION = ['NEW GAME',
               'TOP 10',
               'EXIT',
            ]
#W
WIN_WIDTH = 800
WIN_HEIGHT = 650
