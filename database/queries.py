from database.models import Achievement


def get_achievements(conn):
    achievements = []
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT name, unlocked FROM achievements")
            for name, unlocked in cur.fetchall():
                achievements.append(Achievement(name, unlocked))
    except Exception as e:
        print(f"Ошибка при получении достижения: {e}")
        return achievements


def unlock_achievements(conn, achievement_name):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE achievements
                SET unlocked = TRUE
                WHERE name = %s
            """, (achievement_name,))
            conn.commit()
            return True

    except Exception as e:
        print(f'ошибка не удалось разблокировать достижение: {e}')
        return False

