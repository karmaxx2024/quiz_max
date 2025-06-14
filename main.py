import sys
import pygame
from config import *
from game.states import *
from game.ui import *
from database.db_connection import *
from database.queries import *

# Инициализация БД
# init_db()
conn = get_db_connection()

# Инициализация Pygame ДО загрузки изображений
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('quiz_max')

# Теперь безопасно загружаем изображения
init_assets()
from config import (
    play_button_rect, reboot_button_rect, records_button_rect,
    play_button_img, reboot_button_img, records_button_img,
    background_img, background_rect
)


def achievements_screen():
    font = pygame.font.SysFont('Arial', 36)
    button_font = pygame.font.SysFont('Arial', 24)
    achievements = get_achievements(conn)  # функция уже есть в queries.py

    back_button_rect = pygame.Rect(20, 20, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    return

        screen.fill(BACKGROUND_COLOR)

        title = font.render("Достижения", True, WHITE)
        screen.blit(title, (310, 30))

        # Кнопка "Назад"
        pygame.draw.rect(screen, RED, back_button_rect)
        back_text = button_font.render("Назад", True, WHITE)
        text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, text_rect)

        pygame.display.flip()


def settings_screen():
    font = pygame.font.SysFont('Arial', 36)
    button_font = pygame.font.SysFont('Arial', 24)

    back_button_rect = pygame.Rect(20, 20, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    return

        screen.fill(BACKGROUND_COLOR)

        # Заголовок
        title = font.render("Настройки", True, WHITE)
        screen.blit(title, (310, 30))

        # Кнопка "Назад"
        pygame.draw.rect(screen, RED, back_button_rect)
        back_text = button_font.render("Назад", True, WHITE)
        text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, text_rect)

        pygame.display.flip()


def main_menu():
    """Главное меню игры"""
    # Создаем шрифт для надписи
    font = pygame.font.SysFont('Arial', 72, bold=True)
    title_text = font.render('ВИКТОРИНА', True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    return "play"
                elif reboot_button_rect.collidepoint(mouse_pos):
                    return "settings"
                elif records_button_rect.collidepoint(mouse_pos):
                    return "achievements"

        # Отрисовка
        screen.blit(background_img, background_rect)  # Сначала рисуем фон

        # Затем рисуем полупрозрачный прямоугольник для лучшей читаемости текста
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Черный с прозрачностью 50%
        screen.blit(overlay, (0, 0))

        # Рисуем заголовок
        screen.blit(title_text, title_rect)
        # Рисуем кнопки
        screen.blit(play_button_img, play_button_rect)
        screen.blit(reboot_button_img, reboot_button_rect)

        screen.blit(records_button_img, records_button_rect)

        pygame.display.flip()


def main():
    """Основной цикл"""
    while True:
        action = main_menu()
        if action == "play":
            print("Запуск игры...")
        elif action == "achievements":
            achievements_screen()
        elif action == "settings":
            settings_screen()


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()