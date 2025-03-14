import sys
from datetime import datetime
import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from code.Const import C_BLUE, SCORE_POS, MENU_OPTION, C_RED, C_WHITE, C_YELLOW, ENTITY_SCORE
from code.DBProxy import DBProxy



class Score:

    def __init__(self,window:Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        db_proxy = DBProxy('DBScore')
        name = ''




    def save(self,player_score:list[int]):
        #self.score.append(player_score)  # Salva a pontuação em uma lista
        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ' '
        score = player_score[0] if isinstance(player_score, list) else player_score

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(45,'YOU LOST !',C_RED,SCORE_POS['Title'])
#

            print(f'Seu score2:{score}')


            text = 'Enter your name:'
            self.score_text(40, text, C_BLUE, SCORE_POS['EnterName'])


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) <= 8:

                        db_proxy.save({'name': name, 'score': player_score, 'date': get_formatted_date()})

                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name [:-1]
                    else:
                        if len(name) <= 8:
                            name += event.unicode

            self.score_text(40, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass


    def show(self):

        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 PLAYERS', C_BLUE, SCORE_POS['Title'])
        self.score_text(20, 'NAME      SCORE      DATE       ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()


        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}          {score:05d}          {date}', C_YELLOW,
                            SCORE_POS[list_score.index(player_score)])


        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()


            pass


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="arialblack", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"


