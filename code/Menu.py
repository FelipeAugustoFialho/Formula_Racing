import pygame.image
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, C_BLUE, MENU_OPTION, C_WHITE, C_BLACK, C_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        self.flag = pygame.image.load('./assets/flag.png')
        self.flag = pygame.transform.scale(self.flag, (200, 200))

    def draw_flags(self):
        flag_y = 70  # HEIGHT FLAG
        flag_x_left = int(WIN_WIDTH / 2) + 200  # Adjust left for title
        flag_x_right = int(WIN_WIDTH / 2) - 390  # Adjust right for title

        self.window.blit(self.flag, (flag_x_left, flag_y))  # Left Flag
        self.window.blit(self.flag, (flag_x_right, flag_y))  # Right Flag

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./assets/menuMusic.wav')
        pygame.mixer_music.play(-1)
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.draw_flags()

            self.menu_text(100, text='Fórmula', text_color=C_RED, text_center_pos=((WIN_WIDTH / 2), 80))
            self.menu_text(100, text='Racing', text_color=C_RED, text_center_pos=((WIN_WIDTH / 2), 200))

            for i in range(len(MENU_OPTION)):

                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], C_RED, ((WIN_WIDTH / 2), 500 + 60 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 500 + 60 * i))

            pygame.display.flip()

            # EVENTS

                        #QUIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                    # INTERACTION MENU
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="arialblack", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
