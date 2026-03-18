from src.db.import_cards import import_cards
from src.db.connection import get_db_connection, close_db_connection


if __name__ == "__main__":
    import_cards()

    conn = get_db_connection()
    cursor = conn.execute("SELECT COUNT(*) FROM cards")
    print(cursor.fetchone())

    close_db_connection(conn)