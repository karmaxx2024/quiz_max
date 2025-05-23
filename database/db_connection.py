import psycopg2
from psycopg2 import Error
from config import DB_CONFIG

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE IF NOT EXIST achievements(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    complexity INTEGER NOT NULL,
                    unlocked BOOLEAN DEFAULT FALSE
                    );
                """)

                cur.execute("""
                    INSERT INTO achievements(name)
                    VALUES ('ТЫ ПАПА'),('ТЫ МАМА'),('ПРИВЕТ СЕСТРЁНКА'),('ПРИВЕТ ДРУЖИЩЕ')
                    ON CONFLICT (name) DO NOTHING
                    );
                """)

                conn.commit()
        except Error as e:
            print(f"Ошибка инициализации БД: {e}")
        finally:
            conn.close()