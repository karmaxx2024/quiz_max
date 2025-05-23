from enum import Enum

class GameState(Enum):
    MENU = 0            # Главное меню
    DESCRIPTION = 1     # Экран с описание
    ROLE_SELECT = 2     # Выбор роли
    QUIZ = 3            # Прохождение викторины
    RESULT = 4          # Результаты викторины
    ACHIEVEMENTS = 5    # Просмотр достижений