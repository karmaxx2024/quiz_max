import psycopg2
from psycopg2 import Error
from config import DB_CONFIG

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Подключение произошло успешно")
        return conn
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                # Создаем таблицу с UNIQUE ограничением на name
                cur.execute("""
                CREATE TABLE IF NOT EXISTS achievements(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL UNIQUE,
                    complexity INTEGER NOT NULL,
                    unlocked BOOLEAN DEFAULT FALSE
                    );
                """)

                # Теперь можно использовать ON CONFLICT, так как name UNIQUE
                cur.execute("""
                    INSERT INTO achievements(name, complexity)
                    VALUES ('ТЫ ПАПА', 1), ('ТЫ МАМА', 1), ('ПРИВЕТ СЕСТРЁНКА', 2), ('ПРИВЕТ ДРУЖИЩЕ', 2)
                    ON CONFLICT (name) DO NOTHING;
                """)

                conn.commit()
        except Error as e:
            print(f"Ошибка инициализации БД: {e}")
        finally:
            conn.close()