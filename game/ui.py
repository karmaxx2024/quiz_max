import pygame
from pygame.locals import *
from config import *  # Убедитесь, что RED, BURGUNDY и FONT_PATH определены


class Button:
    def __init__(self, x, y, width, height, text, color=RED, hover_color=BURGUNDY, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.is_hovered = False

        # Подгружаем шрифт

        self.font = pygame.font.Font(None, font_size)  # None = стандартный шрифт

    def draw(self, surface):
        """Рисует кнопку на экране"""
        # Определяем цвет в зависимости от наведения курсора
        current_color = self.hover_color if self.is_hovered else self.color

        # Рисуем фон кнопки
        pygame.draw.rect(surface, current_color, self.rect)

        # Рисуем текст по центру кнопки
        text_surf = self.font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_hover(self, pos):
        """Проверяет, находится ли курсор над кнопкой"""
        self.is_hovered = self.rect.collidepoint(pos)

    def handle_event(self, event):
        """Проверяет нажатие на кнопку"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False