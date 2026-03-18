from src.core.paths import SCHEMA_PATH
from src.db.connection import get_db_connection, close_db_connection


def init_db():
    conn = get_db_connection()

    if conn is None:
        print("Failed to initialize database: connection error")
        return

    try:
        schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema_sql)
        conn.commit()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        close_db_connection(conn)