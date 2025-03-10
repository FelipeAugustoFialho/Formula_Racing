import sys
import pygame
from pygame import Surface
from code.Const import C_BLUE, C_RED, WIN_WIDTH, WIN_HEIGHT, MENU_OVER



class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/GameOver.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_over = 0  # Índice da opção selecionada

    def game_over(self):
        pygame.mixer_music.load('./assets/GameOver.wav')
        pygame.mixer_music.play()
        while pygame.mixer_music.get_busy():
            pygame.time.delay(100)
        pygame.mixer_music.load('./assets/GameOverMusic.mp3')
        pygame.mixer_music.play(-1)





    def run(self):
        pygame.mixer_music.load('./assets/GameOverMusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Redesenha a imagem de fundo
            self.window.blit(self.surf, self.rect)

            # Renderiza as opções do menu
            for i, option in enumerate(MENU_OVER):
                is_selected = (i == self.menu_over)
                color = C_RED if is_selected else C_BLUE
                font_size = 45 if is_selected else 40  # Aumenta a fonte da opção selecionada
                font = pygame.font.Font(None, font_size)
                text = font.render(option, True, color)

                # Define a posição das opções
                x_pos = (WIN_WIDTH / 6-90) if i == 0 else (WIN_WIDTH / 2 + 150)
                y_pos = 610

                # Renderiza o texto na tela
                self.window.blit(text, (x_pos, y_pos))

                # Adiciona sublinhado na opção selecionada
                if is_selected:
                    underline_y = y_pos + text.get_height() + 5  # Posição do sublinhado
                    pygame.draw.line(self.window, color, (x_pos, underline_y),
                                     (x_pos + text.get_width(), underline_y), 3)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # INTERAÇÃO COM O MENU
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.menu_over = (self.menu_over + 1) % len(MENU_OVER)
                    if event.key == pygame.K_LEFT:
                        self.menu_over = (self.menu_over - 1) % len(MENU_OVER)
                    if event.key == pygame.K_RETURN:
                        return MENU_OVER[self.menu_over]

            pygame.time.delay(100)  # Pequeno delay para evitar trocas rápidas demais




#
#
#     def show(self):
#
#         pygame.mixer_music.load('./assets/Score.mp3')
#         pygame.mixer_music.play(-1)
#         self.window.blit(source=self.surf, dest=self.rect)
#
#         pygame.display.flip()
#         while True:
#             self.menu_text(20, text='Restart Game', text_color=C_BLUE, text_center_pos=((WIN_WIDTH / 2), 80))
#             self.menu_text(20, text='Finish Game', text_color=C_RED, text_center_pos=((WIN_WIDTH / 2), 200))
#
#             pygame.display.flip()
#             pass
#
#
#
#     def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
#         text_font: Font = pygame.font.SysFont(name="arialblack", size=text_size)
#         text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
#         text_rect: Rect = text_surf.get_rect(center=text_center_pos)
#         self.window.blit(source=text_surf, dest=text_rect)
#
#
# def get_formatted_date():
#     current_datetime = datetime.now()
#     current_time = current_datetime.strftime("%H:%M")
#     current_date = current_datetime.strftime("%d/%m/%y")
#     return f"{current_time} - {current_date}"