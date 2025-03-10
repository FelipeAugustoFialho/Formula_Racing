
import pygame




#C
C_BLUE =(0,0,255)
C_WHITE =(255,255,255)
C_BLACK = (0,0,0)
C_RED = (255,0,0)
C_GREEN = (0,128,0)
C_CYAN = (0,128,128)
C_YELLOW = (255, 255, 0)


#E


EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_CRASH = pygame.USEREVENT + 2
EVENT_SCORE = pygame.USEREVENT+ 3   # TESTE





ENTITY_SPEED = {
    'Level1Bg0': 7,
    'Level1Bg1': 7,
    'Level1Bg2': 7,
    'Enemy1' : 6,
    'Enemy2' : 6,
    'Enemy3' : 6,
    'Enemy4' : 6,
    'Enemy5' : 6,
    'Enemy6' : 6,


}


ENTITY_HEALTH =  {

    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Enemy1' : 4,
    'Enemy2' : 4,
    'Enemy3' : 4,
    'Enemy4' : 4,
    'Enemy5' : 4,
    'Enemy6' : 4,
    'Player' : 4,
    #'Collision':4,


}


SPEED = {'ENTITY_SPEED': ENTITY_SPEED}

SPAWN_TIME = 1000

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Enemy1': 100,
    'Enemy2': 100,
    'Enemy3': 100,
    'Enemy4': 100,
    'Enemy5': 100,
    'Enemy6': 100,
    'Player': 0,

}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Enemy1': 10,
    'Enemy2': 10,
    'Enemy3': 10,
    'Enemy4': 10,
    'Enemy5': 10,
    'Enemy6': 10,
    'Player': 10,

}

#M
MENU_OPTION = ['NEW GAME',
               'TOP 10',
               'EXIT',
            ]


MENU_OVER = ['RESTART GAME',
               'FINISH GAME',

            ]
#W
WIN_WIDTH = 800
WIN_HEIGHT = 650


SCORE_POS = {'Title':(WIN_WIDTH / 2,50),
             'EnterName': (WIN_WIDTH / 2,80),
             'Label': (WIN_WIDTH / 2,90),
             'Name': (WIN_WIDTH / 2,110),
             0:(WIN_WIDTH / 2,110),
             1:(WIN_WIDTH / 2,130),
             2:(WIN_WIDTH / 2,150),
             3:(WIN_WIDTH / 2,170),
             4:(WIN_WIDTH / 2,190),
             5:(WIN_WIDTH / 2,210),
             6:(WIN_WIDTH / 2,230),
             7:(WIN_WIDTH / 2,250),
             8:(WIN_WIDTH / 2,270),
             9:(WIN_WIDTH / 2,290),

}