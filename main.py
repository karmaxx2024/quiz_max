import sys
import pygame
from config import *
from game.states import *
from game.ui import *
from database.db_connection import *
from database.queries import *

quiz_data = {
    "папа": [
        {"question": "Как ласково называет Максима папа?", "answers": ["хомяк", "кабася"]},
        {'question': 'день рождение когда у максима?', 'answers': ['15 апреля', '15']},
        {'question': 'Какое у максима отчество?', 'answers': ['Юрьевич']},
    ],

    "мама": [
        {"question": " Вопрос как лаского называет максима мама?", "answers": ["зайчонок", "кабася"]},
        {'question': 'день рождение когда у максима?', 'answers': ['15 апреля', '15']},
        {'question': 'Какое у максима отчество?', 'answers': ['Юрьевич']},
    ],

    "сестра": [
        {"question": "как ты называешь максима?", "answers": ["маим", "ма"]},
        {'question': 'как часто он с тобой играет?', 'answers': ['часто']},
        {'question': ' Он тебя любит?', 'answers': ['Да', 'очень сильно']},
    ],

    "друг": [
        {"question": "Как ты называешь максима", "answers": ["карелин", "кареша", 'карелия', 'макс', 'максим']},
        {'question': 'каким спортом увлекается максим', 'answers': ['волейбол']},
        {'question': 'какое отчество у максма карелина', 'answers': ['Юрьевич']},
    ]
}

# Инициализация БД
conn = get_db_connection()

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('quiz_max')

# Загрузка изображений
init_assets()
from config import (
    play_button_rect, reboot_button_rect, records_button_rect,
    play_button_img, reboot_button_img, records_button_img,
    background_img, background_rect
)


def description_screen():
    font = pygame.font.SysFont('Arial', 24)
    button_font = pygame.font.SysFont('Arial', 19)
    button_rect = pygame.Rect(300, 500, 100, 50)

    description = [
        "Здравствуйте, это игра про Максима Карелина - это викторина,",
        "созданная для изучения языка PYTHON (для автора).",
        "Игра создана в развлекательных целях. Приятной игры!",
        "Нажмите 'Начать' чтобы продолжить и начать викторину."
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    return

        screen.fill(BACKGROUND_COLOR)

        # Отображение текста описания
        for i, line in enumerate(description):
            text = font.render(line, True, WHITE)
            screen.blit(text, (50, 100 + i * 30))

        # Кнопка "Начать"
        pygame.draw.rect(screen, BLUE, button_rect)
        back_text = button_font.render("Начать", True, WHITE)
        text_rect = back_text.get_rect(center=button_rect.center)
        screen.blit(back_text, text_rect)

        pygame.display.flip()


def role_selection_screen():
    font = pygame.font.SysFont('Arial', 36)
    button_font = pygame.font.SysFont('Arial', 24)
    back_button_rect = pygame.Rect(20, 20, 100, 50)

    # Создаем кнопки для ролей
    roles = [
        {"name": "Папа", "rect": pygame.Rect(300, 150, 200, 50), "value": "dad"},
        {"name": "Мама", "rect": pygame.Rect(300, 220, 200, 50), "value": "mom"},
        {"name": "Сестра", "rect": pygame.Rect(300, 290, 200, 50), "value": "sister"},
        {"name": "Друг", "rect": pygame.Rect(300, 360, 200, 50), "value": "friend"},
        {"name": "Никто", "rect": pygame.Rect(300, 430, 200, 50), "value": "none"}
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Проверка кнопки "Назад"
                if back_button_rect.collidepoint(mouse_pos):
                    return None

                # Проверка кнопок ролей
                for role in roles:
                    if role["rect"].collidepoint(mouse_pos):
                        return role["value"]

        screen.fill(BACKGROUND_COLOR)

        # Заголовок
        title = font.render("Кто вы для Максима Карелина?", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 30))

        # Отрисовка кнопок ролей
        for role in roles:
            pygame.draw.rect(screen, BLUE, role["rect"])
            text = button_font.render(role["name"], True, WHITE)
            text_rect = text.get_rect(center=role["rect"].center)
            screen.blit(text, text_rect)

        # Кнопка "Назад"
        pygame.draw.rect(screen, RED, back_button_rect)
        back_text = button_font.render("Назад", True, WHITE)
        text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, text_rect)

        pygame.display.flip()


def achievements_screen():
    lock_img = pygame.image.load("assets/images/zamok_quiz.png").convert_alpha()
    lock_img = pygame.transform.scale(lock_img, (40, 40))

    font = pygame.font.SysFont('Arial', 36)
    button_font = pygame.font.SysFont('Arial', 24)
    achievements = [
        {"name": "Ты папа!", "unlocked": True},
        {"name": "Ты мама!", "unlocked": False},
        {"name": "Привет дружище!", "unlocked": False},
        {"name": "Привет сестрёнка!", "unlocked": True}
    ]

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
        title = font.render("Достижения", True, WHITE)
        screen.blit(title, (310, 30))

        # Отрисовка достижений
        for i, ach in enumerate(achievements):
            # Жёлтый прямоугольник
            rect = pygame.Rect(100, 100 + i * 100, 600, 80)
            pygame.draw.rect(screen, (255, 255, 0), rect)

            # Текст
            text = font.render(ach["name"], True, (0, 0, 0))
            screen.blit(text, (rect.x + 20, rect.y + 25))

            # Замок (если закрыто)
            if not ach["unlocked"]:
                screen.blit(lock_img, (rect.x + 540, rect.y + 20))

        # Кнопка "Назад"
        pygame.draw.rect(screen, RED, back_button_rect)
        back_text = button_font.render("Назад", True, WHITE)
        text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, text_rect)

        pygame.display.flip()


def settings_screen():
    font = pygame.font.SysFont('Arial', 36, bold=True)
    button_font = pygame.font.SysFont('Arial', 24)
    setting_font = pygame.font.SysFont('Arial', 28)

    settings = {
        "resolution": {"options": ["800x600", "1280x720", "1920x1080"], "selected": 0},
        "volume": {"value": 50, "min": 0, "max": 100},
        "fps": {"value": 30, "min": 30, "max": 120}
    }

    back_button_rect = pygame.Rect(20, 20, 100, 50)
    resolution_rect = pygame.Rect(400, 120, 200, 40)
    volume_slider_rect = pygame.Rect(400, 200, 200, 20)
    fps_slider_rect = pygame.Rect(400, 280, 200, 20)

    dragging_volume = False
    dragging_fps = False

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
                if back_button_rect.collidepoint(mouse_pos):
                    return
                elif resolution_rect.collidepoint(mouse_pos):
                    settings["resolution"]["selected"] = (settings["resolution"]["selected"] + 1) % len(
                        settings["resolution"]["options"])
                elif volume_slider_rect.collidepoint(mouse_pos):
                    dragging_volume = True
                elif fps_slider_rect.collidepoint(mouse_pos):
                    dragging_fps = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_volume = False
                dragging_fps = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_volume:
                    settings["volume"]["value"] = int(
                        (mouse_pos[0] - volume_slider_rect.x) / volume_slider_rect.width * 100)
                    settings["volume"]["value"] = max(0, min(100, settings["volume"]["value"]))
                elif dragging_fps:
                    settings["fps"]["value"] = int(
                        (mouse_pos[0] - fps_slider_rect.x) / fps_slider_rect.width * (120 - 30) + 30)
                    settings["fps"]["value"] = max(30, min(120, settings["fps"]["value"]))

        screen.fill(BACKGROUND_COLOR)

        title = font.render("Настройки", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 30))

        resolution_text = setting_font.render("Разрешение:", True, WHITE)
        screen.blit(resolution_text, (100, 120))

        pygame.draw.rect(screen, (70, 70, 70), resolution_rect, border_radius=5)
        resolution_value = setting_font.render(settings["resolution"]["options"][settings["resolution"]["selected"]],
                                               True, WHITE)
        screen.blit(resolution_value, (resolution_rect.x + 10, resolution_rect.y + 5))

        volume_text = setting_font.render(f"Громкость: {settings['volume']['value']}%", True, WHITE)
        screen.blit(volume_text, (100, 200))

        pygame.draw.rect(screen, (50, 50, 50), volume_slider_rect)
        volume_pos = int(settings["volume"]["value"] / 100 * volume_slider_rect.width)
        pygame.draw.rect(screen, GREEN,
                         (volume_slider_rect.x, volume_slider_rect.y, volume_pos, volume_slider_rect.height))

        fps_text = setting_font.render(f"FPS: {settings['fps']['value']}", True, WHITE)
        screen.blit(fps_text, (100, 280))

        pygame.draw.rect(screen, (50, 50, 50), fps_slider_rect)
        fps_pos = int((settings["fps"]["value"] - 30) / (120 - 30) * fps_slider_rect.width)
        pygame.draw.rect(screen, BLUE, (fps_slider_rect.x, fps_slider_rect.y, fps_pos, fps_slider_rect.height))

        pygame.draw.rect(screen, RED, back_button_rect, border_radius=5)
        back_text = button_font.render("Назад", True, WHITE)
        screen.blit(back_text, (back_button_rect.x + 20, back_button_rect.y + 15))

        pygame.display.flip()


def main_menu():
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

        screen.blit(background_img, background_rect)

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        screen.blit(overlay, (0, 0))

        screen.blit(title_text, title_rect)
        screen.blit(play_button_img, play_button_rect)
        screen.blit(reboot_button_img, reboot_button_rect)
        screen.blit(records_button_img, records_button_rect)

        pygame.display.flip()


def main():
    while True:
        action = main_menu()

        if action == "play":
            description_screen()
            role = role_selection_screen()
            print(f"Вы выбрали роль: {role}")
        elif action == "achievements":
            achievements_screen()
        elif action == "settings":
            settings_screen()


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()