import pygame

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Прямоугольники для кнопок (изображения будем загружать позже)
play_button_rect = None
reboot_button_rect = None
records_button_rect = None
background_img = None
background_rect = None

# Переменные для изображений (инициализируем позже)
play_button_img = None
reboot_button_img = None
records_button_img = None


FPS = 60
# Настройки PostgreSQL
DB_CONFIG = {
    'user': "postgres",
    'password': "22537171976",
    'host': "localhost",
    'port': "5432",
    'database': "postgres"
    }
# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 205, 50)
RED = (245, 29, 29)
BLUE = (29, 37, 245)
BURGUNDY = (128, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)


def init_assets():
    """Инициализирует изображения и их прямоугольники"""
    global play_button_img, reboot_button_img, records_button_img, background_img
    global play_button_rect, reboot_button_rect, records_button_rect, background_rect

    # Загрузка изображений
    play_button_img = pygame.image.load('assets/images/play_quiz.png').convert_alpha()
    reboot_button_img = pygame.image.load('assets/images/reboot_quiz.png').convert_alpha()
    records_button_img = pygame.image.load('assets/images/records_quiz.png').convert_alpha()
    background_img = pygame.image.load('assets/images/py.imag.jpg').convert_alpha()

    # Масштабируем фоновое изображение под размер экрана
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    background_rect = background_img.get_rect(topleft=(0, 0))

    # Установка прямоугольников для кнопок
    play_button_rect = play_button_img.get_rect(center=(SCREEN_WIDTH//2, 250))
    reboot_button_rect = reboot_button_img.get_rect(center=(SCREEN_WIDTH//2, 350))
    records_button_rect = records_button_img.get_rect(center=(SCREEN_WIDTH//2, 450))
