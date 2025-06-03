import sys
import pygame
from config import *
from game.states import *
from game.ui import *
from database.db_connection import *
from database.queries import *


class Game:
    def __init__(self):
        # Инициализация Pygame ДО загрузки изображений
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('quiz_max')
        self.clock = pygame.time.Clock()  # Добавлено self. для сохранения как атрибута
        self.font_large = pygame.font.SysFont('Arial', 72, bold=True)

        # Инициализация БД
        init_db()
        self.conn = get_db_connection()
        self.achievements = get_achievements(self.conn)

        # Состояние игры (перенесено в __init__ и сделано атрибутами экземпляра)
        self.current_state = GameState.MENU
        self.selected_role = ""

        # Теперь безопасно загружаем изображения
        init_assets()  # Предполагается, что эта функция инициализирует глобальные переменные кнопок

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if self.current_state == GameState.MENU:
                self.handle_menu_events(event)

    def handle_menu_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Предполагается, что эти переменные определены в модуле ui после init_assets()
            if play_button_rect.collidepoint(mouse_pos):
                self.current_state = GameState.ROLE_SELECT
            elif reboot_button_rect.collidepoint(mouse_pos):
                print("настройки")
            elif records_button_rect.collidepoint(mouse_pos):
                self.current_state = GameState.ACHIEVEMENTS

    def render(self):
        self.screen.fill(WHITE)

        if self.current_state == GameState.MENU:
            self.render_menu()
        elif self.current_state == GameState.ACHIEVEMENTS:
            self.render_achievements()

        pygame.display.flip()

    def render_menu(self):
        self.screen.blit(background_img, assets.images.background_rect)

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))

        title = self.font_large.render('ВИКТОРИНА', True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)

        # Предполагается, что эти переменные определены в модуле ui
        self.screen.blit(play_button_img, play_button_rect)
        self.screen.blit(reboot_button_img, reboot_button_rect)
        self.screen.blit(records_button_img, records_button_rect)

    def render_achievements(self):
        # Реализация отображения достижений
        pass

    def quit_game(self):
        if self.conn:
            self.conn.close()
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            self.handle_events()
            self.render()
            self.clock.tick(FPS)  # Исправлено с clock на self.clock


if __name__ == "__main__":
    game = Game()
    game.run()