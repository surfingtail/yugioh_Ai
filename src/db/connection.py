import sqlite3

from src.core.paths import DB_PATH

def get_db_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def close_db_connection(conn):
    if conn:
        try:
            conn.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
            return None
        
